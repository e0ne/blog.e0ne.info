---
title: "Some usefeul JavaScript articles (if you didn't use Javascript suring the last 5 years)"
date: 2019-02-11T21:59:17+02:00
category: [web development]
archives: "2019"
tags: [javascript]
author: Ivan Kolodyazhny
---
If you like me didn’t write any lines of code in JavaScript during the last 5
years, you will be surprised how it changed.

I won’t re-write all existing blog posts and manuals because of two reasons:
I’m too lazy for these things and I’m not feeling that I can do it better.

I’ll leave the references for two topics I’ve found useful for me: variables
declarations and modules. I like [MDN](https://developer.mozilla.org/en-US/),
so I’ll use it for references.

## Variables declaration

You don’t need [var](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
anymore. OK, you still need if for some cases, but
[let](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
is great for local variables with a limited scope and [const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const)
works well if you need a variable which can’t be re-assigned. The value of such
a variable could be changed like any mutable variable.

## Modules

Finally, we’ve got modules in JavaScript. There are still some limitations in
a few browsers and some specs are not approved yet, but with
[babel](https://babeljs.io/) you can use it right now. You can
[import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
from modules when you need to do it and use
[export](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export)
statement to provide a public interface for your modules.
