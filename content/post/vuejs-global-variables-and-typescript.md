---
title: "Vue.js, global variables and TypeScript"
date: 2019-01-15T23:07:27+02:00
category: [web development]
tags: [vuejs, webpack, environment variables, typescript]
archives: [2019]
author: Ivan Kolodyazhny
---

It’s pretty easy to pass some environment variable to Vue.js application using [webpack.DefinePlugin](https://webpack.js.org/plugins/define-plugin/). You just need to have something like a sample below in your `webpack.config.js`:

```
var webpack = require('webpack')

module.exports = {
 // ...
 plugins: [
   // ...
   new webpack.DefinePlugin({
     'BUILD': JSON.stringify(0.0.1')
   })
 ]
}
```

It’s a common way to pass some environment variable into your JavaScript application. Technically, `webpack.DefinePlugin` injects a global variable into your JavaScript application. You may need it for some [feature flags](https://github.com/petehunt/webpack-howto#6-feature-flags) or some global configuration.

Do not forget to use `JSON.stringify` because of DefinePlugin inserts raw string and it could lead to some unexpected results.

It works pretty well until you need all these things with TypeScript. First of all, you need to change your `vue.conf.js` to add metiond webpack plugin:

```
configureWebpack: {
    plugins: [
      new webpack.DefinePlugin({
           'BUILD': JSON.stringify(0.0.1')
    }),
    ]
```

After that, you need to define a [global variable](https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html#global-variables) `BUILD` somewhere in your TypeScript code: ```declare var BUILD: string;```. It’s required because TypeScript doesn’t know anything about global JavaScript variables, so you need to declare them.

I did it in the `globals.ts`:
```
declare var BUILD: string;

export default BUILD;
```

So I can use it everywhere in a project: `import BUILD from '@/globals.ts';`.

The same procedure should be followed if you want to access environment variables from your code (actually, webpack will inject variables values into the code, because I don’t have access to them from the browser). In the JavaScript world, you can just use `process.env.BASE_URL` and everything will work. But for TypeScript you have to declare a new global variable:
```declare var process : {
    env: {
        BUILD: string
    }
}```


Nothing unexpected happened, you just need to remember that every variable you can easily use in JavaScript you have to declare in TypeScript. It’s just because TypeScript is a strong-typed programming language. These actions could be obvious you anybody who knows TypeScript well, but it leads to difficulty for newbies.
