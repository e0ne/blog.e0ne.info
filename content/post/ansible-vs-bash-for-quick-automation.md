---
title: "Ansible vs Bash for Quick Automation"
date: 2019-03-07T23:04:41+02:00
category: [offtopic]
tags: [everything-as-a-code]
archives: [2019]
author: Ivan Kolodyazhny
---

I don’t want to argue on this topic. I really believe that it’s better to use
Ansible if possible even for some ‘home’ automation. But looking on my scripts
for some development automation (setup VMs, clone sources, install some
software) I realized that there's a mix of Ansible playbooks, Bash and Python
scripts.

It becomes to be hard for maintaining from one side, but it works as expected
for me from another side. I didn’t spend a lot of time making a decision on
what to use. I just choose the first and the fastest solution I’d got. It works
pretty well if I have even several dozens independent simple scripts/playbooks
but it’s really hard to get everything working together.

Of course, it’s better to refactor everything to Ansible and get rid of Python
and Bash scripts where it’s possible, so I will not be ashamed to share
everything on GitHub. Also, it will help me to get more experience with
Ansible.
