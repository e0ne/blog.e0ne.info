---
title: "Code Search for Your Repos"
date: 2019-01-25T21:32:33+02:00
category: [notes]
tags: [sources, grep, hound]
archives: [2019]
author: Ivan Kolodyazhny
---

Once you have more than one repository with sources you starting to search
across all of them. You can use IDE and/or your favorite text editor to search
across an open project. Usually,  I use ‘grep’ to search in my '~/src'
directory.

It works pretty well when you have a few repos. But once you’ve got tens of
them, it’s it’s time to find something convenient than 'grep'. This way is good
only if you prefer GUI rather than CLI.

[Hound](https://github.com/etsy/hound) is an extremely fast source code search
engine. It provides a simple web UI to search across your repositories. Hound
works with different version control systems and public or private
repositories. Unfortunately, it searches only for a master branch now, but
there is a [pull request](https://github.com/etsy/hound/pull/275) to fix it.
With a minimal feature set, it helps a lot to find anything you implemented in
the past.
