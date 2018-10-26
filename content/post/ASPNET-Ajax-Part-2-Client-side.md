---
title: "ASP.NET Ajax. Часть 2: Client-side"
date: 2010-09-15T16:30:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [ajax,asp.net,java script]
archives: [2010]
aliases:
    - post/ASPNET-Ajax-Part-2-Client-side.aspx
---


## [1. Введение](#intro)<br />[2. Обзор framework'а](#overview)<br />[3. Жизненный цикл страницы](#lifecycle)<br />[4. Полезные объекты и функции](#features)

<a name="intro"></a>

## 1. Введение

В предыдущем посте из этой серии ([ASP.NET Ajax. Часть 1: что внутри?]( http://blog.e0ne.info/post/ASPNET-Ajax-Part1-Look-Inside.aspx)) я рассказал что такое AJAX и как Microsoft помогает нам его использовать. Сегодня я более подробно расскажу о его клиентской части. Частично из-за того, что эту информацию не так просто найти в MSDN, как хотелось бы, частично  из-за того, что в последнее время Microsoft уделяет этой части всё меньше внимания, агитируя использовать jQuery, многие разработчики даже на догадываются какой мощных инструмент находится у них в руках.

<a name="overview"></a>

## 2. Обзор framework'а

По умолчанию, эти скрипты грузятся на страницу, на которой есть ScriptManager по ссылке вида ScriptResource.axd?d=scriptIdentificator. Сами же скрипты находятся в ресурсах сборки System.Web.Extensions (если у кого-то всё-ещё установлена VS2005, то эти скрипты можно найти в папке c:\Program Files\Microsoft ASP.NET\ASP.NET 2.0 AJAX Extensions\v1.0.61025\MicrosoftAjaxLibrary\System.Web.Extensions\). Также можно загружать эти скрипты с помощью CDN. Подробнее об этом способе можно почитать [тут](http://blog.turlov.com/2009/11/using-microsoft-ajax-library-35-with.html).<br />Сам скирт немного отличается для WebForms и ASP.NET MVC, но ядро у них общее.<br />Все функции/объекты разделены на пространства имён (namespaces) по аналогии с серверной частью. Перечислять я их не буду, так как на MSDN ([http://msdn.microsoft.com/en-us/library/bb397536.aspx](http://msdn.microsoft.com/en-us/library/bb397536.aspx), [http://msdn.microsoft.com/en-us/library/dd410060.aspx](http://msdn.microsoft.com/en-us/library/dd410060.aspx)) всё хорошо описано.

<a name="lifecycle"></a>

## 3. Жизненный цикл страницы

Кроме стандартных для DOM модели событий, ASP.NET Ajax предоставляет нам  доступ как к событиям всего приложения (init, load, unload и др.), так и события, связанные с запросами на сервер (beginRequest, endRequest и др.). Как всегда, за полной информацией лучше обратиться в первоисточник, а именно - [http://msdn.microsoft.com/en-us/library/bb386417.aspx](http://msdn.microsoft.com/en-us/library/bb386417.aspx).

<a name="features"></a>

## 4.Полезные объекты и функции

MS Ajax Library предоставляет нам как новые типы/функции, так и расширения для стандартных - Array, Number, Date, String и др., о которых можно почитать в MSDN Magazine ([http://msdn.microsoft.com/en-us/magazine/cc163300.aspx](http://msdn.microsoft.com/en-us/magazine/cc163300.aspx)).<br />Одними из наиболее частоиспользуемых являются функции $get() и $find():<br />- $get()  - оптимизированный по производительности аналог document.getElementById, который ищет элемент по его ID и в качестве второго параметра может принимать parent-элемент, в котором нам необходимо найти нужный элемент DOM-модели.<br />- $find() - функция, которая очень похожа на $get(), но возвращает не DOM-элемент, а экзепмляр [Ajax Client Control](http://blog.e0ne.info/post/IScriptControl-Ajax-Client-Control-Implementation.aspx).<br />Более детальное описания использования этих функций: [http://mattberseth.com/blog/2007/08/the_everuseful_get_and_find_as.html](http://mattberseth.com/blog/2007/08/the_everuseful_get_and_find_as.html)

