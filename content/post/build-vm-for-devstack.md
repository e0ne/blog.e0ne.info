---
title: "Build VM for Devstack"
date: 2019-02-06T18:25:33+02:00
archives: "2019"
tags: [everything-as-a-code]
author: Ivan Kolodyazhny
---

I posted already about
[diskimage-builder](https://blog.e0ne.info/post/diskimage-builder-in-docker/)
and Docker integration. This is a follow-up post about it and
[Everything-as-a-code](https://blog.e0ne.info/post/everything-as-a-code/)
approach. Since it takes more time than expected (honestly, I didn’t to any
estimations but it seems that it could be done faster), I’ll post you some tips
I use for my development environment automation even if it’s not
`a production-ready solution`, but it already could be used if somebody needs
it.

Almost any work with upstream OpenStack starts with VM setup with
[Devstack](https://github.com/openstack-dev/devstack) and required
configuration. That’s mean even small automation of routine tasks will make me
a bit more happy:).

First of all, I created a few really simple
[diskimage-builder elements](shttps://docs.openstack.org/diskimage-builder/latest/developer/developing_elements.html)
to clone Devstack and configure VM hostname:

```
elements/
├── devstack
│   └── install.d
│       └── 10-clone-devstack
└── hostname
    └── install.d
        └── 10-set-hostname

```

I don’t know if there is a better solution, but it’s good enough for me now.

NOTE: don’t forget to add executable flag `chmod +x 10-clone-devstack`
to get this working.

‘hostname element’ contains one, hardcoded for now, line:
`echo dsvm00 > /etc/hostname`. It’s better to pass environment variable with
hostname and I’ll do it in the next version.

‘devstack element’ just clones devstack sources:

```
mkdir -p /opt/stack
git clone https://github.com/openstack-dev/devstack /opt/stack/devstack
```

That’s all. Now I’m ready to build VM image:

```
DIB_DEV_USER_PWDLESS_SUDO=yes DIB_DEV_USER_USERNAME=e0ne \
DIB_LOCAL_CONFIG_USERNAME=e0ne ELEMENTS_PATH=./elements/ DIB_RELEASE=xenial \
disk-image-create -o ubuntu \
vm ubuntu openssh-server local-config devuser hostname devstack
```

I’m using ‘ubuntu’ instead of ‘ubuntu-minimal’ for more comfort. Once the
image is built, I can start a new VM based on it:

```
sudo virt-install -n dsvm00 -r 8192 --os-type=linux  \
--os-variant=ubuntu16.04 --disk ubuntu.qcow2,device=disk,bus=virtio -w \
bridge=virbr0,model=virtio --vnc --noautoconsole --import
```

NOTE: do not forget to `sudo apt install virtinst` to get the command above
working.
