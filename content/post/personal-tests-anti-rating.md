---
title: "Personal Tests Anti Rating"
date: 2019-01-20T22:21:46+02:00
category: [offtopic]
tags: [tests, ci]
archives: [2019]
author: Ivan Kolodyazhny
---

Here is my personal test anti-rating. If I see something from this list, for me
it means that the testing process on this project is not ideal.

### 5. You can’t run tests on your development environment

It depends on a project ad kind of tests, but you should be able to run unit
tests at least on your development environment. Otherwise, you’ll waste your
time and CI resources waiting for tests results

### 4. A lot of skipped tests

If there are a lot of skipped tests, it means that nobody cares about testing
and/or tests are not stable.

### 3. A lot of non-voting jobs on CI

It’s almost like #4. The main point of this item is that  CI is not effective
enough. There are a lot of tests which nobody cares about.

### 2. There are no tests at all (for a project, feature, module, etc)

It’s simple. It means that your project/feature will be broken for sure. Sooner
or later it’ll be broken.

### 1. You don’t run tests on CI per each commit

Fast feedback is one of the required parts of CI. Without per commit tests run,
you CI is just a UI for tests runner or deployment tool. You don’t have CI if
there are no per-commit tests on it.
