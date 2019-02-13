---
title: "OpenStack Cinder Performance Testing Approach Part 1 of 2"
date: 2019-02-13T21:24:20+02:00
category: [OpenStack]
archives: "2019"
tags: [openstack, cinder, performance]
author: Ivan Kolodyazhny
---

__NOTE__: This post was initially written a few years ago, so something could
be outdated.

## What is Cinder

### High-level Cinder Architecture

Cinder contains 3 main components: Cinder API (c-api), Cinder Scheduler
(c-sched) and Cinder Volume (c-vol). Cinder Backup is a bit different and will
be described later.

All Cinder components communicate between each other using RPC protocol. In our
case, it’s an AMPQ protocol with RabbitMQ backend. All data is stored in the
database (MySQL DB).

Cinder is responsible only for the volume management plane. Cinder backends
(storages) are responsible for data plane and all volumes manipulations.

### Cinder API

Like all OpenStack services, Cinder provides HTTP REST API. Today, there are 3
versions of the API:

* v1 - removed
* v2 - deprecated, contains all features until Mitaka release and performance
  improvements like paging, limits, etc
* v3 - current version, contains all features of API v2, all new features are
  implemented as micro versions.

I do not recommend to use API v2. The latest python-cinderclient uses v3 by
default.

### Cinder CLI

There is an official OpenStack Cinder client called ‘python-cinderclient’.
Unfortunately, python-openstackclient doesn’t support all Cinder APIs. So the
community recommends using python-cinderclient.

### Cinder logging

All logs are stored in `/var/log/cinder/` directory. All services write log to
different files. E.g.: `/var/log/cinder/cinder-volume.log`,
`/var/log/cinder/cinder-api.log`, etc.

If we don’t turn on debug logs, there will be very limited data in logs to
troubleshoot something. To enable debug logs you have to pass the following
steps:

* Add `debug=true` flag in `/etc/cinder/cinder.conf`
* Change `loglevel` to `DEBUG` for the root logger in
  `/etc/cinder/cinder-logging.conf` if exists
* Restart all Cinder services

## What kind of tests are described in this document?

There are different performance tests approached. This document describes
Cinder API and components performance. By performance, we mean how much time
will take to complete API call. We don’t test backends performance and/or
DB/message queue, etc.

### Why do we need these tests?

We want to know what is our expected Cinder performance:

* What is expected time to handle request A?
* How many requests B can Cinder handle in parallel?
* What does impact Cinder performance?
* Where is performance bottleneck?

As a result of performance testing, we should have answers to the questions
above and create recommendations on how to configure Cinder to work faster.
These tests results could be a source of new performance-related bugs.

### What tools/frameworks should we use?

There are a community and industry standard tools for performance testing like
Rally, Mongoose, Wally, Tsung, jMeter, etc. We can use existing and Rally and
Wally scenarios to test Cinder performance.

## Performance testing for different Cinder components

We should describe what actually data do we want. Different components require
different tests. Let’s discuss CRUD (Create-Read-Update-Deletes) API calls.

### Create APIs

In general, there are two different types of ‘create’ command: create something
on the backend (volume, snapshot, consistency group, etc) and create a DB
record (volume type, extra spec, quota, etc).

#### Create APIs without backend interactions

These types of APIs calls are executed only by c-api services.
What components and configuration options could affect performance:

* Database performance
* Memory allocation
* CPU usage
* How many c-api workers are running on the node
* Do we use eventlet or Apache/Ngingx+WSGI

#### Create APIs with backend interactions

These types of APIs calls are executed by c-api, c-shed and c-vol services.
Usually, such operations are asynchronous, so after we’ll invoke
`cinder create volume` command, API returns `202 Accepted` code. It means,
Cinder created a DB record and sent a message by AMPQ to c-sched or c-vol.
In such cases, in the ideal world, we should have 2 different types of tests:

* How quickly c-api creates something
* How quickly Cinder resource will be in the ‘available’ state instead of
  ‘-ing’ state

What components and configuration options could affect performance:

* All components, described in ‘Create APIs without backend interactions’
  section
* In case, where c-api, c-sched and c-vol are located on the different nodes,
  we should be sure, that networking would not be a bottleneck
* RabbitMQ performance
* Cinder backend performance

Depends on backend and Cinder driver, Cinder communicates with a storage using
different solutions: invoke Linux executable (e.g. LVM), call some 3rd party
libs and/or HTTP REST API. It means, that we can’t say that ‘Cinder creates
volume in 5 seconds‘ using some backend. There are a lot of affected components
which could affect performance tests. That’s why __I strongly recommend do not
use any real back-end for Cinder performance tests__. We have to use Fake
driver for tests. For more details, please see ‘Storage Backends’ sections.

__Proposal__: implement ‘create volume(image)/snapshot’ tests for each tested
backend without Cinder to get numbers how much time each backend takes to
create volume/snapshot/etc. Then we can compare the results of such tests with
Cinder performance tests results.

### Read APIs

