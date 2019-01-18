---
title: "Not a DNS Server for Libvirt"
date: 2019-01-18T22:36:28+02:00
category: [linux]
tags: [development environment, linux, libvirt, kvm, qumy, hack]
archives: [2019]
author: Ivan Kolodyazhny
---

Sometimes I’m too lazy to repeat the same task so I do some automation to make
my life easier. Unfortunately, I don’t have enough time to do it well each time.
That’s why I prefer ‘good enough’ way. I implement something good enough for me
and refactor it once I have time.

I use virtual machines on my desktop a lot. Usually, I have several of them up
and running. I don’t like to remember an IP address for each of them, that’s
why I prefer to use hostnames. Based on this, I’ve googled to some
*lightweight* solution to have something like DNS server for my KVM instances
and *it must work inside corporate network*. That’s why I can’t use dnsmasq or
something else.

I googled for a solution about 2 minutes without any acceptable result. After
that, I spent about 5 minutes more to create this script:
[https://gist.github.com/e0ne/0f9b83a549a2f39fc09230e98cab24e6](https://gist.github.com/e0ne/0f9b83a549a2f39fc09230e98cab24e6).
The code is not ideal, but it works well. I spent about 10 minutes and I just
use it for months. I also created crontab job `/etc/cron.d/vm-resolver`
to run my not-a-dns-server each 15 minutes:

```
*/15 * * * *    root    python3 /opt/vm-resolver
```

I hope it will be useful for somebody. Also, I hope I’ll have time to refactor
it, write some tests and publish to pypi.
