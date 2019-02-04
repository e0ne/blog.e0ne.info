---
title: "OpenStack Horizon: integration tests for plugins (part 2, CI)"
date: 2019-02-04T22:30:34+02:00
category: [openstack]
tags: [horizon, plugins, vitrage]
archives: [2019]
author: Ivan Kolodyazhny
---

It’s a small addition to my previous
[post](https://blog.e0ne.info/post/openstack-horizon-integration-tests-for-plugins/).
I don’t like to edit my previous posts. The only exception is when I have to
fix some typos, spelling error, links, etc.

During the previous post, I described how to implement integration tests for
the Horizon plugins, but I didn’t have enough time to implement and verify CI
for it. It’s time to fix this.

We’ve got really awesome CI in the OpenStack. [Zuul](https://www.zuul-ci.org/)
works great for OpenStack needs and allows to configure cross-project jobs.
A big thank you to our Infra team for the help during CI setup.

We’ve got
[horizon-integration-tests](https://github.com/openstack/horizon/blob/0c8de3eb4c2b9bd1828c1e052f4f28e9f4dcd09f/.zuul.yaml#L27-L42)
job for Horizon itself. It means that everything you need is to extend it and
add few config options.

Here is an example from [this patch](https://review.openstack.org/634667/):

```
- job:
    name: vitrage-dashboard-integration-tests
    parent: horizon-integration-tests
    required-projects:
      - name: openstack/horizon
      - name: openstack/vitrage
      - name: openstack/python-vitrageclient
      - name: openstack/vitrage-dashboard
    roles:
      - zuul: openstack-infra/devstack
      - zuul: openstack/horizon
    irrelevant-files:
      - ^.*\.rst$
      - ^doc/.*$
      - ^releasenotes/.*$
    vars:
      devstack_plugins:
        vitrage: https://git.openstack.org/openstack/vitrage
        vitrage-dashboard: https://git.openstack.org/openstack/vitrage-dashboard
      devstack_services:
        horizon: true
      tox_envlist: integration
```

I’ll describe you the most important parts.

`parent: horizon-integration-tests` - you need to make your job as a child of
the existing one, to not duplicate code and playbooks.

`required-projects` - just add your project and client here to the list. It’s
a requirement on how our CI works. It lets Zuul clone repos before Devstack
starts. Cloning repositories during Devstack setup is not allowed.

`roles` - devstack and horizon needed here to be configured explicitly.
I really need to check if everything works without this section.

`devstack_plugins` and `devstack_services` - here you can configure your.
plugins and enable or disable some services from the Devstack default
configuration.
