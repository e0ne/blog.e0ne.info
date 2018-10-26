---
title: "HTML Decode/Encode и URL Decode/Encode - что, когда и зачем использовать?"
date: 2010-09-03T11:15:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,python,javascript,xss]
archives: [2010]
aliases:
    - post/HTML-DecodeEncode-and-URL-DecodeEncode-what-when-and-why-to-use.aspx
---


## HTML Decode/Encode.

Если кто-то слышал об такой атаке на веб-сайты, как XSS Injection, то он(она) знает что для предотвращение такой атаки необходимо использовать функции HtmlEncode/HtmlDecode. XSS Injection (Cross-site injection) - один из способов атак веб-приложений, главной идеей которого является вставка(инъекция) чужого javascript-кода на атакуемый веб-сайт. Как минимум, это может привести к краже печенек cookies и получении прав администратора сайта. ...

### 1.1. ASP.NET

Это происходит, примерно, так:<br />Допустим, у нас есть форма для отправки комментарием, где пользователь вводит свой еmail и текст коммеентария. Самый простой обработчик кнопки добавить окмментарий будет выглядить так:

С первой точки зрения этот код не содержит никаких ошибок, компилируется и корректно сохраняет данные в БД. Но, если в тексте  комментария будет любой HTML или JavaScript-код, то при отображении этого комментария на страницу без предварительной обработки мы увидем, что HTML и JavaScript-код без особых проблем обрабатываются браузером. <br />Таким образом, мы сделали наш сайт уязвимым и нарушили одно из базовых правил проектирования ПО: “Не доверять данным, которые пришли извне нашей системы”. От себя еще добавлю: вдвойне недоверять данным, которые были введенны пользователем. Чтобы исправить это ошибку, необходимо всего-лишь вызвать метод HttpServerUtility.HtmlEncode(), перед сохранением данных в базу:

После чего, строка вида **“<script>alert(‘hello!’);</script>”** будет сохранена в базу в таком виде:

Теперь все хорошо: любой введенный пользователем текст не ламает нашу верстку и не вызывает выполнения стороннего javascript (пример 2).<br />Но все не так просто, как кажется. Теперь, если такой код вставить в обработчике OnAddPage(), где администратор сайта будет добавлять страницы, то вместо красивого текста пользователи увидят набор непонятных символов. Поэтому, при отображении содержимого страницы мы вызываем метод HttpServerUtility.HtmlDecode(), который переведет сохраненный в базе данных текст в такой вид, чтобы браузер его корректно обрабатывал.

Таким образом, мы избавили наш сайт от XSS Injection дали возможность пользователям воодить разнообразные данные без вреда для сайта.

Примечание. Во всех примерах выше свойство странице EnableRequestValidation было установлено в false для возможноти ввода символов “<“ и “>”.<br />Примечание для ASP.NET 4.0/ASP.NET MVC 2.0. В ASP.NET 4.0/ASP.NET MVC 2.0 появилась конструкция <%: ... %>, которая делает за нас HTML Decode/Encode.

### 1.2. JavaScript

Если нам необходимо реализовать данную функциональность на клиенте с помощью javascript, то нам на помощь приходит jQuery:

### 1.3 Python/Django

В фреймворке Django HTML Decode работает по умолчанию, и для его отключение в шаблоне (template) добавить блок** {% autoescape off %}** и в нем поместить все элементы, для которых нам не нужен HTML Decode, после чего закрыть блок с помощью** {% endautoescape %}**.

## 2. URL Decode/Encode.

В отличии от HTML Encode/Decode незаэкранированный url больших проблем не вызывает, за исключением двух моментов: url становится не таким простым и понятным для пользователя и это не очень хорошо влияет на SEO.

### 2.1 ASP.NET

Рассмотрим такую ситуацию: у нас есть сайт с функцией поиска по нем. Стандартная форма поиска содержит поле для вводи и кнопу "Поиск". В простейшем случае при нажатии на кнопку “Поиск” у нас есть такой обработчик:

Вполне рабочий код, за исключением того, что в некоторых случаях в итоге мы получаем не очень красивый url вида:

**/Search.aspx?q=some%20keywords**

Конечно, такой url правильно обрабатывается браузером, но не всем пользователям будет понятно что он значит. Происходит это из-за того, что браузер автоматически заменяет символ пробела и ряд других символов на  их шестнадцатиричное значение вида %XX, где XX - код символа в шестнадцатиричной системе.<br />Сделано это было давно, кода браузеры были маленкими еще не умели отображать нелатинские символы в строке ввода адреса и для правильного отображения разнообразных символов.<br />И тут нам на помощь приходят методы HttpServerUtility.UrlEncode() и HttpServerUtility.UrlDecode() которые предназначены для переобразования параметров строки запроса в понятный для пользователей вид. Отдельно отчему, что эти методы предназначены для обработки исключительно параметров url, а для переобразования адреса к необходимому ресурсу существует метод HttpServerUtility.UrlPathEncode(), работа которого больше похожа на работу метода HttpServerUtility.HtmlEncode(), но учитывает все особенности построения url. Этот метод не имеет метода для обратного переобразования, но при правильном подходе к проектированию приложенич это не понадобится.

### 2.2. JavaScript

Аналог URL Encode в javascript - функция encodeURI()
