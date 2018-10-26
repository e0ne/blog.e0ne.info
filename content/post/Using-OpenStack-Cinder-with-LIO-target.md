---
title: "Using OpenStack Cinder with LIO target"
date: 2017-02-23T19:40:00+03:00
draft: False
category: []
tags: [cinder,lio,tgt,linux]
archives: [2017]
aliases:
    - post/Using-OpenStack-Cinder-with-LIO-target.aspx
---


What is **LIO target**? Linux-OI Target is a Linux SCSI target introduced in a kernel v.2.6.38 and supports different fabrics modules like **FibreChannel, iSCSI, iSER**, etc. It works in a kernel space, so it’s faster than tgtd which is used in Cinder by default. Why do we still use **tgtd** instead of more faster LIO in Cinder by default? It’s only because we have to support rolling upgrades and we don’t know how to migrate from TGTd to LIO in a such way and pass Grenade successfully.

We’ve got non-voting **gate-tempest-dsvm-full-lio-ubuntu-xenial** job for a while. Due to some of my performance tests results it’s really faster than tgtd. So, how can you use it?

It’s pretty easy with LVM + Devstack. Everything you need is to add '**CINDER_ISCSI_HELPER=lioadm**' to your **localrc/local.conf**.

If you have already configured Cinder+LVM it’s easy too to switch to the new target driver. I mean that you don’t have any in-use volume now but you have Cinder with LVM configured and running. Just follow these steps:

1) first of all, you have to install ‘rtslib-fb’ package using pip:

**# pip install rtslib-fb**

or using OS package manager:

**# apt-get install python-rtslib-fb **

2) stop tgt:

**# sudo service tgt stop**

3) change **/etc/cinder/cinder.conf** to use LIO driver:

Set ‘**iscsi_helper = lioadm**' instead of ‘**iscsi_helper = tgtadm**’

 

4) restart cinder and enjoy it!

 

