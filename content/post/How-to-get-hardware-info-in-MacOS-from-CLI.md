---
title: "How to Get Hardware Info in MacOS From CLI"
date: 2019-02-07T23:15:45+02:00
archives: "2019"
category: [nix]
tags: [macos,cli,hardware]
author: Ivan Kolodyazhny
---

I know that most MacOS users use GUI instead of CLI but sometimes it’s faster
to use CLI. A also prefer command line when I need to copy results: it’s easier
to copy text rather than do snapshots even with hotkeys and send it.

There are two tools I use to get hardware info: `system_profiler` and `sysctl`.

I do not like to copy the documentation, so I just drop a few most interesting
for me commands:

* sysctl -n machdep.cpu.brand_string - view CPU information
* system_profiler SPNVMeDataType - view NVMe SSD information
* system_profiler SPMemoryDataType - view RAM information
* system_profiler SPDisplaysDataType - display ad GPU information
