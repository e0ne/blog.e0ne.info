---
title: "Minimal OpenStack Cinder setup"
date: 2019-01-07T23:31:24+02:00
category: [openstack]
tags: [openstack, cinder, docker, loci, devstack]
archives: [2019]
author: Ivan Kolodyazhny
---

During OpenStack Cinder development you may want to have some minimal working configuration to run the only Cinder on your environment. If you don’t need to test full volume attach flow with Nova, you may need to run only Cinder(cinder-api, cinder-scheduler, and cinder-volume, even cinder-backup is optional), RabbitMQ, and MySQL.

Usually, for Cinder development, I don’t need full OpenStack up and running on my virtual machine. I just need to have only Cinder itself and such required things like database and message queue.

To have such development environment you have two options. OK, technically, there are four options: you can configure everything manually or use ay configuration management like Ansible, Puppet, Chef, etc.

Depend on what environment do I need, I use containerized or virtualized deployments. For light-weight containerized Cinder environment you can use [LOCI](https://github.com/openstack/loci) - Lightweight Open Compute Initiative. Everything you need is to run `docker-compose up` in [`cinder/contrib/block-box`](https://github.com/openstack/cinder/tree/master/contrib/block-box) directory. It will run containers with Maria DB, RabbitMQ and cinder services o your laptop or desktop. By default, it uses LVM as a backend.

Sometimes I need more complicated deployment with Cinder: Ceph backend, Tempest or something else. For such things, I use [Devstack](https://docs.openstack.org/devstack/latest/) on the virtual machine with Cinder only. Of course, I run MySQL and RabbitMQ as well. I use ‘noauth’ mode to run my Cinder without Keystone. I’ve got my [local.conf](https://gist.github.com/e0ne/985010123015e3f961ee99e032544145) for Devstack which could be easily modified to add additional services and/or change Cinder backend.
