---
title: "OpenStack Horizon: integration tests for plugins"
date: 2019-02-01T23:00:05+02:00
category: [openstack]
tags: [horizon, plugins, vitrage]
archives: [2019]
author: Ivan Kolodyazhny
---

Ideally, I need to push this post into the Horizon documentation, but I would
like to publish it here as HOTO for me before everything will be approved and I
move this into the official documentation.

About one week ago we, finally, included integration
[tests job](https://review.openstack.org/#/c/580469/) to our gates in
non-voting mode. A big thanks to everyone who helped to get this done. We’ve
got about 80 integrations tests in the horizon
[repository](https://github.com/openstack/horizon/tree/master/openstack_dashboard/test/integration_tests).
Also, it could be used as a base framework to implement tests for plugins.
Unfortunately, these tests work only with python2 now, but we’re going to fix
it soon.

This is a step-by-step guide on how to implement integration tests for your
Horizon plugin. I’ll take
[vitrage-dashboard](https://github.com/openstack/vitrage-dashboard/) as
an example.

## Step #1: tox.ini
You have to add a tox environment to run new tests. I’m using the same, as
we’ve got in Horizon:

```
[testenv:integration]
# Run integration tests only
passenv = AVCONV_INSTALLED
setenv =
  PYTHONHASHSEED=0
  INTEGRATION_TESTS=1
  SELENIUM_HEADLESS=1
  HORIZON_INTEGRATION_TESTS_CONFIG_FILE=vitrage_dashboard/dashboard/tests/integration/horizon.conf
basepython = python2.7
commands = {envpython} {toxinidir}/manage.py test vitrage_dashboard {posargs}
```

`INTEGRATION_TESTS` and `SELENIUM_HEADLESS` are needed to configure selenium on
your host.

`HORIZON_INTEGRATION_TESTS_CONFIG_FILE` variable should point to your
plugin-specific configuration file which will be described in the next section.
Please,  make sure that you’ve got python2 there :(.

## Step #2: configuration file
We use [oslo.config](https://github.com/openstack/oslo.config) to work with configuration file. A minimal config file looks like:

```
[plugin]
is_plugin=True
plugin_page_path=vitrage_dashboard.dashboard.tests.integration.pages
plugin_page_structure='{"Project": {"Vitrage": {"_": ["Topology", "Alarms"]}}}'
```

All other settings will be used from horizon’s
[config](https://github.com/openstack/horizon/blob/fe6910473860feec4276e699d9adbd1dc08ccfff/openstack_dashboard/test/integration_tests/config.py).
Since Horizon uses
(Page Objects)[https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide#Page_Objects]
pattern in the integration tests, it’s required to implement the same solution
in plugins. That’s why we need to specify a path to Page Objects
implementation.

Also, you need to specify your plugins page structure like we’ve got for
[core pages](https://github.com/openstack/horizon/blob/15574cad5c265256a2c8664516537c01ed2233da/openstack_dashboard/test/integration_tests/pages/navigation.py#L62)
in `plugin_page_structure` param as a JSON string representation.


## Step #3: Page Objects

There is a requirement for Horizon integration tests framework to have Page
Object class for each page. As an any OOP approach, it work’s well for a lot of
code(pages) but looks like a over-engineering for simple tests for few pages.
The structure of these modules should be like:

```
pages/__init__.py
pages/project/__init__.py
pages/project/vitrage/__init__.py
pages/project/vitrage/alarmspage.py
```

It should be located in the module, specified in `plugin_page_path`.

## Step #4: Implement tests

It’s up to you how you implement integration tests. Horizon provides some
useful helpers for navigation, base
[TestCase](https://github.com/openstack/horizon/blob/15574cad5c265256a2c8664516537c01ed2233da/openstack_dashboard/test/integration_tests/helpers.py#L304)
and
[AdminTestCase](https://github.com/openstack/horizon/blob/15574cad5c265256a2c8664516537c01ed2233da/openstack_dashboard/test/integration_tests/helpers.py#L333)
for your tests.

The simplest test I implemented looks like:

```
class TestVitrageDashboardInstalled(helpers.TestCase):
    def test_alarms_page_opened(self):
        alarms_page = self.home_pg.go_to_project_vitrage_alarmspage()
        self.assertEqual(alarms_page.page_title,
                         'Alarms Analysis - OpenStack Dashboard')

```

It just opens the required page and verifies it’s title.

## Step #5: test requirements

You have to add these two libraries to your test-requirements.txt to get
everything working:

```
# integration tests requirements
selenium>=2.50.1 # Apache-2.0
xvfbwrapper>=0.1.3 #license: MIT
```

## Step 6: Enjoy!

You can run your tests now:

```
tox -e integration
```

A sample code could be found here:
[https://review.openstack.org/634487](https://review.openstack.org/634487)
