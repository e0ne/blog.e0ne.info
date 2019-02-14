---
title: "Code Coverage and Cyclomatic Complexity"
date: 2019-02-14T23:38:30+02:00
category: [offtopic]
archives: "2019"
tags: [unit tests, software engineering]
author: Ivan Kolodyazhny
---

Code coverage for unit tests and
[cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
could be extremely useful metrics for your code. They help you to understand
if something is not tested at all by unit tests. A combination of these metrics
allows you to understand how many unit tests you should implement and what is
your code complexity. I’m pretty sure, that everybody agrees that more coverage
and less complexity is that you should aim for.

I just realized that even I’ve got tools for coverage and cyclomatic complexity
analysis, I don’t use them on a regular basis if there are no jobs on CI. IMO,
it’s a good idea to do this on CI. I hope, my colleges will agree with me.
