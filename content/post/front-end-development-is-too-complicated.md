---
title: "Front End Development Is Too Complicated"
date: 2019-01-14T23:13:55+02:00
archives: "2019"
category: [offtopic]
tags: []
archives: [2019]
author: Ivan Kolodyazhny
---



It becomes more and more complicated. Single Page Applications (SPA) are a great thing. I’m pretty sure that all users like it. I don’t know if many developers like it or not. Personally, I think that its development is too complicated.

Maybe it’s not so complicated as I think if you are Front-end Engineer or even full-stack JavaScript Developer. But it becomes extremely hard if you need to integrate your SPA with Python-based API with is working behind Nginx in Docker or Kubernetes. In such case, you have to be able to configure all this stuff. Of course, you may say that there are special guys in your team called DevOps or Deployment Engineers to do all configurations in a correct way but it doesn’t allow you to not understand how it works.

It’s not bad. It’s not good. It’s how things are going forward. If you grow your skills only in front-end, back-end or sysops area nothing will change. You need to be an expert only in your subject area. But if you want to be a [T-shaped person](https://en.wikipedia.org/wiki/T-shaped_skills) you have to know about all of these tools:

Webpack to configure your front-end builds and dev area.
uwsgi/gunicorn/etc to run your API
Nginx to make everything work together
Docker/K8S to deploy your application into containers (OK, you may not use Nginx in this case)

I do not say anything specific about JavaScript, Python, deployment tools and so on. I just mentioned all areas you should know to become a full-stack engineer.

I would like to have some unified environment configuration to run my projects with front-end, API, DB, key-value storage, etc in some unified way. Maybe it will be some yaml, maybe not. I just do not want to have dozens of config with different formats in one project.


P.S. I just tired a bit configuring nginx, webpack and getting everything work with docker-compose today.
