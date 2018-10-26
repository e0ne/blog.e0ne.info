---
title: "Пишем Hello World на IronPython"
date: 2008-10-21T10:30:00+03:00
draft: False
category: [Python]
tags: [.net,python,iron python,dlr]
archives: [2008]
aliases:
    - post/Hello-World-with-IronPython.aspx
---



[IronPython](http://www.codeplex.com/IronPython) - динамический язык с поддержкой .NET. Полностью совместим с оригинальным [Python](http://python.org/), но, в тоже время, позволяет пользоваться всеми преимуществами .net framework. Проект развивается комьюнити и поддерживается Microsoft. Оффициальный блог - [http://blogs.msdn.com/ironpython](http://blogs.msdn.com/ironpython). Текущая стабильная версия - 1.1.2, но уже сейчас доступна вполне рабочая 2.0 Beta 5, которая включает в себя множетсво баг-фиксов и другие изменения. 



Чтобы начать программировать на этом языке достаточно всего лишь скачать его дистрибутив и запустить его консоль. Только таким образом мы избавим себя от таких удобств, как:удобная IDE, подсветка кода, дебаггер и всё то, что помагает нам каждый день в порцессе разработки прилижений. 



В качестве IDE можно выбрать [SharpDevelop](http://www.codeplex.com/SharpDevelop), который уже после установки поддерживает IronPython, или же установить [IronPython Studio](http://www.codeplex.com/IronPythonStudio) - продукт, основанный на Visual Studio Shell и может работеть как отдельное приложение, так и как часть Visual Studio. 



 После установки IronPython Studio появляются новые проекты на языке IronPython: Console Application, Windows Application, Class Library и WPF Application. 



 



<img src="/image.axd?picture=IronPython_1.JPG" alt="" width="683" height="464" /> 



Для написания первого приложения создаём Console Application. После чего нам генерируется приложение, которое уже выводит на экран текст. Но, так как мыхотим использовать для этого .net framework, то немногоменяем код: 



 


> 
	`<font face="Courier New" size="2" color="#000000"></font><font face="Courier New" size="2" color="#000000"><font color="#0000ff">from</font> System import * </font><font face="Courier New" size="2" color="#000000">hello = <font color="#a31515">"Hello World!!!"</font> </font><font face="Courier New" size="2" color="#000000"><font color="#2b91af">Console</font>.WriteLine(hello) </font><font face="Courier New" size="2" color="#000000"><font color="#2b91af">Console</font>.ReadLine()</font> <font size="1" color="#808080"></font>` 



 



 Продоление следует... 



 P.S. А логотим [Python](http://python.org/) чем-то напоминает украинский фаг. 


