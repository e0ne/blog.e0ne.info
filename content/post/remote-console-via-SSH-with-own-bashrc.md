---
title: "Remote console via SSH with own bashrc"
date: 2017-08-09T22:00:00+03:00
draft: False
category: [Linux]
tags: [bash,ssh,shell,everything-as-a-code]
archives: [2017]
aliases:
    - post/remote-console-via-SSH-with-own-bashrc.aspx
---


I think, most of us have customized bash or zsh environment. I'm too lazy to switch from bash to zsh, so I use bash on my laptop. There are some benefits: bash is still the more popular shell, so it exists on mostly Linux-based servers.

That's why I try to use my [`.bashrc`](https://github.com/e0ne/dot-files/blob/master/.bashrc) wherever it's possible. But on a remote server, sometimes you don't have the own user account. That's why I've added a very simple alias for `ssh` command to mine `[.bashrc`](https://github.com/e0ne/dot-files/blob/master/.bashrc#L51) file:

It will create temporary file with your `.bashrc` content on a remote host and remove it once the session ends. The backside of this solution is your ssh connection will start with some delay to copy your`.bashrc` file to the remote host. It's not an issue for me now and I'm happy this.

The next step is to make the same with `.vimrc` with all needed plugins.

