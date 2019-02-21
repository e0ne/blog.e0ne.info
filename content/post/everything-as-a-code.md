---
title: "Everything as a Code"
date: 2019-01-16T22:33:35+02:00
category: [offtopic]
tags: [ansible, development environment, everything-as-a-code, ci]
archives: [2019]
author: Ivan Kolodyazhny
---

Infrastructure as a code… I hear about it during at least last 5-7 years. There are a lot of activities in each company (I hope) to introduce configuration management like Ansible, Puppet, Chef, etc to achieve Continuous Integration and Continuous Deployment(Delivery) aka CI/CD.

I saw a lot of successful implementations for CI/CD for small and mid-size projects. It’s harder to introduce full automation on big projects but it’s absolutely doable.

Infrastructure as a code is a common pattern for CI/CD now. It’s really easy to implement it on GitHub for small projects and individual blogs like this one.

But what about ‘everything as a code’ approach? It’s great to have ansible playbooks that will setup your development environment while you’re drinking your coffee. In such a case, you can configure your favorite editor/IDE, shell, hotkeys, etc in a few minutes on any desktop or server. You don’t need to take your laptop with you. Everything you need is your GitHub repository.

I like the idea to have own CI server for any needs: setup VMs, build Docker images and publish them into the private Docker Registry, setup Kubernetes and run your website there. Of course, this CI server could be automatically configured by Ansible playbook from your GitHub repo. Does anyone have something like it for personal needs? I’ve got plenty of cron jobs, some Ansible playbook to configure some software on my desktop but I’m still far away from everything as a code approach. It will be cool to have something like it.
