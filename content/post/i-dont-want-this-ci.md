---
title: "I don't want this CI"
date: 2019-03-13T22:36:17+02:00
category: [offtopic]
tags: [ci]
archives: [2019]
author: Ivan Kolodyazhny
---
I love CI and I’m sure that it’s a required part of the software development.
It helps a lot to test software to find issues as soon, as possible. CI save
thousands of person-hours by automatically project testing. It works almost in
the background and guides you to the next steps: go forward or step back and
fix the issue.

Everything is written above is valid only for good CI. It should not be too
noisy. It tesh every change in a automatic way. It’s stupid if you need to run
some tests on “CI” manually. It’s not CI. A lot of false-positive jobs makes CI
annoying. If there's a lot of non-voting jobs, it’s not useful at all. You’ll
ignore such jobs in the future if they fail on a regular basis. All tests
results should show you the current status of a project or a patch. If tests
results are not clear, it means that CI or tests should be changed.

Every engineer before setting up the CI should read this book:
[Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation](https://www.amazon.com/Continuous-Delivery-Deployment-Automation-Addison-Wesley/dp/0321601912).

It’s obvious that CI requires a lot of resources for huge projects: both
hardware and human. It’s the price you should pay be successful.
