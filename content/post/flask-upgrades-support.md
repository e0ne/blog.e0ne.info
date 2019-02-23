---
title: "Flask Upgrades Support"
date: 2019-02-23T19:00:30+02:00
category: [web development]
tags: [flask, django, upgrades]
archives: [2019]
author: Ivan Kolodyazhny
---

Upgrading flask-based project from flask v.0.12.x to 1.0.x I realized that
Flask itself doesn’t ready for upgrades yet.

There is no documentation about 0.x -> 1.0 upgrade at all. There is
[some documentation](http://flask.pocoo.org/docs/1.0/upgrading/) about
upgrades prior 1.0 but nothing about 1.0 at all!
[Change log](http://flask.pocoo.org/docs/1.0/changelog/) isn’t helpful a lot.

It’s one more argument to use Django instead of Flask. It has great
[release notes](https://docs.djangoproject.com/en/2.1/releases/2.0/)
with detailed [backward incompatible](https://docs.djangoproject.com/en/2.1/releases/2.0/#backwards-incompatible-changes-in-2-0)
and [deprecation](https://docs.djangoproject.com/en/2.1/releases/2.0/#features-deprecated-in-2-0) sections.
