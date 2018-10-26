---
title: "Dynamic Language Runtime: динамические языки в .NET"
date: 2009-03-21T14:18:00+03:00
draft: False
category: [.NET Framework,Python]
tags: [dlr]
archives: [2009]
aliases:
    - post/Dynamic-Language-Runtime-Dynamic-Languages-in-dot-NET.aspx
---


[Dynamic Language Runtime (DLR)](http://www.codeplex.com/dlr) - позволяет создавать свои динамические языки на платформе .NET. Сейчас самыми популярными из них являются IronPython и IronRuby. Также на просторах CodePlex существует [IronLisp](http://ironlisp.codeplex.com/) и другие динамические языки. Последняя версия DLR имеет номер 0.9 и была выпущена 10 декабря 2008 года.

<img src="/image.axd?picture=dlr0.jpg" alt="" width="638" height="373" />

Кроме того, что DLR позволяет создавать динамические языки, она также позволяет добавлять динамические элементы в уже сеществующие языки: C# 4.0 уже использует DLR - смотрите в сторону IDynamicObject.  Если я правильно понял документ DLR Overview, то DLR 1.0 будет частью Common Language Runtime (CLR), выход которой уже не за горами.

Dynamic Language Runtime состоит из трех основных частей: 

- Common Hosting - оперирует со скриптами (компиляция, парсинг, загрузка), включает в себя всю необходимую функциональность для работы со скриптами динамических языков.
- Runtime - как видно из названия отвечает за выполнение скриптов, взаимодействие с COM, CLR.
- Language Implementation - отвечает за механизмы, необходимые для реализации скриптовых языков. 

 

<img src="/image.axd?picture=dlr1.jpg" alt="" width="630" height="389" /><br /> <br /> Все это очень хорошо подробно описано в документации (DLR Overview и DLR Spec), которую можно скачать со [страницы проекта](http://dlr.codeplex.com/Wiki/View.aspx?title=Docs%20and%20specs&referringTitle=Home).

Если у вас будет желания (не будет желания читать официальную, англоязычную, документацию), то в следующих постах я рассмотрю более подробнее работу DLR.

