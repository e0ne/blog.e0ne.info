---
title: "Default Config Options"
date: 2019-01-28T18:21:28+02:00
archives: "2019"
tags: []
author: John SMITH
---

Once your project becomes a bit bigger than ‘Hello, World’, you need to add an
ability to configure it. It could be config in the code like in Django or
Flask, pass environment variables, CLI arguments or a special config file
located somewhere in the filesystem.

At this point, everyone should ask themselves this question: What should I
consider as a default option? Should it be production-like or developers
friendly options?

The first rule is: you should be able to run your application with default
config. You can use SQLite as a database, maybe some features should not work
properly but the application must be able to start.

What does it mean? E.g.: if an application requires RabbitMQ for RPC, it should
startup but raise an exception with a proper message like ‘Can not connect to
the RabbitMQ host: localhost, port: 5672’ so you’ll be able to understand what
is going and how to fix it. Another option is to raise an exception like
'RabbitMQ connection is not configured. Please specify "rabbitmq_host" config
option'. Sometimes you even can start an application without some third party
requirements like a database, message broker or something like it. But any such
issues should be logged. Errors like “Can’t startup with invalid config” are
not useful at all.

Another important thing is to decide what is defaults: development or the
production-like environment. As a software engineer, I prefer to have
development-friendly defaults. But if you don’t have good configuration
management, it’s harder to have production config tested.

I think, on CI you should have production-like configurations in your configs.
It helps you to prevent many issues in the future.

If you can have a production-like config for your development needs, it’s
awesome. It leads to some more testing even during development. Also, if you
keep your development environment closer to a production one, you’ll have fewer
errors in the future.

It’s a hard choice. I don’t have a strong opinion on it. I just try to keep my
configs as close to production as possible and do not make development
as a nightmare.
