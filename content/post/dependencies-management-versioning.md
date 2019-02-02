---
title: "Dependencies management: versioning"
date: 2019-02-02T22:59:29+02:00
category: [software development]
tags: [dependencies]
archives: [2019]
author: Ivan Kolodyazhny
---

It’s a really complicated topic. Almost everyone has own opinion on it. I’ll
try to describe you several patterns with pros and cons for each.

It doesn’t matter if it’s a python dependency in requirements.txt or a
javascript one in package-lock.json file.

What could go wrong? First of all, there are several approaches how dependency
could be described:

## Case 1: without version

It’s a great approach for development on early stages. You always use the
latest version and you’ll be notified soon if your application stopped to work.
On the other hand, it’s a nightmare for production deployment. Everything could
stop work at any moment after any operating system update.

## Case 2: with strong version pinning

It’s the most stable approach. Once you start your application and freeze
dependencies, everything will work without any issue. A lot of deployment
engineers prefer this way. It’s good for production but it does not provide a
good development experience. After each version update in your requirements
file, you need to test your application with a new dependency version before
starting to use it

## Case 3: min/max range

It’s one of the easiest ways to handle dependencies. Once you added new
dependency into the project, you specify the version as a minimum one. If
something fails with a new version, you just add a maximum cap for your
dependency version and use it until application will support it.


## Case 4: min/max range with some exception

It’s almost the same as a previous one but adds an ability to skip some
version. E.g. you can work with v.1.0-2.5, but v.2.4.3 introduces some issue
which you want to avoid. IMO, it’s the most powerful and convenient way to deal
with dependencies in a project. It’s flexible enough both for developers and
deployment engineers.
