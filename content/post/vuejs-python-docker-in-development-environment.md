---
title: "Vue.js + Python API + Docker in Development Environment"
date: 2019-01-08T23:18:15+02:00
category: [web development]
tags: [python, vue.js, docker, nginx]
archives: [2019]
author: Ivan Kolodyazhny
---

## NOTE:

All things described in this post could be not 100% correct. I just described my development environment for a simple project with JavaScript fronted and Python backend. Everything located in the same repository to make example less complicated but it also could work well for small projects and/or when backend and frontend are implemented by the same team. Any contributions are welcome!

## Intro

It’s a story about how I tried to create a simple development environment for web project with Python-based backend and frontend written on Vue.js with typescript. Also, there are containers with database and web server.

Why do I need all of these things? The goal is to have a production-like setup which cares about developers needs too. All of these containers are supposed to be started in the following order: database => API => UI => nginx. Let’s describe them one by one.

## Database

A MySQL-based container with pre-defined credentials and database. Personally, I prefer PostgreSQL but I had to use MySQL for the project:(. You can easily use it by including [official Docker image](https://docs.docker.com/engine/examples/postgresql_service/) or build own using [this manual](https://docs.docker.com/engine/examples/postgresql_service/).


## API

You can have any backend here. I use dummy Flask app just for example. That’s why I didn’t provide a better example with database usage. I didn’t want to introduce Flask or Django here. But I’m too lazy to create an empty application, so I wrote 6 lines of code to get Flask app which returns ‘OK’ every time.

## UI

I like [Vue.js](https://vuejs.org/) and [TypeScript](https://www.typescriptlang.org/). I used [vue-cli](https://cli.vuejs.org/) to create a project template. It serves development server on the localhost (127.0.0.1) by default, so I’ve added `vue.config.js` to configure devserver to run at 0.0.0.0.

## Nginx

A piece of production-like environment where both UI and API are located on the same host. It works like a simple proxy between the browser (or any other client) on the one side and UI/API on the other.

## tox environments

Nothing special is here. There are pretty common pep8, py36 environments. I use [nodeenv](https://pypi.org/project/nodeenv/) to create virtualenv with Node.js to run front end checks.

## Docker

I mostly use Docker like virtual environments so these images are not good for production usage but I feel good to use them for development purposes. That’s why:

* my `Dockerfile`s are as simple as possible - I don’t care about any kind of optimizations
* I install development libraries in containers - it allows to get everything up and running faster
* I install vue-cli and all dependencies in the bootstrap script but not in the single Docker image layer
* my containers are mutable - it allows to modify sources on your laptop or desktop and all changes will be applied to containers on the fly. It’s great for development to have code auto reload but please, DON’T DO THIS for production.


There is [wait-for-it](https://github.com/vishnubob/wait-for-it) script to check if containers are started.


All sourses are availeble at GitHub: [docker-vuejs-python-nginx](https://github.com/e0ne/docker-vuejs-python-nginx)


Kudos to [Pavlo](https://github.com/pshchelo) for fixes to `docker-compose.yaml` and [Vlad](https://github.com/vladiskuz) for enabling `wait-for-it.sh` and `nodeenv`. You helped me make these containers better.
