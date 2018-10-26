---
title: "Избавляемся от ошибки ValueError: unknown locale"
date: 2012-10-08T22:04:00+03:00
draft: False
category: [Python]
tags: [linux,mac os]
archives: [2012]
aliases:
    - post/Fix-ValueError-unknown-locale.aspx
---


Переодически сталкиваюсь с этой проблемой и приходится гуглить. Решил, записать, что бы проще искать.

Собственно, проблема выглядит так:


<p style="padding-left: 30px;">File "/**home/e0ne/src/project/.venv**/ap**p/lib/python2.7/locale.py", line 496, in getdefaultlocale<br />return _parse_localename(localename)<br />File "/home/e0ne/src/project/.venv/app/lib/python2.7/locale.py", line 428, in _parse_localename<br />raise ValueError, 'unknown locale: %s' % localename<br />ValueError: unknown locale: UTF-8**

File "/**home/e0ne/src/project/.venv**/ap**p/lib/python2.7/locale.py", line 496, in getdefaultlocale<br />return _parse_localename(localename)<br />File "/home/e0ne/src/project/.venv/app/lib/python2.7/locale.py", line 428, in _parse_localename<br />raise ValueError, 'unknown locale: %s' % localename<br />ValueError: unknown locale: UTF-8**

Проблема заключается в том, что для текущего сеанса шелла(bash, etc) не настроена системная локаль. Ошибка позникала как под Linux(Ubuntu, RHEL-based), так под Mac OS. Фиксится просто:

Добавляем в ~/.bashrc следующие строки:


<p style="padding-left: 30px;">export LANG="en_US.UTF-8"<br />**export LC_COLLATE="en_US.UTF-8"<br />****export LC_CTYPE="en_US.UTF-8"<br />****export LC_MESSAGES="en_US.UTF-8"<br />****export LC_MONETARY="en_US.UTF-8"<br />****export LC_NUMERIC="en_US.UTF-8"<br />****export LC_TIME="en_US.UTF-8"<br />****export LC_ALL=**

Вместо "en_US" нужно(можно) подставить нужное значение. Таже, можно выполнить эти строки в шелле и это будет работать до конца сеанса.

