---
title: "Pros and Cons of Vue.js"
date: 2019-01-02T16:27:02+02:00
category: [web development]
tags: [javascript, vuejs, typescript]
archives: [2019]
author: Ivan Kolodyazhny
---

Since I started to learn Vue.js a few months ago, I realized that it has some benefits I like and some things which I really hate. I’m not an expert in this framework, but I would like to share my thoughts about it.

## Pros:


### Simplicity


It is really easy to integrate it into your existing web application by just adding one more ~20KB-size JavaScript library. It allows you to start using it with an old or legacy web site like you did with jQuery in the past! You don’t need all that npm and Single Page Application (SPA) stuff in your (mostly python or something else) project. If you need to start only with a simple grid or ‘Load more’ button - you’ll do exactly what you need without tons of JavaScript libraries and npm packages nightmare.

### Curve of learning that helps start fast

Good documentation and examples allow everybody to start development fast. You don’t need to read a lot about patterns in this framework, you won’t be feeling bad because you don’t understand why you have to do it in this way. It’s really easy if you created few websites using at least Flask or Django.

### Good number of features are already included

Template engine, vue-router and vuex allow you to implement whatever you need. Two-way binding works out of the box too!


### Good TypeScript support

If you’re afraid of JavaScript - try strong-typed TypeScript. I really like this language for front-end development.


## Cons:

### Debugging


I use Vue Devtools extension for Chrome but I’m still feeling that it’s not good enough. I would like to have a better debugger and/or IDE integration (I use Pycharm, btw). It won’t tell you about problems if something went wrong during template rendering - it’s the biggest issue with this framework. It really sucks.

### Development process

It’s not really an issue if you are not going to contribute to Vue.js. If you don’t like to file bugs to libraries frameworks you’re using, it’s not an issue for you at all. But you should know, that Vue.js development process is pretty closed and it’s not easy to contribute or get the latest news from the Vue team during new version development.

### TypeScript

TypeScript integration with Vue.js is good enough but you’ll be feeling a lack of TypeScript mapping for all dependencies you will use. I think it’s not an issue for Vue.js, it relates to any other framework too.


That’s all I want to say for now. It has own cons and pros but I still like it and I’m going to use it at least for some time more to understand it deeper and maybe find something I like more.
