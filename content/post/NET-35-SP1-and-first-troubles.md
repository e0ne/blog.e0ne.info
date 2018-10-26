---
title: ".NET 3.5 SP1 и первые проблемы"
date: 2008-08-22T10:15:00+03:00
draft: False
category: [.NET Framework]
tags: [.net framework 3.5,ajax,asp.net,ajax control toolkit]
archives: [2008]
aliases:
    - post/NET-35-SP1-and-first-troubles.aspx
---



Свершилось! Несколько дней назад вышел [</script>8319-81da479ab0d7&displaylang=en" target="_blank">.net 3.5 service pack 1](http://www.microsoft.com/downloads/details.aspx?familyid=ab99342f-5d1a-413d-<script type=). В месте с ним мы получили ASP.NET Dynamic Data,  Entity Framework,  ADO.NET Data Services и много чего другого. Подообнее можно почитать [тут](http://msdn.microsoft.com/en-us/vstudio/products/cc533447.aspx). 



Но, разумеется, в каждой бочке мёда найдётся своя ложка дёгтя. Ей стал [Ajax Control Toolkit](http://www.codeplex.com/AjaxControlToolkit), а именно одни из его базовых компонентов - ToolkitScriptManager. После установки .net 3.5 sp1 ToolkitScriptManager, входящий в состав Microsoft Ajax Control toolkit, перестал правильно функционировать. Разработчики компонентов достаточно быстро отреагировали  и выпустили новый релиз, который имеет совместимость с носледней версией .net framework. Так что ставим новую версию, и продолжаем использовать пусть и не лучшую, но уже ставшую достаточно популярной связку MS Ajax и Ajax Control Toolkit. Новую версию тулкита качает [здесь](http://www.codeplex.com/AjaxControlToolkit/Release/ProjectReleases.aspx?ReleaseId=16488). 