These APIs tests are almost the same as for ‘Create APIs without backend
interactions’. Cinder reads data from DB and returns it to the consumer.

There are exceptions from this rule: few APIs call c-vol for data, so the
supposed to be slower due to RPC communications.

### Update APIs

Please, read the ‘Create APIs‘ section. Update APIs are very similar to Create
APIs with the same behaviors.

### Delete APIs

Please, read the ‘Create APIs‘ section. Delete APIs are very similar to
Create APIs with the same.

#### Delete volumes/snapshots/backups performance testing

Storages and Cinder drivers have different ‘delete’ feature implementation.
According to it, volume/snapshot/etc deletion could take some time. E.g. LVM
driver uses ‘dd’ tool to clean-up volume with /dev/zero. Ceph has own solution
to shred volume after deletion. For Cinder performance tests we have to disable
such options if possible.

__Proposal__: implement backend-specific tests for volume/snapshots deletion
and compare their results with Cinder tests.

### Testing using Fake Driver

Fake Driver allows you to run both functional and performance tests without
real storage backend impact. It means. We test only Cinder with a minimum
required 3rd party software and hardware. The minimum Cinder requirements are
Cinder, Keystone, RabbitMQ, MySQL, [Nova and Glance for related tests].

## What could impact Cinder performance?

### Cinder components

__NOTE__: Until Ocata release, c-api and c-vol services cannot be runned in
Active/Active HA mode. We use HAProxy for c-api and config hacks for c-vol to
achieve working HA solution.

#### API workers

By default, Cinder runs one API worker per CPU. We can configure this option if
needed in a case when we use Eventlet WSGI implementation. We don’t need to
change it if Cinder works under Apache or Nginx.

#### Cinder Scheduler

Usually, Cinder scheduler is runned on Controllers nodes. There should not be
a big performance impact if we run more or less c-sched services. We start
several s-sched services to achieve HA mode.

#### Cinder Volume

In general, we run one c-vol service per backend. We can run more c-vol
services per backend when Active/Active HA will be implemented. We can’t run
multiple c-vol services for LVM and Block Device Driver now. You can configure
multiple c-vol per backend for Ceph and any other distributed or remote
storages (e.g. NetApp, EMC, SolidFire, etc). Multiple c-vol could increase
Cinder CRUD operation performance if storage is not a bottleneck. We have to
test how to increase or decrease c-vol services number impacts performance.

### 3rd party components

#### Storage Backends

Different backend and even their configuration have different CRUD performance.
So we have to test each backend separately from Cinder to get numbers
according to CRUD operation performance. After these test, we have to run
Cinder CRUD performance tests with real backend and compare results to answer
the question: what is the Cinder’s overhead working with specified backend?

##### LVM

Create/delete LVM volume operations are fast enough and depend on disk I/O. In
the case of Cinder, by default, it uses secure delete feature to full volume
with zeros using ‘dd’ tool before deletion. That’s why disk I/O could impact
performance. We can/should disable this feature for Cinder performance testing.

##### Ceph

Create volumes and snapshots in Ceph are a fast operation. But Ceph uses secure
delete feature while deletion. It increases the time of deletion depended on
volume size.

### Apache/Nginx or Eventlet-based

Eventlet-based deployments are supported only for old releases now.
Apache+mod_wsgi or Nginx+uWSGI will be faster than eventlet. Configuring
Cinder API + Apache/Nginx should be done like any other WSGI application and
follow industry best practices.

__NOTE__: I did some performance testing for this in the past, but results are
lost.

### Database

We have to track DB performance during Cinder testing to find the slowest
queries, be sure that there are enough resources for the DB Server.

There are a big performance and concurrency impact created by DB drivers.
PyMySQL works better in a concurrency mode with eventlet than MySQL-Python. We
have to test Cinder CRUD operations with a Fake Driver to get real numbers.

### Message bus (RabbitMQ)

While Cinder performance testing we should monitor RabbitMQ state to be sure
that there is enough OS resources and both RabbitMQ with oslo.messaging works
well with the current load.

### Networking

Because Cinder is a distributed component wiсh is runned on different nodes,
we have to have enough networking resources, I/O and latency to provide fast
communication between Cinder nodes.

### CPU Load

As an any component, Cinder should have enough CPU resources. We should
monitor CPU load, average load, what is the main CPU users on each node when
Cinder is running.

### Disk Load

In general, please see ‘CPU Load’ According to different backends like LVM and
Block Device Driver, we have to provide enough disk  I/O bandwidth for c-vol
services. It could impact such operations like `create volume from image` and
`upload volume to image’`

### Memory

Please, see ‘CPU Load’ section.

## Useful Links

* https://wiki.openstack.org/wiki/Cinder
* http://developer.openstack.org/api-ref-blockstorage-v2.html
* http://docs.openstack.org/cli-reference/cinder.html
* https://wiki.openstack.org/wiki/Rally
* https://github.com/Mirantis/disk_perf_test_tool/wiki
* https://github.com/emc-mongoose/mongoose
* http://tsung.erlang-projects.org/
* http://jmeter.apache.org/
