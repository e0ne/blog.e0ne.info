---
title: "Request validation в ASP.NET"
date: 2010-11-26T12:32:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [xss,asp.net]
archives: [2010]
aliases:
    - post/Request-validation-in-ASPNET.aspx
---


Со времен ASP.NET 1.1, по умолчанию, у всех страниц свойство ValidateRequest было равно true. Это означает, что при вводе в поле ввода определенные спецсимволы (пример: <,>,&,#)  и отправки формы на сервер мы успешно получим HttpRequestValidationException.

Непонятное, на первый взгляд, поведение объясняется достаточно просто - защита от XSS атак. XSS (cross site scripting) - один из типов атак на веб-сайт, целью которой является вставка (инъекция)  чужого javascript-кода на атакуемый сайт. Результатами такой атаки могут быть от показа пользователю ненужных ему сообщений, до кражи cookie и перенаправления на другой сайт, который может содержать вредоносный код. Пример такой ситуации можно посмотреть в XssSample.aspx.

Но так как в определённых ситуациях должна быть возможность ввести любой символ, то приходится отключать request validation. Для предотвращения XSS-атаки при отображении пользователю введенного текста необходимо экранировать специальные символы с помощью метода Server.HtmlEncode(). Пример кода находится в AntiXssSample.aspx.

На первый взгляд, кажется что всё просто и понятно. Но есть некоторые нюансы:

- необходимо помнить о том, что request validation отключен и нужно экранировать весь введенный пользователем текст во все поля (помним правило: никогда(!) не доверять данным, которые ввёл пользователь);
- если используется Server.HtmlEncode(), то помним, что есть ещё “обратный” метод Server.HtmlDecode();
- можно не отключать request validation и экранировать все введенные данные на стороне клиента с помощью javascript, но при этом не забывать о валидации (проверки) данных на сервере.

В целом, при правильном подходе никаких проблем с отключением request validation не должно быть, но всегда необходимо помнить о безопасности.

Ещё стоит отметить то, что механихм request validation немного поменялся в ASP.NET 4. Теперь он, по умолчанию, проверяет не только запросы к aspx страницам, но и все остальные запросы к серверу. Отключить это можно в web.config таким способом:

Ссылки по теме:

- [http://blog.e0ne.info/post/HTML-DecodeEncode-and-URL-DecodeEncode-what-when-and-why-to-use.aspx](http://blog.e0ne.info/post/HTML-DecodeEncode-and-URL-DecodeEncode-what-when-and-why-to-use.aspx)
- [http://www.asp.net/LEARN/whitepapers/request-validation](http://www.asp.net/LEARN/whitepapers/request-validation)
- [http://www.asp.net/learn/whitepapers/aspnet4/breaking-changes#0.1__Toc256770147](http://www.asp.net/learn/whitepapers/aspnet4/breaking-changes#0.1__Toc256770147)
- [http://msdn.microsoft.com/en-us/library/system.web.httprequestvalidationexception.aspx](http://msdn.microsoft.com/en-us/library/system.web.httprequestvalidationexception.aspx)
- [http://en.wikipedia.org/wiki/Cross-site_scripting](http://en.wikipedia.org/wiki/Cross-site_scripting)

Ссылка на пример: [https://github.com/e0ne/BlogSamples](https://github.com/e0ne/BlogSamples)

