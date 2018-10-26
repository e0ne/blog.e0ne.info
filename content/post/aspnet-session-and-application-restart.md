---
title: "ASP.NET, сэссия и рестарт приложения"
date: 2009-06-09T11:28:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,iis]
archives: [2009]
aliases:
    - post/aspnet-session-and-application-restart.aspx
---



Всё началось с того, что в спецификации к проекту написали примерно такое: "Время продолжительности сэссии пользователя на сайте должно составлять 120 минут". После чего, в web.config была добавлена следующая строка: 


> 
	<p>
	<em><sessionState mode="InProc" cookieless="false" timeout="120" /> 
	</em>
	</p>



А на страницу был добавлен такой мета-тег:


> 
	<p>
	<strong><meta http-equiv="Refresh" content="7200; URL=/EzRc/Pages/LogOn/SessionExpired.aspx" /> 
	</strong>
	</p>



Следует упомянуть конфигурацию  тестовых серверов: Windows Vista/2008, IIS7, .NET 3.5. Ничто не предвещало беды. Но, как и полагается, в один "прекрасный" день всеми людимые QA написали баг следующего содержания: "Session expiration occurs prior to 30 min (and as little as 10 min)." При этом повторить его было достаточно просто:


	- залогиниться на сайт
	- оставить браузер в покое на 30 минут


После этих нетрудный манипуляций при попытке перейти по любой ссылке мы оказывались на странице, в которой радостно говорилось об окончании сэссии и предлагалось перейти на страницу логина. Естественно, этот баг повторялся не всегда.<br />
<br />
Ещё раз убедившись в правильности настроек сэссии в web.config я реши воспроизвести этот баг на локальном (dev) компьютере. Как ни странно, но баг воспроизводился в 100% случаев. "Странно" - подумал я и налил ещё чашку кофе.



Запустив Fiddler2 и залогинившись на сайт я снова оставил его в покое на 30 минут. Через это время, убедившись, что cookie приходят валидные, я наал смотреть логи. Напервый взгляд всё было хорошо, но присмотревшись внимательно, увидел что отрабатывает событие ApplicationStart. Теперь понятно почему заканчивается сэссия. Осталось разобраться почему перезапускается приложение.



Из логов IIS:


> 
	Event code: 1002 <br />
	Event message: Application is shutting down. Reason: Hosting environment is shutting down. <br />
	Event time: 6/8/2009 1:50:21 PM <br />
	Event time (UTC): 6/8/2009 10:50:21 AM <br />
	Event ID: 80d0faffb34547fea6299cfff8cf1c6f <br />
	Event sequence: 4 <br />
	Event occurrence: 1 <br />
	Event detail code: 50002 <br />
	 <br />
	Application information: <br />
	    Application domain: /LM/W3SVC/1/ROOT/Web-1-128889305624881519 <br />
	    Trust level: Full <br />
	    Application Virtual Path: /EzRc <br />
	    Application Path: C:\Src\Sites\Web\ <br />
	    Machine name: localdev <br />
	 <br />
	Process information: <br />
	    Process ID: 6364 <br />
	    Process name: w3wp.exe <br />
	    Account name: NT AUTHORITY\NETWORK SERVICE <br />



 



 



После прочтения статьи из MSDN [ASP.NET Application Life Cycle Overview](http://msdn.microsoft.com/en-us/library/bb470252.aspx) ответ на интересующий вопрос не был получен, из чего был сделан вывод, что проблема находится уровне выше, а именно в IIS. Начал детально изучать настройки, которые могут повлиять на работу приложения и остановился на Application Pools. После чтения документации и нескольких неверных попыток был найден источник проблемы. Им оказался параметр **Idle Time-out**. 



 



<img src="/image.axd?picture=apppool.jpg" alt="" /><br />
<br />
Оказалось, что при настройках по умолчанию, процесс, отвечающий за работу asp.net, тушится при условии, что к нему **не обращаются** в течении 20 минут. Это объясняло, почему проблему можно было не всегда воспроизвести на тестовом сервере. 



Это же можно настроить и через файл machine.config. Подробнее описано [здесь](http://www.xefteri.com/articles/show.cfm?id=14).


