---
title: "Internal Bash Variables"
date: 2019-03-04T22:01:58+02:00
category: [linux]
tags: [bash]
archives: [2019]
author: Ivan Kolodyazhny
---

I didn’t pay attention to some variables I used in bash script before. I just
realized that there are a lot of variables I don’t see in the output of `env`
or `export` commands.

There a lot of
[internal bash variables](http://tldp.org/LDP/abs/html/internalvariables.html)
you can use or change. I don’t have a lot of bash scripts in my sources.
Usually, I don’t write scripts bigger than 10-20 lines. TBH, most of scripts
are copy-pasted from somewhere with minor changes. I prefer to you Python where
it’s possible and reasonable.

I was surprised that there are a lot of useful bash variables like `$OSTYPE`,
`$PWD` (I don’t need to call `pwd` in my scripts now!), `$SECONDS` (can be used
like some mini-prrofiler), `$?`, `$LINENO` and others.

A full reference of the internal bash variable could be found here:
[http://tldp.org/LDP/abs/html/internalvariables.html](http://tldp.org/LDP/abs/html/internalvariables.html).
