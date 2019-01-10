---
title: "Some Useful Docker Commands"
date: 2019-01-10T22:11:42+02:00
category: [linux]
tags: [docker]
archives: [2019]
author: Ivan Kolodyazhny
---

Five years ago I wrote the post [Git: some useful commands](https://blog.e0ne.info/post/git-some-useful-commands/) (in Russian).
Probably, it’s a good idea to translate it into English too but it’s a
different story.

I used that post as a handbook for some git commands which I had to use really
rare. Now I would like to create a similar list for Docker. Some of these
commands you can easily find in the manual and help but if you’re such lazy as
me, you would like to get such list noted somewhere.

### List all running containers of docker compose.
Really, I forget about this too often and use `docker ps`. I have to use
`docker-compose ps` for these needs.

### Fast validation of the docker-compose.yaml
It's just `docker-compose config`

### Remove all existing docker containers
A bit of bash is here: `docker rm $(docker ps -a -q)`

### Remove all existing images
It's very similar to the previous one: `docker rmi $(docker images -a -q)`

### Remove all existing non-used volumes:
I use `-f` flag, do not ask for the confirmation
`docker volume prune -f`


### Remove everything
I use `-f` flag, do not ask for the confirmation
`docker system prune -a -f`


### Stop all running containers
Kill 'Em All: `docker kill $(docker ps -q)`


I've got aliases for most of these command in my 'bashrc' file now, so I don't
need to remember any of them now :).