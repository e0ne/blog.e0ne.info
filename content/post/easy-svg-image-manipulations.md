---
title: "Easy SVG image manipulations"
date: 2019-01-13T17:44:42+02:00
category: [web development]
tags: [svg, webpack]
archives: [2019]
author: Ivan Kolodyazhny
---

If you decided to use SVG images as icons in your UI it becomes extremely important to have these images with different colors. E.g. you need resource status icons for ‘available’ and ‘not available’ states. You can use the same SVG for both of these states but fill it with red or green color depending on the state.

It’s one of the possible use cases which could be covered by [svg-transform-loader](https://github.com/JetBrains/svg-mixer/tree/master/packages/svg-transform-loader) library. It’s really small and useful webpack plugin loader for SVG manipulations. You can fill or stroke your SVG image inside css, scss, less or even JavaScript.

I will not provide you any example how to use it because it has pretty good documentation which I don’t wont to copy.
