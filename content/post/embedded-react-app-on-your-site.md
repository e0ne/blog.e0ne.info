---
title: "Embedded React App on Your Site"
date: 2019-02-19T23:08:08+02:00
category: [web development]
tags: [react, webpack, javascript]
archives: [2019]
author: Ivan Kolodyazhny
---

It’s great if you’re able to start development from scratch and you can
implement SPA using the latest technologies. But sometimes you can only extend
existing functionality. In such a case, it makes sense to embed your React app
into the existing web site.

The idea is pretty simple: you need to add your react-based application to the
existing page.

The easiest way is to add some `<div id="reactApp"></div>` to your page and add
the script with a production build of your react application.
E.g.: `<script src=”main.3d23bdc2.js”></script>`

`main.3d23bdc2.js` - is built by executing something like `npm run build`
command. I don’t like such auto-generated file names because It’s hard to
understand what actually this file does. Of course, webpack generates such
names to resolve issues with caching and new version deployment but I don’t
need it in my specific case.

It’s possible to create some bash script to rename it, but I prefer to use
webpack config for it:

```
output: {
     filename: `${commonPaths.jsFolder}/plugin.js`,
     path: commonPaths.outputPath,
     chunkFilename: 'plugin.js',
   },
plugins: [
     new MiniCssExtractPlugin({
       filename: `${commonPaths.cssFolder}/plugin.css`,
       chunkFilename: 'plugin.css',
     }),
   ],
```

With such config webpack will generate for you two files `plugin.js` and
`plugin.css` in a production build. It becomes more manageable now.

As a next step, I don’t want to include third-party dependencies for my
production bundle. It’s a requirement for the current project, so I need to
specify all scripts like I did ten years ago:

```
    <script src="https://unpkg.com/react@16.7.0/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@16.7.0/umd/react-dom.development.js"></script>
    <script src="/static/custom/plugin/plugin.js"></script>
```

To get this working, I need to change my webpack configuration to not include
React code into the production bundle:


```
   externals: {
       'react':'React',
       'react-dom':'ReactDOM',
   },
```
