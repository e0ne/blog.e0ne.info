---
title: "Attach Cinder Volume to the Ironic Instance without Nova"
date: 2016-01-13T21:50:00+03:00
draft: False
category: [Linux,OpenStack]
tags: [openstack,cinder,ironic,devstack,iscsi]
archives: [2016]
aliases:
    - post/Attach-Cinder-Volume-to-the-Ironic-Instance-without-Nova.aspx
---


OpenStack Cinder provides an API to attach/detach volume to Nova instances. This is public, but not documented API which is used only by Nova now.  In scope of “Attach/detach volumes without Nova” [1] blueprint we introduce new python-cinderclient extension to provide attach/detach API not only for Nova called python-brick-cinderclient-ext. Before Mitaka release everybody who want to use Cinder volumes not only with Nova instances have to create hardening scripts based on python-cinderclient and os-brick [3] projects to make it done.

Since Mitaka, Cinder opens attach/detach API for any users. It will allow to:

 

- Attach volume to Ironic instance
- Attach volume to any virtual/baremetal host which is not provisioned by Nova or Ironic

 

It means, Cinder becomes stand-alone project that could be used outside OpenStack cloud with one limitation: Keystone is still required.

For now, python-brick-cinderclient-ext has only ‘get-connector’ API. Attach/detach features are under development and any feedback are welcome to get implemented in the best way. I hope, it will be implemented and documented as well in scope of Mitaka release cycle.

I will show you how it works in current proof-of-concept code [4]. Anybody is welcome to review and test it:).

To demonstrate this feature I will use virtual Devstack environment with Ironic+Cinder. Here is my local.conf [5].

Current limitations are:

 

- Ironic instance must have access to API and storage networks (it works on Devstack with a default configuration
- Users inside instance must have root permissions and be able to install required software

 

Detailed manual how to setup Ironic using Devstack could be found here [6]. Since volumes attach/detach operations require python, open-iscsi, udev and other packages I will use Ubuntu-based image for Ironic instances. You can use Ubuntu cloud image [7] or build your own using ‘disk-image-builder’ tool [8]. I’ve built my Ubuntu image with disk-image-builder:

After it we need to run Ironic instance:

Wait until instance is booted and ready [9]:

Now you can connect to the instance using SSH:

By default, in Devstack both Nova and Ironic instances have access to OpenStack APIs.

To attach volume you need to install required packages inside you instance:

NOTE: if you can't acces Internet inside your instance, try the following command on the DevStack host:

Clone and install the latest python-cinderclient (the latests version from PyPi will also work but you'll need to pass --os-volume-api-version explicit):

Clone the python-brick-cinderclient-ext and apply the patch:

That’s all! Now, you can attach/detach volumes inside your instance. Because it is still PoC implementation you need few additional steps:

The steps above is needed until **python-brick-cinderclient-ext** will use **oslo.rootwrap** or **privsep** libraries.

Verify, that python-brick-cinderclient-ext works well [10] (you need to setup your own credentiala and auth_url):

You should get something this: [11].

Finally, create and attach volume to your Ironic instance:

You should get something like: [12]

Now you can verify that volume is attached via iSCSI protocol [13]:

Detach is also easy:

That’s all! You’ve got attached your Cinder volume to an Ironic instance without Nova! You can do the same steps to attach volumes inside Nova instance or your desktop. It will work too. I will show you a demo with Nova instance and cloud config scrips in the next post.

 

[1] [https://github.com/openstack/cinder-specs/blob/master/specs/mitaka/use-cinder-without-nova.rst](https://github.com/openstack/cinder-specs/blob/master/specs/mitaka/use-cinder-without-nova.rst)<br />[2] [https://github.com/openstack/python-brick-cinderclient-ext](https://github.com/openstack/python-brick-cinderclient-ext)<br />[3] [https://github.com/openstack/os-brick](https://github.com/openstack/os-brick)<br />[4] [https://review.openstack.org/263744](https://review.openstack.org/263744)<br />[5] [https://gist.github.com/e0ne/2579921aba839322decc](https://gist.github.com/e0ne/2579921aba839322decc)<br />[6] [http://docs.openstack.org/developer/ironic/dev/dev-quickstart.html#deploying-ironic-with-devstack](http://docs.openstack.org/developer/ironic/dev/dev-quickstart.html#deploying-ironic-with-devstack)<br />[7] [https://cloud-images.ubuntu.com/](https://cloud-images.ubuntu.com/)<br />[8] [http://docs.openstack.org/developer/ironic/deploy/install-guide.html#image-requirements](http://docs.openstack.org/developer/ironic/deploy/install-guide.html#image-requirements)<br />[9] [http://paste.openstack.org/show/483734/](http://paste.openstack.org/show/483734/)<br />[11] [http://paste.openstack.org/show/483742/](http://paste.openstack.org/show/483742/)<br />[12] [http://paste.openstack.org/show/483743/](http://paste.openstack.org/show/483743/)

- [https://en.wikipedia.org/wiki/ISCSI#Initiator](https://en.wikipedia.org/wiki/ISCSI#Initiator)
- [https://en.wikipedia.org/wiki/SCSI_initiator_and_target](https://en.wikipedia.org/wiki/SCSI_initiator_and_target)
- [http://j-griffith.blogspot.com/2015/07/volume-attach-code-flow-in-cinder.html](http://j-griffith.blogspot.com/2015/07/volume-attach-code-flow-in-cinder.html)
- [http://www.linux.org/threads/iscsi-storage-configuration-using-iscsiadm-command.4241/](http://www.linux.org/threads/iscsi-storage-configuration-using-iscsiadm-command.4241/)

