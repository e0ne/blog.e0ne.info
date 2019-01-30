---
title: "Config Inheritance"
date: 2019-01-30T23:09:38+02:00
category: [software development]
tags: [config]
archives: [2019]
author: Ivan Kolodyazhny
---
Continuing the topic from the
[previos post](https://blog.e0ne.info/post/default-config-options/) about
project configuration, I would like to metion one more important thing. It’s a
config inheritance or config overriding. I don’t want to argue if my approach
is good or not. I just like it and I try to follow it wherever it’s possible.

I will write about possible configuration location in the order where the next
level will override the previous one:

* Default values in the code. It’s a common location for defaults if it’s
possible. Sometimes you can’t have any default value due to the different
reasons.

* Config file in the default. I mean that you often have something like
`/etc/yourapp/yourapp.conf` or a config file in the working directory. Nothing
special here. It’s obvious that config files should override defaults from the
code.

* Additional config file. Sometimes it’s possible to provide several config
files into your application.
E.g.: /usr/local/bin/yourapp --config=/path/to/configA --config=/path/to/configB.
In a such case, values from the configB should override values from the
configA.

* CLI arguments like `/usr/local/bin/yourapp --paramA=1 --param2=2`. Sometimes
it’s extremely useful to have the ability to specify config options in such a
way. E.g. you need to launch the second instance of your application just with
a different database connection string or something like that.

* Environment variable. It’s the most controversial item in this list, I guess.
Somebody like it, somebody doesn’t. The argument against it is simple: it’s not
explicitly passed to the application, so you can pass some wrong value by a
mistake. E.g. some environment variable could be set by default when you’re
logging in into some remote console. But I like it for the following reason:
it’s easy to set an environment variable inside your session to override some
options for each application call during the SSH session. Honestly, I’m not
sure what should have the highest priority: environment variables or CLI
arguments but for a consistency, I decided to have such order.
