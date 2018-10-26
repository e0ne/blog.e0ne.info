---
title: "Миграция unit tests на Visual Studio 2008"
date: 2008-03-03T02:12:00+03:00
draft: False
category: [.NET Framework]
tags: [.net,visual studio,unit tests]
archives: [2008]
aliases:
    - post/d09cd0b8d0b3d180d0b0d186d0b8d18f-unit-tests-d0bdd0b0-Visual-Studio-2008.aspx
---



При миграции unit-тестов с Visual Studio 2005 на 2008 (.net 2.0) обнаружил интересный баг. Студия радостно отрапортовала об успешной конвертиции проектов, но при запустке тесты проваливались с такой ошибкой: 


> 
	Method SampleTest.ClassDBTest.MyClassInitialize has wrong signature. Parameter 1 should be of type Microsoft.VisualStudio.TestTools.UnitTesting.TestContext. 


