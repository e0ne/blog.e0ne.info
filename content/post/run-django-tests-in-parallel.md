---
title: "Run Django Tests in Parallel"
date: 2019-02-24T21:57:35+02:00
category: [web development]
tags: [django, unit tests]
archives: [2019]
author: Ivan Kolodyazhny
---

I’m wondering that in 2019 we still have a lot of tasks which are not
parallelized yet. I’m pretty sure, that almost all laptops, desktops and even
smartphones have more than one core on board.

In the meantime, I just realized that Django runs tests using only one
process/core on my desktop. I’m disappointed but I think I know why it happens.

Many of us are not used to write concurrent code. Speaking about unit tests,
it’s even worse. If you have a old project with a big amount of tests,
I’m pretty sure that some tests could not be executed in a parallel. I’ll be
happy if I’m wrong. But I think it’s only one reason that Django doesn’t
add `--parallel` by default.

I just checked on my project and got such results:

* Ran 1503 tests in 175.383s - in a default configuration
* Ran 1503 tests in 50.671s - with `--parallel` flag

It’s really good performance impact which could be added to the project
without any additional costs. Unfortunately, sometimes you have to spend some
time to get tests working in a parallel.

To enable parallel tests execution in Django you need to add `--parallel`
option to you test command. E.g.: `python manage.py test -- parallel`

The default number of parallel processes equals to
` multiprocessing.cpu_count()`. You can change it via the `--parallel=4`
parameter or `DJANGO_TEST_PROCESSES` environment variable.

More details could be found in the official documentation
[here](https://docs.djangoproject.com/en/2.2/ref/django-admin/#cmdoption-test-parallel).