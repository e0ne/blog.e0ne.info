---
title: "UUIDs usage in /etc/fstab"
date: 2019-03-08T22:58:17+02:00
category: [linux]
tags: [fstab]
archives: [2019]
author: Ivan Kolodyazhny
---




`/etc/fstab` is a [config file](http://man7.org/linux/man-pages/man5/fstab.5.html) to store static information about file system. It’s a native place to add disks information you would like to mount automatically on each system start. It has a pretty simple format:

```
[device] [mountpoint]    [filesystem]    [options]   [dump]  [fscheck pass count]
```

I used such format for the years and it worked before:

```
/dev/sdb1       /opt/media       ext4    defaults        0       0
```

I don’t know how many people do the same. I think this is the most used way to mount partitions during the startup. The main issue is that you have to specify the correct device name like `/dev/sdb1` for each partition. It means you have to have the same disk names even after the system upgrade or just after pulling out and plugin again your hard drive or SSD.

To omit this behavior you ca use the following format:

```
UUID=e11165a4-1b4c-4244-971e-25c50a1dbf04 /opt/media ext4 defaults 0 0
```

The only difference is using `UUID=...` instead of `/dev/…`. This UUID is a unique identifier for the filesystem. It allows you to not care a lot about disks order connection during hardware maintenance or update. To get this UUID just execute `blkid` CLI tool and you’ll get everything needed.
