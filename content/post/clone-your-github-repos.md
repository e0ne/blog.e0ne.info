---
title: "Clone Your Github Repos"
date: 2019-03-03T23:00:41+02:00
category: [development environment]
tags: [everything-as-a-code, github]
archives: [2019]
author: Ivan Kolodyazhny
---

Since GitHub allows to store unlimited private repositories, I moved everything there. It’s really great to have such sources storage for free.

Once I pushed everything to GitHub, I need to sync my repositories over all environments I have.  I wrote a simple Python script below to clone all my GitHub repositories:
<script src="https://gist.github.com/e0ne/1ab17bcc62cd4f8f698efdf8b3840d19.js"></script>

My use case could not fit everyone, but you can adjust my script to cover your use cases. Everything I need is:

* Clone all my repos to some directory
* Clone all forks into ‘forks’ sub-directory
* Clone all repose from organizations I’m a member of into the ‘orgname’ sub-directory
* Have a simple way to execute `git pull` for each repository

I hope, this script will be helpful for somebody except me.
