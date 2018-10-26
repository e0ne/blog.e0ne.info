---
title: "Новый релиз Mono 2.2"
date: 2009-01-21T09:00:00+03:00
draft: False
category: [.NET Framework]
tags: [.net,mono]
archives: [2009]
aliases:
    - post/Mono-22.aspx
---


Делюсь моими впечатлениями от знакомства с [Mono](http://www.mono-project.com). 

На прошлой неделе вышел очередной релиз [Mono](http://www.mono-project.com) - open source реализации .Net framework, разрабатываемый при поддержке компаний [Novell](http://www.novell.com/) и [Microsoft](http://www.microsoft.com/). Подробно но нововведения можно почитать на странице проекта [http://www.mono-project.com/Release_Notes_Mono_2.2](http://www.mono-project.com/Release_Notes_Mono_2.2). 

Радует, что Mono в последних версиях поддерживает C# 3.0. Также есть [Moonlight 1.0](http://www.go-mono.com/moonlight/)  - аналог Silverlight 2.0. Для миграции существующих проектов есть утилита Mono Migration Analyzer, которая позволяет узнать будет ли работать существующий код под Mono. Хочу сказать, что запуск небольшого WinForms приложения написаного на .Net framework 3.5 прошел порблем, а вот с web-приложением все немного хуже. Оффицияльня IDE MonoDevelop не поддерживает Web Application проекты, созданные в VS2008, поэтому для открытия каккого-ннибудь сужествующего проекти или StarterKit пришлось создавать новый проект и вручную добавлять в него все необходимые файлы. По удобству работы MonoDevelopв данный момент существенно проигрывает своему старшему брату и конкуренту - VisualStudio, но работать вполне можно. За время её использования MonoDevelop не разу не упала, аботала стабильно.

 Вот так прошло моё знакомство с тем, что неоторые называют "убийцей .net", а некоторые просто не верят в жизнеспособность этого продукта.

To be continued... 

