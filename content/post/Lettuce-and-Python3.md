---
title: "Lettuce и Python3"
date: 2012-12-03T23:43:00+03:00
draft: False
category: [Python]
tags: [python 3,lettuce,uapycon,github,opensource]
archives: [2012]
aliases:
    - post/Lettuce-and-Python3.aspx
---


 

Решил я для своих маленьких и уютных домашних проектов (pet project'ов) использовать Python 3.3. Казалось бы, ничто не предвещало беды. Ну кроме как отсутстие поддержки Python 3.x у некоторых библиотек. В частности, Lettuce([http://lettuce.it/](http://lettuce.it/)).

Но так, как я уже выбрал не самый простой, на данный момент, путь (да, я про python3), то отступать было не куда, решил портировать Lettuce под Python 3.3. Возможно, свою роль в этом сыграли еще свежие воспоминания о UA Pycon 2012, в частности, доклад Михаила Коробова “Как всем перейти на Python 3.x” ([http://ua.pycon.org/talks/26](http://ua.pycon.org/talks/26)).

Дальше все понеслось и после нескольких часов ковыряния в исходниках Lettuce и его зависимостей, github fork, py2to3, [http://wiki.python.org/moin/PortingPythonToPy3k](http://wiki.python.org/moin/PortingPythonToPy3k), [http://lettuce.it/dev/index.html](http://lettuce.it/dev/index.html), [https://groups.google.com/forum/?fromgroups=#!topic/lettuce-developers/MaOPzOuMQzg](https://groups.google.com/forum/?fromgroups=#!topic/lettuce-developers/MaOPzOuMQzg) и постоянных попытках запустить это все получилась первая рабочая версия:), commit, push, кофе, кофе, печеньки... До беты, конечно, еще писать и писать (фиксить и фиксить), но начало уже есть  и отступать некуда, ибо сзади остались только Python 2.x и большой enterprise.

Ссылки на GitHub repos:

 

- [https://github.com/e0ne/fuzzywuzzy/tree/python3](https://github.com/e0ne/fuzzywuzzy/tree/python3)
- [https://github.com/e0ne/sure/tree/python3](https://github.com/e0ne/sure/tree/python3)
- [https://github.com/e0ne/lettuce/tree/python3](https://github.com/e0ne/lettuce/tree/python3)

 

Продолжение следует...

 

