---
title: "Делаем daily builds с помощью CruiseControl.NET и Nant"
date: 2009-05-01T13:05:00+03:00
draft: True
category: []
tags: []
archives: [2009]
aliases:
    - post/d094d0b5d0bbd0b0d0b5d0bc-daily-builds-d181-d0bfd0bed0bcd0bed189d18cd18e-CruiseControlNET-d0b8-Nant.aspx
---


Не так давно мне поставили задачу: сделать ежедневные билды для тестирования. Делать это каждый день вручную надоело уже во второй день и я решил всё это автоматизировать. Так как, до этогго до этого я уже сталкивался с CruiseControl.NET, то решил использовать это приложение. Первым делом я зашел на Google, чтобы скачать дистрибутив. Естесстенно, в строке запроса я ввел CruiseControl, что привело меня к [http://cruisecontrol.sourceforge.net/](http://cruisecontrol.sourceforge.net/). Невнимательно прочитав содержимое первой страницы, пошел по ссылке download и скачал дистрибутив. После установки и нескольких не очень успешных попыток всё это заставить работать, окачалось что CruiseControl и CruiseControl.NET являются разными продуктами, хотя в целом синтаксис конфигурационных файлов очень похож.

> 		<br />	<blockquote style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 40px; border-width: initial; border-color: initial; border-style: none; padding: 0px">		"There are ports of CruiseControl for .NET and Ruby. The original CruiseControl source code was contributed by ThoughtWorks, who now offers the commerical tool Cruise (not based on the CruiseControl codebase)."	

> 		Эксперементировать дальше с CruiseContol времени не было и я вернулся к уже знакомому порту, написанном на .NET.	

В целом, порцесс сборки билдов у меня поделился на такие этапы:
			1. Забрать последнюю версию исходников из репозитария. <br />				1. Скомпилировать web-site и обновить его версию на тестовом сервере.<br />				1. Разослать нотификации о новом билде на email.<br />		
 

Для начала я в общих расскажу о CruiseControl.NET и Nant, а потом приступим к их конфигурации.

 

