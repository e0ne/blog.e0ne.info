---
title: "Google App Engine 1.5.0: backends, Go и другие изменения"
date: 2011-05-10T21:30:00+03:00
draft: False
category: [.NET Framework,Python]
tags: [gae,google app engine,google,python,go]
archives: [2011]
aliases:
    - post/Google-App-Engine-1-5-0-backends-Go-and-other-changes.aspx
---


Сегодня вышел Google App Engine 1.5.0. Кроме большого числа пофикшенных багов, появилось несколько достаточно интересных изменений.

Среди них стоит отметить такие:

 

- Backends - постоянно запущенный инстанс одной из четырех конфигураций, который не связан с запросами (http requests) и может занимать до 1GB памяти. Один из способов применения - генерация отчетов, которая занимает много времени или другие ресурсоемкие задач
- Изменения в Task Queue - поддержка pull-запросов, увеличение лимита на используемую память
- Размер HTTP Request и Response увеличен до 32MB
- High Replication Datastore теперь является хранилищем по умолчанию для новых приложений
- Много изменений, связанных с квотами - некоторые были увеличены, а некоторые, наоборот - уменьшены
- К моему сожалению, Full Text Search еще не закончили :(. 

 

 Отдельным пунктом хочу отметить экспериментальную поддержку языка программирования Go.  Новости об этом языке, в основном, проходили мимо меня и я только иногда слышал упоминания о нем. Теперь же, когда Google добавил пусть и эксперементальную, но все-же поддержку, то многие захотят посмотреть на него более внимательно. Особенно, учитывая то, что он создан для ресурсо(процессоро)-емких задач будет компилироваться в native code.

Ссылки по теме:

 

- SdkReleaseNotes - [http://code.google.com/p/googleappengine/wiki/SdkReleaseNotes](http://code.google.com/p/googleappengine/wiki/SdkReleaseNotes) 
- Google App Engine: a new version and a preview of future plans - [http://googlecode.blogspot.com/2011/05/google-app-engine-new-version-and.html](http://googlecode.blogspot.com/2011/05/google-app-engine-new-version-and.html) 
- The Go programming language is coming to Google App Engine - [http://googlecode.blogspot.com/2011/05/go-programming-language-is-coming-to.html](http://googlecode.blogspot.com/2011/05/go-programming-language-is-coming-to.html) 
- Google App Engine Developer's Guide - [http://code.google.com/appengine/docs/](http://code.google.com/appengine/docs/)

 

 

 P.S. Интересно, насколько будет популярен Go в Украине через полгода-год, по сравнению с Python и Ruby?

