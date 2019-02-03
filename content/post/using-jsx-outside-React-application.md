---
title: "Using JSX outside React application"
date: 2019-02-03T22:17:47+02:00
category: [web development]
tags: [react, reactjs, jsx, npm, npx, babel, webpack]
archives: [2019]
author: Ivan Kolodyazhny
---

I’m not a fan of the [React](https://reactjs.org/) at all. I prefer to use
[VueJS](https://vuejs.org/) wherever it’s possible. But React is really one of
the most popular JavaScript libraries now. There are a lot of people who use it
and like it.

One of the most important parts of React is
[JSX](https://reactjs.org/docs/jsx-in-depth.html) -  “a syntax extension to
JavaScript. It is similar to a template language, but it has full power of
JavaScript”. Honestly, it’s the one reasons why I don’t like React. But if
you’re using React, it’s really painful to not use JSX too.

But you can like both React and JSX. It’s up to you: to use it or not.
You can even use JSX not only with react-based applications. You just need to
install `babel` and `babel-preset-react` and integrate it with webpack. All
details could be found here:
[https://babeljs.io/docs/en/babel-preset-react](https://babeljs.io/docs/en/babel-preset-react).

There is also a way to use it without webpack too:

```
npx babel --watch src --out-dir . --presets react-app/prod
```

Please, be sure that you use
[npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b),
not npm command here.
