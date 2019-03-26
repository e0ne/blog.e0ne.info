---
title: "I need more (fake) disks"
date: 2019-01-24T21:52:22+02:00
category: [linux]
tags: [losetup, devices, loopback, lvm, disks, linux]
archives: [2019]
author: Ivan Kolodyazhny
---

Sometime I need some additional disks or volume groups to do some testing.
E.g. it’s widely used for [OpenStack Cinder](https://github.com/openstack/cinder)
testing with LVM driver.

Usually, I don’t have additional disks to work with:(. That’s why I use
loopback devices instead. It’s an easy to configure solution. Of course, it
works a but slower than on a real hardware but it’s absolutely acceptable for
many scenarios.

I’ll show you an example based on [Devstack](https://github.com/openstack-dev/devstack/blob/e812d284b8970d0242f35b3d15b923d246fa7308/lib/lvm#L123)
solution.

There are only three steps to do it.

1. Create backing file to store your data:
```sudo dd if=/dev/zero of=/opt/fake-lvm bs=1M count=20480``` - it will create
a 20Gb file filled with zeros.

2. Create new loopback device
```sudo losetup -f --show /opt/fake-lvm``` - this command returns a new
loopback device name like `/dev/loopN`

3. After this, you can create partitions and filesystems using `fdisk` and
`mkfs` utilities or new volume group via `sudo vgcreate test-vg /dev/loopN` command

More information about `losetup` you can find in
[man](https://linux.die.net/man/8/losetup)
