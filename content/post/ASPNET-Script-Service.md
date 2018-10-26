---
title: "ASPNET: Script Service"
date: 2009-12-03T23:05:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,web service,java script]
archives: [2009]
aliases:
    - post/ASPNET-Script-Service.aspx
---


Почему-то, всегда забываю синтаксис вызова script service/method. Руки так и тянуться написать:

И каждый раз, после написания такого когда приходится лезть в MSDN/Google чтобы понять почему же оно не работает. После прочтения документации становится понятно "как" нужно писать вызов метода, но вопрос "почему" ответ, как правило, находится не сразу. Чтобы понять почему же всё работает именно так, достаточно посмотреть JavaScript код, который генерируется службой. Посмотреть это можно зайдя по адресу http://localhost:65456/AsmxService.asmx/js и сохранив себе js-файл следующего содержания:

С WFC AJAX-enabled службами всё работает также.

 

[ScriptServiceExample.rar (7.44 kb)](/file.axd?file=2009%2f12%2fScriptServiceExample.rar)

