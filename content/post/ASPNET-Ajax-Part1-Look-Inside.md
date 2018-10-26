---
title: "ASP.NET Ajax. Часть 1: что внутри?"
date: 2009-04-02T12:00:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [asp.net,ajax]
archives: [2009]
aliases:
    - post/ASPNET-Ajax-Part1-Look-Inside.aspx
---



На днях столкнулся такой ситуацией, что <strike>многие</strike> некоторые разработчики при упоминании Ajax имеют в виду компонент UpdatePanel и не понимают как она работает. Сегодня я решил попытаться исправить эту ситуацию и рассказать что такое и как устроен ASP.NET Ajax.



 Для начала обратимся Википедии и посмотрим, что такое Ajax:


> 
	<p>
	AJAX (Asynchronous Javascript and XML — «асинхронный JavaScript и XML») — это подход к построению интерактивных пользовательских интерфейсов веб-приложений, заключающийся в «фоновом» обмене данными браузера с веб-сервером. В результате при обновлении данных веб-страница не перезагружается полностью, и веб-приложения становятся более быстрыми и удобными.
	</p>



Для выполнения асинхронных запросов, на JavaSctipt необходимо создать объект XMLHttpRequest, который и будет взаимодействовать с сервером. В зависимости от браузера, объект создаётся разными способами, но можно написать универсальный метод для его создания:



 



Теперь вернёмся в ASP.NET. Как несложно догадаться, Microsoft ASP.NET Ajax имееит клиент-серверную архитектуру:
<img src="/image.axd?picture=ms-ajax.jpg" alt="" />



Серверная часть Microsoft ASP.NET Ajax отвечает за авторизацию и аутентификацию пользователей, генерацию и регистрацию на странице необходимых скриптов, имеет всё необходимое для работы с веб-службами, включая генерацию proxy-классов, xml и JavaScript сериализацию. Также доступно несколько компонентов (ScriptManager, UpdatePanel, UpdateProgress и Timer), которых вполне достаточно для реализации базовых функций. 



Клиентская часть имеет название Microsoft AJAX Library и состоит из нескольких JavaScript файлов, с помощью каких взаимодействие с сервером становится проще. В этой библиотеке доступно множество классов, для взаимодействия с веб-службами, работы с DOM-моделью браузера, имебтся базовые классы для создания собственных контролов.



В следующих постах я расскажу подробнее о том, как работает серверная часть и загляну внутрь Microsoft AJAX Library.



Ссылки, где можно почитать подробнее об ASP.NET AJAX:


	- [http://msdn.microsoft.com/en-us/library/bb398874.aspx](http://msdn.microsoft.com/en-us/library/bb398874.aspx)
	- [http://www.asp.net/ajax/documentation/ ](http://www.asp.net/ajax/documentation/)
	- [http://aspnet.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=24645](http://aspnet.codeplex.com/Release/ProjectReleases.aspx?ReleaseId=24645)
	<li>[http://ajaxcontroltoolkit.codeplex.com/](http://ajaxcontroltoolkit.codeplex.com/)<br />
	</li>

