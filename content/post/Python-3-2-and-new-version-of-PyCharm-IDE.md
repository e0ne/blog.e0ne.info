---
title: "[Updated] Python 3.2 и новая версия PyCharm IDE"
date: 2011-02-22T10:15:00+03:00
draft: False
category: [Python]
tags: [python,pycharm,news]
archives: [2011]
aliases:
    - post/Python-3-2-and-new-version-of-PyCharm-IDE.aspx
---


Буквально на днях вышло сразу два интеречных релиза: [Python 3.2](http://python.org/download/releases/3.2/) и [PyCharm 1.2 EAP Build 105.13](http://blogs.jetbrains.com/pycharm/).

Так как сейчас в новых версиях Python изменений в синтаксисе нет (сделано это для ускорения перехода с ветки 2.x на 3.x), то все изменения сводятся к более стабильной работе, фиксам багов и всяким маленьким и не очень плюшкам.

На фоне этого релиза новая версия PyCharm кроме некоторых небольших улучшений/изменений несет в себе одну достаточно важную функцию под названием "Python version compatibility inspection".

 

<img src="/image.axd?picture=2011%2f2%2fpythonCompatibility.png" alt="" />

Идея этой фичи очень простая: при написании кода среда разработки (IDE) будет вам подсказывать, что данный код будет или не будет работать на разных версиях интерпритатора Python. На мой взгляд, эта функция будет очень полезна тем, кто пишет под Google App Engine или если на машине разработчика версия Python отличается от версии на других environment'ах (окружениях) и по каким-то, надеюсь объективным причинам, не используется [virtualenv](http://blog.e0ne.info/post/Python-and-virtualenv.aspx).

[Update] Хороший комментарий по этой фичи PyCharm дал мне в твиттере Dmitry Jemerov ([@intelliyole](http://twitter.com/#!/intelliyole))

 

<img src="/image.axd?picture=2011%2f2%2fcomment.jpg" alt="" />

