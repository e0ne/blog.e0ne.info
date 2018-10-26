---
title: "IronPython и ASP.NET"
date: 2008-10-30T11:10:00+03:00
draft: False
category: [Python]
tags: [iron python,asp.net,asp.net mvc,web development,dlr]
archives: [2008]
aliases:
    - post/IronPython-and-ASPNET-MVC.aspx
---



В предыдущем [посте](/post/Hello-World-with-IronPython.aspx) я рассказал как подружить Visual Studio и IronPython. Сегодня мы напишем первое приложение на ASP.NET на языке IronPython. 



Для начала необходимо скачать [ASP.NET Dynamic Language Support](http://www.codeplex.com/aspnet/Release/ProjectReleases.aspx?ReleaseId=17613), который включает в себя документацию и два примера: ASP.NET MVC IronPython Sample и ASP.NET Webforms IronPython Sample. Webforms sample- это обычный web site проект с такими файлами: 



  <img src="/image.axd?picture=webforms.JPG" alt="" width="357" height="322" /> 



 К сожалению, в текущей версии не поддердивается проект Web Application. 



C ASP.NET MVC Sample всё на много интереснее. Т.к. Python - это динамичский язык и не поддерживает атрибутов, то код контроллеров приходится писать на C#. С model и view всё значитально проще. Можно использовать IronPython, только во view нужно указать Language="IronPython". В остальном создание приложение ничем не отличается от такового на C#. 



Ну и напоследок хочу сказать, что на прошлой неделе вышел [IronPython ](http://www.codeplex.com/IronPython/Release/ProjectReleases.aspx?ReleaseId=17404)[2.0 Release Candidate 1](http://www.codeplex.com/IronPython/Release/ProjectReleases.aspx?ReleaseId=17404). 



Продолжение следует. 


