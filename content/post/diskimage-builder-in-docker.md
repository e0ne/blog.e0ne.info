---
title: "Diskimage-builder in Docker"
date: 2019-01-17T21:08:04+02:00
category: [linux]
tags: [development environment, everything-as-a-code]
archives: [2019]
author: Ivan Kolodyazhny
---

[diskimage-builder](https://docs.openstack.org/diskimage-builder/latest/index.html)
is a tool for automatically building customized operating-system images for use
in clouds and other environments.

Unfortunately, I can't do everything in Docker so I have to use VMs a lot.
diskimage-builder helps me a lot to build basic VM images with pre-installed
packages, my SSH key, etc.

Since I try to have my development environment as clean, as possible I do not
install additional packages on my desktop. Any Python package I install in the
virtualenv. For system-level packages (deb/rpm) I try to use Docker and
Virtual Machines.

That’s why I created [Dockerfile](https://github.com/e0ne/diskimage-builder-docker)
for diskimage-builder. There is a sample file to build and run this container.
Do not forget to run container in `--privileged` mode because it’s required to
get chroot working.

Here is my GitHub repository with Dockerfile:
[https://github.com/e0ne/diskimage-builder-docker](https://github.com/e0ne/diskimage-builder-docker)


P.S. I’ll add this to the Docker Hub soon.
