---
title: "Несколько слов о ASP.NET и безопастности"
date: 2008-09-23T14:35:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [asp.net,security]
archives: [2008]
aliases:
    - post/few-words-about-aspnet-and-security.aspx
---



Навеянно постом "[Asp.NET контроли і HtmlEncode](http://dev.net.ua/blogs/mikechaliy/archive/2008/09/17/6886.aspx)". Сейчас уже многие пользуются методами HtmlEncode/HtmlDecode и UrlEncode/UrlDecode для обработки данных, которые ввел пользователь. Но эти медоты используют базовый алгоритм, что может не подходить для частных случаев, таких как использование данных в качестве атрибутов html-тегов и других. Более спецефические методы нам предоставлены в библиотеке [Microsoft Anti-Cross Site Scripting Library](http://www.microsoft.com/downloads/details.aspx?familyid=EFB9C819-53FF-4F82-BFAF-E11625130C25&displaylang=en). Более подробно о ней и ещё преимуществах написано в документации. 



Также для нахождения Sql и XSS Injection предоставлены [Microsoft Source Code Analyzer for SQL Injection](http://www.microsoft.com/downloads/info.aspx?na=47&p=1&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=efb9c819-53ff-4f82-bfaf-e11625130c25&u=details.aspx%3ffamilyid%3d58A7C46E-A599-4FCB-9AB4-A4334146B6BA%26displaylang%3den) и [XSS Detect Beta Code Analysis Tool](http://www.microsoft.com/downloads/info.aspx?na=47&p=4&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=efb9c819-53ff-4f82-bfaf-e11625130c25&u=details.aspx%3ffamilyid%3d19A9E348-BDB9-45B3-A1B7-44CCDCB7CFBE%26displaylang%3den) соответственно. НЕ забываем прочитать базовые вседения о безопастности веб-приложений в целом и приложений, написанных на ASP.NET в частности. 


	- [Improving Web Application Security: Threats and Countermeasures](http://www.microsoft.com/downloads/details.aspx?familyid=E9C4BFAA-AF88-4AA5-88D4-0DEA898C31B9&displaylang=en)  [ ](http://www.microsoft.com/downloads/details.aspx?familyid=E9C4BFAA-AF88-4AA5-88D4-0DEA898C31B9&displaylang=en)
	- [Building Secure ASP .NET Applications ](http://www.microsoft.com/downloads/info.aspx?na=40&p=1&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=e9c4bfaa-af88-4aa5-88d4-0dea898c31b9&u=http%3a%2f%2fmsdn.microsoft.com%2flibrary%2fdefault.asp%3furl%3d%2flibrary%2fen-us%2fdnnetsec%2fhtml%2fsecnetlpMSDN.asp%3fframe%3dtrue)
	- [Improving Web Application Security: Threats and Countermeasures ](http://www.microsoft.com/downloads/info.aspx?na=40&p=2&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=e9c4bfaa-af88-4aa5-88d4-0dea898c31b9&u=http%3a%2f%2fmsdn.microsoft.com%2flibrary%2fdefault.asp%3furl%3d%2flibrary%2fen-us%2fdnnetsec%2fhtml%2fThreatCounter.asp)
	- [Web Service Security Guide ](http://www.microsoft.com/downloads/info.aspx?na=47&p=1&SrcDisplayLang=en&SrcCategoryId=&SrcFamilyId=e9c4bfaa-af88-4aa5-88d4-0dea898c31b9&u=details.aspx%3ffamilyid%3d3E02A6C8-128A-47C2-9F39-4082582F3FE1%26displaylang%3den)

