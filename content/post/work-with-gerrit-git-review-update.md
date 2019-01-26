---
title: "Work with Gerrit: git review-update"
date: 2019-01-26T23:12:56+02:00
category: [development environment]
tags: [gerrit, git, code review]
archives: [2019]
author: Ivan Kolodyazhny
---

If you work with [Gerrit](https://www.gerritcodereview.com/) you use its CLI
tool [git review](https://docs.openstack.org/infra/git-review/usage.html).

Working with OpenStack, I use it a lot every day. I need to update the last
patch and send it to the Gerrit very often. That’s why I created one line
script to execute `git commit -a --amend && git review` command.

I put it into the `/usr/local/bin/git-review-update` file with a following
content:

```
 #!/bin/sh

git commit -a --amend && git review
```

Now, I can use `git review-update` command to update the last patch and send it
to Gerrit. It’s a good example of the simplest and fastest solutions which
works for me during the last two years. Of course, I have to read
[Contributing guide](https://docs.openstack.org/infra/git-review/developing.html)
and propose a new command to `git-review` at some point.
