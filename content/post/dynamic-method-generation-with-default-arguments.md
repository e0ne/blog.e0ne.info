---
title: "Dynamic method generation with default arguments"
date: 2019-03-01T23:00:38+02:00
category: [python]
tags: [horizon]
archives: [2019]
author: Ivan Kolodyazhny
---

NOTE: please, be sure that you really need such things in your project. It
could be useful if you understand how it works. You can also spend hours or
even days to understand what is going wrong if you don’t understand how method
generation works in the project.

NOTE: this post is based on
[OpenStack Horizon](https://governance.openstack.org/tc/reference/projects/horizon.html)
[integration tests](https://github.com/openstack/horizon/tree/master/openstack_dashboard/test/integration_tests).

We use method generation in our tests framework to generate methods like
‘go_to_some_page’. It’s pretty useful because we don’t need to implement such
methods manually for each page.

The issue is that we need to generate methods with some default arguments. We
used [unbound methods](https://six.readthedocs.io/#six.create_unbound_method)
for Python 2.7. Unfortunately, it doesn’t work at all in our case for
Python 3.5+. What we need is something like: dynamically generated methods with
some default arguments.

TBH, I’m pretty sure that it could be refactored to have less complex and
cleaner code, so I’ll be happy to review such patches if somebody wants to do it.

There is a new function
[functools.partialmethod](https://docs.python.org/3/library/functools.html#functools.partialmethod)
in Python 3.4 with is pretty similar to
[functools.partial](https://docs.python.org/3/library/functools.html#functools.partial),
but leave `self` as a first element, so it could be used for class methods:

```
def _go_to_page(self, path):
   return Navigation._go_to_page(self, path)

wrapped_go_to = functools.partialmethod(_go_to_page, ‘/about’)
setattr(Navigation, ‘go_to_about_page’, wrapped_go_to)
```

The code above adds `‘go_to_about_page` method to class `Navigation` which will
receive ‘/about` value of `path` argument each time this method will be called.


I’m glad that this code is cleaner than we’ve got for Python 2.7:

```
class GoToMethodFactory(object):
   def __init__(self, path):
       self.path = path
       self.name = self._create_name()

   def __call__(self, *args, **kwargs):
       return Navigation._go_to_page(args[0], self.path)

go_to_method = Navigation.GoToMethodFactory(‘/about’’)
inst_method = six.create_unbound_method(go_to_method, Navigation)
setattr(Navigation, inst_method.name, inst_method)

```

In both cases, the definition of the `Navigation._go_to_page` is the same:

```
def _go_to_page(self, path):
    …
```

It means, we need to path `self` param everywhere (it’s easy because we use
code like: `page.go_to_about_page()`) and pass `path` param. That’s why we need
to store `path` somewhere. For Python 2.7 we used a simple class for it. For
Python 3.5+ we use `partialmethod` now.
