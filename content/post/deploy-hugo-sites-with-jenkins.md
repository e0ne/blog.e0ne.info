---
title: "Deploy Hugo Sites With Jenkins"
date: 2019-02-17T20:54:46+02:00
category: [blog]
tags: [hugo, jenkins, static site, development environment, everything-as-a-code, ci]
archives: [2019]
---
I’ll describe how I do my [Hugo](https://gohugo.io/)-based blog updates with
Jenkins, but it’s pretty similar to any other static site generator.

## Pre-requirements
Jenkins installation is out of the scope of this post. Also, you need to have
installed and configured
[Publish Over SSH](https://jenkins.io/doc/pipeline/steps/publish-over-ssh/)
plugin.

Also, I use
[Jenkins Job Builder (JJB)](https://docs.openstack.org/infra/jenkins-job-builder/)
to configure Jenkins jobs from yaml file.

I’ll describe my blog-jobs.yaml config for my blog below.

## Jenkins configuration

### Views

If you have a lot of jobs or just want to group them by project, it makes sense
to create a view:

```
- view:
    name: Blog
    view-type: list
    job-name:
      - build-blog
      - build-blog-theme

```

Since I’ve got own blog theme, I need to track theme changes too.

### SCM
It’s pretty simple here:

```
- scm:
    name: blog-github
    scm:
      - git:
         url: https://github.com/e0ne/blog.e0ne.info.git
         branches:
          - origin/master

- scm:
    name: e0ne-hugo
    scm:
      - git:
         url: https://github.com/e0ne/e0ne-hugo.git
         branches:
          - origin/master
```


### Job templates

Simple template for theme:

```
- job-template:
    name: 'build-blog-theme'
    id: 'build-blog-theme'
    branch: master
    scm:
      - e0ne-hugo
    builders:
      - shell: |
         hugo version

    publishers:
      - trigger:
          project: build-blog
```

Do not forget to trigger blog update job here.


Build a blog from sources:

```
- job-template:
    disabled_var:
    test_var: Hello World
    name: 'build-blog'
    id: 'build-blog'
    disabled: '{obj:disabled_var}'
    branch: master
    scm:
      - blog-github
    builders:
      - shell: |
         git clone http://github.com/e0ne/e0ne-hugo.git themes/e0ne-hugo
         hugo
    triggers:
      - pollscm:
          cron: "@hourly"
    publishers:
      - ssh:
          site: 'blog.e0ne.info'
          target: 'html'
          clean-remote: true
          source: 'public/**/*.*'
          timeout: 1800000
          use-pty: true
          always-publish-from-master: true
          fail-on-error: true
          verbose: true

```

### Jobs definition

Jobs templates step is optional for such a simple project, but I prefer to keep
with consistency with others. Now I need to define jobs and run JBB to update
my Jenkins configuration.

```
- project:
    name: blog
    jobs:
        - 'build-blog':
        - 'build-blog-theme':
```

That’s all:). I hope it will be useful for sombody.
