---
title: "How to Get Hardware Info in Linux Console Cli"
date: 2018-10-05T12:44:10+03:00
draft: true
category: [linux]
tags: [linux,cli,hardware]
aliases:
    - post/how-to-get-hardware-info-in-linux-console-cli.aspx
---

Sometimes it’s needed to get hardware information on your Linux desktop or server using the command line only. Of course, you can do everything via CLI in Linux. Here just some reminders for myself how to do it.

Most of the information you can get using the following three commands:

*   lspci - list all PCI devices
*   lshw - list hardware
*   dmidecode - DMI table decoder

Using multiple keys to these CLI tools you can get everything you need.

It's not a full guide. It's just a list of commands to quickly identify what hardware do you have. I recommend executing all commands with root privileges to get more information.

1\. What CPU do I have?
-----------------------

**1.1.** I think, almost everybody knows the command to get CPU information about your CPU. Here is just a friendly reminder:

_\# cat /proc/cpuinfo_

2\. How to get your GPU information?
------------------------------------

**2.1.** A very short information:

_\# lspci | grep -i --color 'vga\\|3d\\|2d'_

01:00.0 VGA compatible controller: \*\*\*

**2.2.**Need more details about your GPU?

_\# lspci -v -s 01:00.0_

2.3. In the case of Nvidia GPUs you can collect some use \`nvidia-smi\` tool to get some information:

_$ nvidia-smi_

3\. Motherboard
---------------

**3.1.** If you need just a model name:

_#dmidecode -s baseboard-product-name_

**3.2.** If you’re too lazy to google your motherboards specs, you can do it via the command below:

_\# dmidecode -t baseboard_

4\. RAM
-------

Everybody knows \`_free_\` utility. It’s one of the easiest ways to see how many free or used memory you have. To determinate what actually RAM do you have you can use ‘_dmidecode_\` or \`_lshw_\` utilites.

**4.1.** dmidecode:

_# dmidecode --type 17_

**4.2.** lshw:

_\# lshw -short -C memory_

5\. How to get your HDD or SSD hardware info?
---------------------------------------------

For Linux, it doesn’t matter you’ve got SSD or HDD. To get their hardware information such a serial or model number, configuration and capabilities you can use the same software.

**5.1.** hdparm - get/set SATA/IDE device parameters

_\# hdparm -I /dev/sda_

**5.2.** If you need to know more about your storage controllers and storage devices, just type the following command:

_# lshw -class disk -class storage_

6\. Network Controllers Info (NIC)
----------------------------------

Last but not least, there are two commands to get the information about your NICs.

**6.1. **_lspci:_

_\# lspci | egrep -i --color 'network|ethernet'_

**6.2.**  lshw:

_# lshw -class network_