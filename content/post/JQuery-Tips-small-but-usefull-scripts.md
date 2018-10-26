---
title: "JQuery Tips: маленькие, но полезные скрипты"
date: 2010-08-10T22:25:00+03:00
draft: False
category: [Web Development]
tags: [javascript,jquery]
archives: [2010]
aliases:
    - post/JQuery-Tips-small-but-usefull-scripts.aspx
---


Те, кто с помощью [jQuery](http://jquery.com/) написал уже не одну сотню, а может и тысячу строк javascript-кода, в этом посте врядли найдут много нового и/или интересного. Пост рассчитан на разработчиков, которые только начинают знакомиться со всей мощью бтблиотеки [jQuery](http://jquery.com/). В нем я дам несколько примеров скриптов, которые я время от времени использую с небольшим количеством изменений или вообще без таковых.

[Добавлено перед публикацией поста]<br />Все примеры достаточно просты, большинство (5 штук!) взяты из документации, но они активно используются мной и я решил сделать пост-заметку для себя. Может, еще кому-то будет полезно. Те, кто не использует [jQuery](http://jquery.com/) либо другую библиотеку (еще остались такие?) поймут, что эти несколько строк кода в каждом примере иногда заменяют десятки строк кода на javascript’е без использования сторонних библиотек и своих велосипедов.<br />[/Добавлено перед публикацией поста]

- Прочитать и/или изменить значение нужного атрибута в элемента DOM-модели: <br />**var value = $("#element").attr("custimAttribute"); <br />**и<br />**$("#element").attr("custimAttribute")=”some text”;** 
- Тоже самое, но для классов:<br />методы **.addClass()** ([http://api.jquery.com/addClass/](http://api.jquery.com/addClass/)) и **.removeClass()** ([http://api.jquery.com/removeClass/](http://api.jquery.com/removeClass/))  
- Сделать подсветку всех картинок на странице по заданному параметру (имя класса):<br />**$(".image").mouseover(function () { <br />    $(this).css("border-width", "2px");<br />    $(this).css("border-style", "solid"); <br />    $(this).css("border-color", "#1b5790"); <br />});** ****
- Сделать какие-либо действия над коллекцией объектов: <br />**$.each([52, 97], function(index, value) {<br />    alert(index + : + value); <br />});** <br />[http://api.jquery.com/jQuery.each/](http://api.jquery.com/jQuery.each/)
- Присвоить tabIndex для всех элементов ввода на форме: <br />**$(function(){ <br />    var tabindex = 1; <br />    $(input,select).each(function() { <br />         if (this.type != "hidden") { <br />              var $input = $(this); <br />              $input.attr("tabindex", tabindex); <br />              tabindex++; <br />         } <br />    }); <br /> });** <br />[http://greatwebguy.com/programming/dom/setting-your-tabindex-on-your-html-forms-automatically-with-jquery/](http://greatwebguy.com/programming/dom/setting-your-tabindex-on-your-html-forms-automatically-with-jquery/) 
- Отправить AJAX-запрос на сервер:<br />как ни странно, но примеры из документации [http://api.jquery.com/category/ajax/](http://api.jquery.com/category/ajax/) достаточно работоспособны чтобы использовать их практически без изменений (ссылку на службу все-таки прийдется подставить свою). 
- Создать start-up скрипт на странице (без использования ScriptManager, входящего в состав ASP.NET):<br />**$(document).ready(function () {<br />     alert (hello); <br />});** 

 

