---
title: "How to exdend your VM's drive size in 8 steps"
date: 2015-08-31T22:05:00+03:00
draft: False
category: [Linux]
tags: [kvm,qcow,vm]
archives: [2015]
aliases:
    - post/How-to-exdend-your-VMs-drive-size-in-8-steps.aspx
---


**It’s my first try to blog in English. Feel free to comment for any typo, grammar errors, etc.**

There are nothing new, nothing innovative below. There are just a step-by-step guide to not forget and to not google each time when I need it.

Usually, on my dev environment, I’ve got KVM instances with disk images in QCOW format. So time to time I need to extend my virtual disks to get more free space.

<ol>
<li>Shutdown VM:
<ul>
- `**sudo shutdown -p now**` inside VM
- `**sudo virsh shutdown <vm_name>**` on my host
</ul>
</li>
- Find QCOW file to change it:<br />Be default, it’s located at `/var/lib/libvirt/images`<br />`**virsh dumpxml dsvm1 | grep file**`<br />Find something like:<br /><disk type='file' device='disk'><br /><source file='/var/lib/libvirt/images/devstack.img'/>
- **Create backup of your virtual drive** (E.g. `cp /var/lib/libvirt/images/devstack.img /var/lib/libvirt/images/devstack.img.bak`)!!!!
<li>Change QCOW image size: `**sudo qemu-img resize /var/lib/libvirt/images/devstack.img +10G**`  - this command increases size with 10 GB more
<ul>
- If image has snapshots, you need to delete them first:<br />**sudo qemu-img snapshot -l /var/lib/libvirt/images/devstack.img**<br />**sudo qemu-img snapshot -d <snapshot_id> /var/lib/libvirt/images/devstack.img**
</ul>
</li>
- Boot VM: `**sudo virsh start <vm_name>**`
- **NOTE**: I don’t care about disk data in this example. But I have backup (see #3) and can restore all needed data.<br />Create new partition table with fdisk. fdisk can’t change partition size, we need to delete and create a new one:<br />**sudo fdisk /dev/sdb**<br />‘d’ - delete partitions(s)<br />‘p’ - create new partition(s)<br />‘w’ - write changes
- Mount drive to your VM:<br />**sudo mount /dev/sdb1 /mnt/data**
- Create filesystem:<br />**sudo resize2fs /dev/vda3**
- In case, if you use something else like parted instead of fdisk, you could just extend filesystem size:<br />**sudo mkfs.ext3 /dev/sdb1**
</ol>

<li>Shutdown VM:
<ul>
1. `**sudo shutdown -p now**` inside VM
1. `**sudo virsh shutdown <vm_name>**` on my host
</ul>
</li>
1. Find QCOW file to change it:<br />Be default, it’s located at `/var/lib/libvirt/images`<br />`**virsh dumpxml dsvm1 | grep file**`<br />Find something like:<br /><disk type='file' device='disk'><br /><source file='/var/lib/libvirt/images/devstack.img'/>
1. **Create backup of your virtual drive** (E.g. `cp /var/lib/libvirt/images/devstack.img /var/lib/libvirt/images/devstack.img.bak`)!!!!
<li>Change QCOW image size: `**sudo qemu-img resize /var/lib/libvirt/images/devstack.img +10G**`  - this command increases size with 10 GB more
<ul>
1. If image has snapshots, you need to delete them first:<br />**sudo qemu-img snapshot -l /var/lib/libvirt/images/devstack.img**<br />**sudo qemu-img snapshot -d <snapshot_id> /var/lib/libvirt/images/devstack.img**
</ul>
</li>
1. Boot VM: `**sudo virsh start <vm_name>**`
1. **NOTE**: I don’t care about disk data in this example. But I have backup (see #3) and can restore all needed data.<br />Create new partition table with fdisk. fdisk can’t change partition size, we need to delete and create a new one:<br />**sudo fdisk /dev/sdb**<br />‘d’ - delete partitions(s)<br />‘p’ - create new partition(s)<br />‘w’ - write changes
1. Mount drive to your VM:<br />**sudo mount /dev/sdb1 /mnt/data**
1. Create filesystem:<br />**sudo resize2fs /dev/vda3**
1. In case, if you use something else like parted instead of fdisk, you could just extend filesystem size:<br />**sudo mkfs.ext3 /dev/sdb1**

 

