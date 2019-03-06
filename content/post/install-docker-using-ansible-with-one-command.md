---
title: "Install Docker Using Ansible With One Command"
date: 2019-03-06T23:34:39+02:00
category: [development environment]
tags: [everything-as-a-code]
archives: [2019]
author: Ivan Kolodyazhny
---

It’s boring to install Docker and Docker Compose on any host I need. Maybe
Kubernetes is the right weight to di such things but Docker fits all my needs
at the moment, so I use it for some development scenarios.

I’ve got a simple `docker_bootstrap.sh` script to install Ansible if it’s not
installed yet and setup Docker on the same host:

```
#!/bin/bash

pip install ansible
ansible-galaxy install nickjj.docker

ansible-playbook ./site.yml -t docker
```

I use Ansible from pip because it’s not supposed to be installed on
a production environment. If you want to install Ansible using operating system
packages, for Debian-based distros you can do something like:

```
apt-get update
apt-get install --yes software-properties-common
apt-add-repository --yes --update ppa:ansible/ansible
apt-get install --yes ansible
```

And here is a really simple `site.yml`:

```
---

# site.yml

- name: Install Docker
  hosts: "localhost"
  become: true

  roles:
    - role: "nickjj.docker"
      tags: ["docker"]
```

It’s one of the simples solutions and it works for me. I try to not
over-engineering my development environment and keep it as simple, as possible
to do fewer efforts during support it.
