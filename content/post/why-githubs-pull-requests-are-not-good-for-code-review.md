---
title: "Why GitHub's pull requests are not good for code review"
date: 2019-03-12T22:48:09+02:00
category: [offtopic]
tags: [code review]
archives: [2019]
author: Ivan Kolodyazhny
---

I hope many of you at lease once created or received pull requests in GitHub.
Usually, before pull request is merged some code review process happens. Even
after [the last changes](https://github.com/features/code-review/), code review
functionality in GitHub is not really cool for day to day activities.

I think it’s mostly because of pull requests are not designed for code review.
It just allows you to add a few comments to the code. It was designed to allow
contributors to propose their patches from fork to the original repository.
Usually, in small and maybe in a mid-size project, the code review process is
a pretty quick and not frequent activity.

I liked that we’ve finally got good improvements for Pull Requests UI, but
GitHub is still good only for code sharing. Collaboration features should be
improved.

From another hand, [Gerrit](https://www.gerritcodereview.com/) has a good code
review feature, but it hasn’t good UI for code navigation and search.
