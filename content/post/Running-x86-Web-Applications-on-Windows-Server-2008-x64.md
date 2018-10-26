---
title: "Запуск 32-х битных веб сайтов на Windows Server 2008 x64"
date: 2009-11-17T15:17:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [x32,x64,iis]
archives: [2009]
aliases:
    - post/Running-x86-Web-Applications-on-Windows-Server-2008-x64.aspx
---


Всё началось с того, что на один из тестовых серверов поставили 64-х битную ОС. Особых проблем это не вызвало, за исключением того, что обна из сборок использует COM -объекты и появилась необходимость её сборки для платформы x86. Вот сдесь уже начали появляться первые подводные камни.

Первым делом я в свойствах проекта поменял свойство Platform Target (посже оказалось что это нужно сделать для всех проектов в solution):

 

[PlatrormTestWeb.zip (10.01 kb)](/file.axd?file=PlatrormTestWeb.zip)

