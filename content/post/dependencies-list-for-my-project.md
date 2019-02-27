---
title: "Dependencies List for My Project"
date: 2019-02-27T23:16:07+02:00
category: [notes]
tags: [pip, npm]
archives: [2019]
author: Ivan Kolodyazhny
---

Time to time you need to get all dependencies for a project you work with.
It’s good if you have an up-to-date list in the requirements.txt file. In
another case, you can always use `pip freeze` command in your virtualenv.
It provides a flat list of all installed dependencies. To get the dependencies
tree, it’s I use [pipdeptree](https://pypi.org/project/pipdeptree/) package.
It provides a simple CLI tool to get dependencies tree with version constraints
for packages where they are specified.

If you develop some library, it’s good to know who uses it and which version is
used. E.g. if version 1.0 is not popular enough, maybe it makes sense to fix
only 2.0 and do not backport a fix to 1.x. For this case, I use
[https://libraries.io/pypi/](https://libraries.io/pypi/). It helps you to find
libraries and see who uses them.
E.g.: [https://libraries.io/pypi/Flask/usage](https://libraries.io/pypi/Flask/usage).
Also, this awesome site supports 36 different package managers for different
programming languages.
