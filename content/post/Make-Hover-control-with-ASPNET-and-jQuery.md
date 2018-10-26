---
title: "Делаем Hover control с ипользованием ASP.NET и jQuery"
date: 2010-06-14T15:30:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,javascript,jquery]
archives: [2010]
aliases:
    - post/Make-Hover-control-with-ASPNET-and-jQuery.aspx
---


В связи с тем, что я повсеместно пытаюсь избавиться от [ASP.NET AJAX Control Toolkit (ACT)](http://www.asp.net/ajax/AjaxControlToolkit/Samples/) и перейти на использование [jQuery](http://jquery.com/), то от использования Hover Extender от ACT пришлось отказаться. Сразу же было найдено большое количество разнообразных плагинов для jQuery, но большинство из них имели недостаточную реализацию, из-за чегоостановился на [jQuery plugin EZPZ Tooltip](http://theezpzway.com/2009/3/17/jquery-plugin-ezpz-tooltip).

Из основных достоинств данного плагина хочется выделить:

- "Чистый" HTML - не нужно добавлять специальные атрибуты для элементов, плагин завязывается на отдельный HTML элемент.
- Конфигурация через наименование (Convention over configuration) - поведение элементов зависит от из ID.
- Гибкие настройки - с помощью CSS можно настроить как внешний вид контрола, так и его позиционирование.
- Возможность замены стандартных эффектов путем перехвата соответствующих событий на jQuery.
- Удобство и простота работы.
- Маленький размер - 4.5K в сжатов виде.

Более подробно о всем этом можно почитать на [странице](http://theezpzway.com/2009/3/17/jquery-plugin-ezpz-tooltip) проекта, а я хочу рассказать как можно его использовать в связке с ASP.NET на примере простого UserControl.

Для инициализации контрола нужно выполнить небольшой javascript:

$("#example-target-1").ezpz_tooltip();<br />или<br />$("#target").ezpz_tooltip({contentId:"content"}); - В случае если у наших HTML-элементов будут "нестандартные" для этого контрола ID.

Так как, ASP.NET сам генерирует нам ClientID элементов (я не учитываю специфику ASP.NET 4.0, где можно отключать автоматическую генерацию ClientID), то приходится использовать 2-й вариант таки образом:

 <img src="/image.axd?picture=2010%2f6%2fhover_1.jpg" alt="" />

При этом у нас:

-  TargetControlId - ID элемента, при наведении на который будет отображаться наш hover (tooltip).
- ContainerClientId - ID элемента который будет показываться в качестве hover (tooltip).

 Разметка нашего user control выглядит так:

 

<img src="/image.axd?picture=2010%2f6%2fhover_2.jpg" alt="" />

Нам остаётся только разместить наш UserControl на странице и подключить необходимые стили и скрипты. Можно ещё сделать WebControl, но это уже зависит от конкретной задачи. В моём случае UserControl был предпочтительнее.

[HoverControl.zip (31.35 kb)](/file.axd?file=2010%2f6%2fHoverControl.zip)

