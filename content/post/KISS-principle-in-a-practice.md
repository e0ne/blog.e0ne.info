---
title: "KISS Principle in a Practice"
date: 2019-01-21T23:28:31+02:00
category: [software development]
tags: [kiss, software engineering]
archives: [2019]
author: Ivan Kolodyazhny
---
I hope everybody is familiar with [“Keep It Simple, Stupid” (KISS) principle]
(https://en.wikipedia.org/wiki/KISS_principle). If not, it’s a good time to
read about it.

It a software engineering, it means that you need to keep your software as
simple as possible. Your software architecture should do things that are
required **at this moment**. Please, do not do premature optimization just
because you think it’s a good idea. You don’t need tons of patterns implemented
and dozens of layers in your software on early stages.

Of course, you need to think about maintainability and extensibility. Without
them, you’ll just waste your time and re-write everything or almost everything
in the future. But you don’t need to think a lot about features and cases which
could appear in a far future.

In a real case, sometimes it’s better to hardcode some values or logic with a
proper comment in the code than implement a huge amount of logic on all layers
of your application. It’s faster and less complex.

As any software engineering practice, you should follow it only if needed. IMO,
KISS is one of the most un-used practice now.
