---
title: "webpack: devserver proxy configuration"
date: 2019-03-09T22:10:24+02:00
category: [web development]
tags: [webpack, proxy]
archives: [2019]
author: Ivan Kolodyazhny
---

[Webpack’s devserver](https://github.com/webpack/webpack-dev-server) is a very
helpful tool. It helps a lot by setting web server for application during
development.

Usually, you need to communicate with your API (backend) from the client-side
via some URL. To avoid cross-site scripting and
[CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) configuration on
your backend or web server(I hope, it’s Nginx:)), you can use a built-in proxy
server in the webpack devserver.

You use it you need just to update webpack config or `vue.conf.js` if you use
`vue-cli` with such options:

```
devServer: {
    proxy: {
      '/api': 'http://localhost:5000'
    }
  }
```

It will redirect all requests from `/api` to `'http://localhost:5000`.

[devserver-proxy](https://webpack.js.org/configuration/dev-server/#devserver-proxy)
could do some simple URL rewrite, ignore SSL certificate validation (it’s a
useful feature for development and self-signed certificates), etc.

It’s really easy to configure. And, of course, this solution is simpler than to
have Nginx to proxy your requests to back-end in the development environment.
