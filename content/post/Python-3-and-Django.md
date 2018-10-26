---
title: "Python 3.0 и Django"
date: 2009-01-22T11:15:00+03:00
draft: False
category: [Python,Web Development]
tags: []
archives: [2009]
aliases:
    - post/Python-3-and-Django.aspx
---


Новое - не всегда означает хорошее. Я когда-то уже писал про [IT-гонки глазами программиста](/post/IT-d0b3d0bed0bdd0bad0b8-d0b3d0bbd0b0d0b7d0b0d0bcd0b8-d0bfd180d0bed0b3d180d0b0d0bcd0bcd0b8d181d182d0b0.aspx). Основная идея поста - не стоит спешить переходить на новее, если в этом нет крайней необходимости.

Вот и после очередного релиза Python, правильнее сказать после выхода новой версии языка Python 3.0 захотелось сразу опробоватьвсе гого "вкустности". Вот только новая версия не полностью совместима с веткой 2.х. Поэтому возникает вопрос на какой версии начинать новые проекты? Популярный web framework[](http://www.djangoproject.com/)[Django](http://www.djangoproject.com/) все ещё не пожжерживает Python версии 3.0. Вот что пишут их разработчики:

> 		 			**Can I use Django with Python 3.0?**			**Not at the moment. Python 3.0 introduced a number of backwards-incompatible changes to the Python language, and although these changes are generally a good thing for Python’s future, it will be a while before most Python software catches up and is able to run on Python 3.0. For larger Python-based software like Django, the transition is expected to take at least a year or two (since it involves dropping support for older Python releases and so must be done gradually).**			**In the meantime, Python 2.x releases will be supported and provided with bug fixes and security updates by the Python development team, so continuing to use a Python 2.x release during the transition should not present any risk.**			 	

Вот так.  Пока что для веб-разработки прийдётся использовать старую, но провереннуюверсию языка.

