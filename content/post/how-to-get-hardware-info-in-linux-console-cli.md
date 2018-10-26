---
title: "How to get hardware info in Linux console/CLI"
date: 2018-10-02T12:50:00+03:00
draft: False
category: [Linux]
tags: [linux,cli,hardware]
archives: [2018]
aliases:
    - post/how-to-get-hardware-info-in-linux-console-cli.aspx
---


Sometimes it’s needed to get hardware information on your Linux desktop or server using the command line only. Of course, you can do everything via CLI in Linux. Here just some reminders for myself how to do it.

Most of the information you can get using the following three commands:

- lspci - list all PCI devices
- lshw - list hardware
- dmidecode - DMI table decoder

Using multiple keys to these CLI tools you can get everything you need.

It's not a full guide. It's just a list of commands to quickly identify what hardware do you have. I recommend executing all commands with root privileges to get more information.

## 1. What CPU do I have?

**1.1.** I think, almost everybody knows the command to get CPU information about your CPU. Here is just a friendly reminder:

**# cat /proc/cpuinfo**

## 2. How to get your GPU information?

**2.1.** A very short information:

**# lspci | grep -i --color 'vga\|3d\|2d'**

01:00.0 VGA compatible controller: ***

**2.2.**Need more details about your GPU?

**# lspci -v -s 01:00.0**

2.3. In the case of Nvidia GPUs you can collect some use `nvidia-smi` tool to get some information:

 

**$ nvidia-smi**

## 3. Motherboard

**3.1.** If you need just a model name:

**#dmidecode -s baseboard-product-name**

**3.2.** If you’re too lazy to google your motherboards specs, you can do it via the command below:

**# dmidecode -t baseboard**

## 4. RAM

Everybody knows `**free**` utility. It’s one of the easiest ways to see how many free or used memory you have. To determinate what actually RAM do you have you can use ‘**dmidecode**` or `**lshw**` utilites.

**4.1.** dmidecode:

**# dmidecode --type 17**

**4.2.** lshw:

**# lshw -short -C memory**

## 5. How to get your HDD or SSD hardware info?

For Linux, it doesn’t matter you’ve got SSD or HDD. To get their hardware information such a serial or model number, configuration and capabilities you can use the same software.

**5.1.** hdparm - get/set SATA/IDE device parameters

**# hdparm -I /dev/sda**

**5.2.** If you need to know more about your storage controllers and storage devices, just type the following command:

**# lshw -class disk -class storage**

## 6. Network Controllers Info (NIC)

Last but not least, there are two commands to get the information about your NICs.

**6.1. ****lspci:**

**# lspci | egrep -i --color 'network|ethernet'**

**6.2.**  lshw:

**# lshw -class network**

 

