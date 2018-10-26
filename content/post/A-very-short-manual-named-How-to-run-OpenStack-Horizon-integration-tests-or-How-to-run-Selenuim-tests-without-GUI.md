---
title: "A very short manual named How to run OpenStack Horizon integration tests or How to run Selenuim tests without GUI"
date: 2015-09-03T23:36:00+03:00
draft: False
category: [Linux,Web Development]
tags: [openstack,horizon,firefox,selenium,headless,xvfb]
archives: [2015]
aliases:
    - post/A-very-short-manual-named-How-to-run-OpenStack-Horizon-integration-tests-or-How-to-run-Selenuim-tests-without-GUI.aspx
---


Didn't google "how to run horizon integration tests" unswer in 10 seconds. Making note how to do it.

My development environment usually looks like: macbook + VM with Ubuntu Server or CentOS without GUI. I try to run all tests inside VMs. In case of Selenium tests, I need some preparation for it:

1. **$ sudo apt-get install firefox<br />**this command will install FireFox. Selenium has WebDriver for it out of the box
1. **$ sudo apt-get install xvfb<br />**install Virtual Frame Buffer for X Server ([https://en.wikipedia.org/wiki/Xvfb](https://en.wikipedia.org/wiki/Xvfb))
<li>Run tests:  
<ul>
1. Simple way for OpenStack Horizon:<br />./run_tests.sh --integration --selenium-headless
<li>Hard way for any project:<br /> 
<ul>
1. Start xvfb:<br />**$ sudo Xvfb :10 -ac** 
1. Start headless FireFox:<br />DISPLAY=:10 firefox
1. run tests
</ul>
</li>
</ul>
</li>

- [http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/](http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/)
- [http://docs.openstack.org/developer/horizon/ref/run_tests.html#i-just-want-to-run-the-tests](http://docs.openstack.org/developer/horizon/ref/run_tests.html#i-just-want-to-run-the-tests)

