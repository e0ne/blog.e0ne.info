---
title: "Right Way to Setup Jenkins in Docker"
date: 2019-02-21T22:30:11+02:00
category: [offtopic]
tags: [development environment, everything-as-a-code, ci]
archives: [2019]
author: Ivan Kolodyazhny
---

I was for this solution for months. Almost any guide I’ve found was about using
an official [Docker image](https://github.com/jenkinsci/docker) with few
plugins installed. It works pretty well if you agree with a manual initial
configuration like configure admin user and password. It doesn’t work at all if
you deploy Jenkins in an automated way.

Here is a `Dockerfile` to get installed and ready to use Jenkins:

```
FROM jenkins/jenkins:lts

# https://github.com/jenkinsci/docker/blob/master/README.md

# Jenkins configuration
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy

# Jenkins plugins
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

```

`security.groovy` content:

```
#!groovy

import jenkins.model.*
import hudson.security.*
import jenkins.security.s2m.AdminWhitelistRule

def instance = Jenkins.getInstance()

def hudsonRealm = new HudsonPrivateSecurityRealm(false)
hudsonRealm.createAccount("admin", "admin")
//def user = new File("/run/secrets/jenkins-user").text.trim()
//def pass = new File("/run/secrets/jenkins-pass").text.trim()


instance.setSecurityRealm(hudsonRealm)

def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
instance.setAuthorizationStrategy(strategy)
instance.save()

Jenkins.instance.getInjector().getInstance(AdminWhitelistRule.class).setMasterKillSwitch(false)
```

Of course, I don’t use this login/password pair for my instances :).


The original post is
[here](https://technologyconversations.com/2017/06/16/automating-jenkins-docker-setup/comment-page-1/).
I’m coping it to my blog just to not forget about it because I don’t like
notes, favorites in a browser and so on.
