---
title: "Lerned About Pystone"
date: 2019-01-04T15:27:15+02:00
category: [python, offtopic]
tags: [python, benchmark]
archives: [2019]
author: Ivan Kolodyazhny
---

[pystone](https://github.com/blackberry/Python/blob/master/Python-3/Lib/test/pystone.py)
is a simple Python benchmark which is included in a standard library.

As any other benchmark you need to be careful with its' results. It was
interestings how fast are my environments:

* Intel Core i5 4590 @ 3.30GHz:

  ```python
Pystone(1.2) time for 50000 passes = 0.19486
This machine benchmarks at 256594 pystones/second
  ```

* Intel Core i7 2600 @ 3.40GHz:

  ```python
Pystone(1.2) time for 50000 passes = 0.315069
This machine benchmarks at 158695 pystones/second
  ```

* Intel Core i7 7567U @ 3.50GHz:

  ```python
Pystone(1.2) time for 50000 passes = 0.312304
This machine benchmarks at 160100 pystones/second
  ```

Looks like my old desktop is still good for python development.