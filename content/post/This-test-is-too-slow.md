---
title: "This test is too slow"
date: 2017-07-28T13:48:00+03:00
draft: False
category: [Python]
tags: [unit tests,profiler]
archives: [2017]
aliases:
    - post/This-test-is-too-slow.aspx
---


Sometimes we need to understand why unit-test is so slow. Sometimes I’m to lazy to go deep to understand why.

That’s why I’ve created a very simple profiled class to make unit-tests profiling fast and simple. I used only cProfile, so it will work on any Python project. It’s so simple, so I can’t talk about it more. You can install it via ‘pip install ProfiledTest’ and use it like:

 

GitHub url: [https://github.com/e0ne/profiled_test](https://github.com/e0ne/profiled_test)

