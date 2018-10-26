---
title: "Configuration Section Designer - дизайнер настроек"
date: 2008-10-09T20:15:00+03:00
draft: False
category: [.NET Framework]
tags: [visual studio,codeplex]
archives: [2008]
aliases:
    - post/Configuration-Section-Designer-the-Designer-of-Settings.aspx
---


Почти год назад я писал о плагине для Visual Studio, под названием [Visual Local History 2005](http://www.codeplex.com/VLH2005/) - мини система контролей версий на локальном компьютере. Не так давно на [www.codeplex.com](http://www.codeplex.com/) был найден очередной интересный, а главное - полезный, проект под названием [Configuration Section Designer](http://www.codeplex.com/csd). 

 

<img style="width: 502px; height: 341px" src="/image.axd?picture=DSC00987.JPG" alt="" />

После установки плагин добавляет новый тип проекта в Visual Studio, к котором подобно class diagram можно "рисовать" диаграммы конфигурационных файлов. После чего, плагин автоматически сгенерирует класс, который будет содержать в себе конфигурационную секцию, сделанную в диаграмме, доступ к настройкам будет состоять из доступа к свойствам класса.

Пример: с помощью диаграммы мы описали такой конфигурационный файл:

 

 После этого, чтобы прочитать значение, необходимо только обратиться к свойству класса CustomSettingsSection.ConnectionStrings.LocalConnectionStrings, которое вам вернёт строку подключения к базе данных.

Кроме этого, плагин генерирует xsd-схему, что добавит intellisense для конфигурационного файла. Таким образом работа с файлами настроек становится легкой и быстрой.

