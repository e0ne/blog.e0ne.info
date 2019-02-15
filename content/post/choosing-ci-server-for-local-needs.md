---
title: "Choosing CI server for local needs"
date: 2019-02-15T22:23:49+02:00
category: [offtopic]
tags: [ansible, development environment, everything-as-a-code, ci]
archives: [2019]
author: Ivan Kolodyazhny
---

Implementing [everything-as-a-code](https://blog.e0ne.info/post/everything-as-a-code/)
initiative, I need some CI server up and running on my desktop. I don’t want to
use cron directly or implement something myself because of I don’t have enough
time for it.

That’s mean, I can’t use [Drone](https://drone.io/),
[Circle CI](https://circleci.com/pricing/), or [Travis CI](https://travis-ci.org/)
because of pricing. I tried [Buildbot](https://buildbot.net/) and
[GoCD](https://www.gocd.org/) and they look pretty good but not mature enough.

I really like [GitLab CI](https://about.gitlab.com/product/continuous-integration/)
but it requires a lot of resources and looks like too powerful for my simple
tasks. I can say the same about [TeamCity](https://www.jetbrains.com/teamcity/).
It’s one of the best CI servers I ever used.

I didn’t try [Azure DevOps Server](https://visualstudio.microsoft.com/tfs/)
formerly known as TFS. It was a great CI for Microsoft technology stack in the
past. I believe it’s still good but it requires Windows instance.

I don’t want to use [Zuul](https://www.zuul-ci.org/) because it’s designed for
another use cases.

And the last, but not the least item in my list is
[Jenkins](https://jenkins.io/). I don’t like Jenkins for its ugly GUI.
It didn’t change for years. But it doesn’t require a lot of knowledge to do
simple things.
I used [Jenkins Job Builder](https://docs.openstack.org/infra/jenkins-job-builder/)
in the past, so I can store my jobs configuration in a yaml file. I decided to
use this one because I can configure it really fast and it will work. I hope,
I’ll find some time to switch to the TeamCity or GitLab CI in the future.
