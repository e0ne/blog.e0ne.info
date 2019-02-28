---
title: "TypeScript: forgot to compile"
date: 2019-02-28T23:13:37+02:00
category: [offtopic]
tags: [typescript]
archives: [2019]
author: Ivan Kolodyazhny
---

I’m working too much time with script languages like Python, JavaScript, and
even bash. I almost forgot that sometimes I need to compile my sources.
A stupid mistake was made on TypeScript project I’m working on: I didn’t add
a job on CI which will compile sources to JavaScript.

Of course, I use `npm run build` build to make a production bundle. I see
TypeScript compile errors in my console when I run the code. But there are
no checks on CI yet:(.

I need to add a CI job which will execute two simple commands:
`tsc --project package.json` and `npm run build` to check if the code could
be compiled anytime.
