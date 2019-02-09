---
title: "I don't believe performance tests results"
date: 2019-02-09T21:55:21+02:00
archives: "2019"
category: [testing]
tags: [performance]
author: Ivan Kolodyazhny
---

Performance testing is one of the most complex and hard types of testing. It’s
really hard to make fair tests which fit everyone. There are a lot of things
which can impact the measurement result. That’s why I don’t believe any
particular test result which I found on the Internet.

If you are a software or hardware vendor, it’s a big temptation to test only
your strengths. Even if you want to get fair results, you can miss something
during the testing or don’t have enough results to see a performance impact.
If you test your application with only one core/process but it’ll have two
cores/processes on a production environment your tests could not show
application performance on production.

Web servers performance could not be measured in general. E.g.: what will
affect Apache2 vs Nginx performance results? There are a lot of things could
affect performance like: static or dynamic content, what app server do you use
(mod_wsgi or uwsgi), what does your app do (e.g. I don’t care on Wordpress
performance results if I develop some custom apps with Django).

That’s why I believe that everybody should do own performance testing for their
apps in a production-like environment. Any existing tests results found on the
web should not be treated as 100% of the truth.
