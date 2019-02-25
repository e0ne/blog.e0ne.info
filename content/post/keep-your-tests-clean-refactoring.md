---
title: "Keep Your Tests Clean: Refactoring"
date: 2019-02-25T17:35:12+02:00
category: [software development]
tags: [unit tests, refactoring]
archives: [2019]
author: Ivan Kolodyazhny
---

Refactoring tests could be painful a lot. But it could also give you a lot of
fun too. During refactoring unit tests, I’ve found a log of issues to be
resolved. Also, it gives me more knowledge about how the project works.

Refactoring tests could be harder than refactoring rest of code because it
could affect not only tests.

Since there are no tests for tests, there is only one way to understand if
refactoring didn’t lead to less test coverage. It’s required to measure testsc
overage before and after refactoring. New tests coverage should be equal to or
more than the old one.

It’s important to keep code quality for tests too. Tests are the same code as
any other. That means, that you have to follow the same patterns and practices:
code reviews, KISS, DRY, etc. It’s extremely dangerous to not do code review
just because ‘it’s unit tests’.
