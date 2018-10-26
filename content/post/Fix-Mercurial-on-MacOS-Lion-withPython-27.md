---
title: "Восстанавливаем работу Mercurial и MacOS Lion + Python 2.7"
date: 2012-03-21T18:55:00+03:00
draft: False
category: []
tags: [python,mercurial,mac os]
archives: [2012]
aliases:
    - post/Fix-Mercurial-on-MacOS-Lion-withPython-27.aspx
---


Уже не помню когда у меня перестал ратотать клиент к mercurial (hg) - после перехода на Python 2.7 или апгрейда дла Lion. Но так, как я им не пользовался, то решил не тратить время на восстановлние работоспособности. Но тут на проекте решили использовать Mercurial в качестве source control. Соответственно пришлось разбираться с hg. Сразу скажу что установка **последней версии** проблему **не** решила.

Шаг 1. Выполняем команду hg и получаем ошибку:

 

**$ hg<br />abort: couldn't find mercurial libraries in [/usr/platlib/Library/Python/2.7/site-packages /usr/local/bin ...**

Тут понятно что клиент написан на Python и при запуске не может импортировать нужные модули.

 

Шаг 2. Смотрим исходники:

Выполняем команду

**$ sudo vim `which hg`**

и практически в самом начале файла (не считая комменатиев - 3-я строка) видем такую строчку:

libdir = '../../platlib/Library/Python/2.7/site-packages/'

Для тех кто знаком с расположением биболиотек, в частности Python'а, в MacOS сразу поймет что путь к Python указан неправильно, соответственно меняем его на:

libdir = '/Library/Python/2.7/site-packages/'

Шаг 3. Пользуемся mercurial:

 

$ **hg<br />Mercurial Distributed SCM<br />...**

 

