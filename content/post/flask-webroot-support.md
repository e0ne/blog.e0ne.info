---
title: "Flask WEB_ROOT Support"
date: 2019-01-22T21:20:01+02:00
archives: "2019"
category: [web development]
tags: [flask, webroot, web_root]
archives: [2019]
author: Ivan Kolodyazhny
---

Impressed by [OpenStack Horizon](https://github.com/openstack/horizon)
[WEBROOT](https://docs.openstack.org/horizon/latest/configuration/settings.html#webroot)
config option I decided to add the same for my Flask-based project. TBH, I was
sure that it’s an option from Django. It works great and it’s extremely useful.

From the Horizon’s documentation:

**WEBROOT** - Specifies the location where the access to the dashboard is
configured in the web server. For example, if you’re accessing the Dashboard
via **https://<your server>/dashboard**, you would set thisto
**"/dashboard/"**.

It’s not needed by everybody, but sometimes it’s good to have something like
it.

We’ve got [APPLICATION_ROOT](http://flask.pocoo.org/docs/1.0/config/#APPLICATION_ROOT)
in Flask, but this option doesn’t affect application routes. That’s why I’ve
added WEB_ROOT support to my application.

NOTE: I’ll describe you my solution without any reference on project structure
to keep this manual as general, as possible.

First of all, I added WEB_ROOT param to my config and re-defined
APPLICATION_ROOT value:

```
WEB_ROOT = ‘/’
APPLICATION_ROOT = WEB_ROOT
```

The next and the last thing (this manual is really short) you need to pass
WEB_ROOT value to your blueprints as `url_prefix` param.

Depends o how do you register blueprints, this code could be located in some
blueprint factory or just simple a simple code like:

```app.register_blueprint(your_blueprint, url_prefix=app.config['WEB_ROOT'])```

That’s all:). Now you can easily deploy your application to some path like
`https://example.com/your-app`.
