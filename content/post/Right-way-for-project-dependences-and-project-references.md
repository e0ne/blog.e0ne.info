---
title: "Project dependences и project references: делаем это правильно"
date: 2009-07-23T15:00:00+03:00
draft: False
category: [.NET Framework]
tags: []
archives: [2009]
aliases:
    - post/Right-way-for-project-dependences-and-project-references.aspx
---


Раньше всегда это делал настолько автоматически, что даже и не задумывался что это млжно делать по-другому. Но когда столкнулся с такой проблемой в текущем проекте - решил написать.

 Рассмотрим такую ситуацию: у нас есть главная сборка (Main), сборка с утилитными классами (Utils) и 3-rd party логгер (Logger):

 
																																	1. Добавляем в наш solution нужные нам проекты.																	1. Добавляем ссылки на проекты.
[ReferencesSample.zip (76.14 kb)](/file.axd?file=ReferencesSample.zip)

