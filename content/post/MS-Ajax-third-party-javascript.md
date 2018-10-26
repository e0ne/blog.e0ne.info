---
title: "MS Ajax и сторонние скрипты"
date: 2008-04-05T01:31:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,ajax,javascript]
archives: [2008]
aliases:
    - post/MS-Ajax-third-party-javascript.aspx
---



Интеграция различных скриптов на страницу, где используется MS Ajax - задача нередкая, но единого решения для неё не существует. Я поделюсь с вами некоторыми методами, которые помогут интегрировать срипт в вашу страницу. 


	<li>
	
	Никогда не подключайте скрипты с помощью тега <font size="2" color="#0000ff"><font size="2" color="#0000ff"><</font></font><font size="2" color="#a31515"><font size="2" color="#a31515">script</font></font><font size="2"> </font><font size="2" color="#ff0000"><font size="2" color="#ff0000">src</font></font><font size="2" color="#0000ff"><font size="2" color="#0000ff">="..."></</font></font><font size="2" color="#a31515"><font size="2" color="#a31515">script</font></font><font size="2" color="#0000ff"><font size="2" color="#0000ff">></font></font>. Вместо этого следует использовать копмонени ScriptManager либо ScriptManagerProxy. 
	
	</li>
	<li>
	
	Что бы не говорили разработчики MS Ajax и AjaxControlToolkit, в конец каждого файла со скриптом следует добавить такой код:<br />
	<font size="2" color="#0000ff"><font size="2" color="#0000ff">if</font></font><font size="2"> (</font><font size="2" color="#0000ff"><font size="2" color="#0000ff">typeof</font></font><font size="2">(Sys) !== </font><font size="2" color="#a31515"><font size="2" color="#a31515">'undefined'</font></font><font size="2">) Sys.Application.notifyScriptLoaded();<br />
	</font>Данный код указывает на то, что скрипт полностью загрущился и можно его выполнять. 
	
	</li>
	<li>
	
	Если скрипт необходимо подгружать только в определённых ситуациях (например, добавление нового компонента на форму), то его следует регистрировать с помощью статических методов класса ScriptManager вида RegisterClientScriptXXX(). 
	
	</li>
	<li>
	
	Для выполнения скрипта после загрузки на страницу есть несколько методов: <br />
	1) использовать клиентское событие EndRequest;<br />
	2) создать функцию с именем pageLoad() - метод аналогичен первому;<br />
	3) если скрипт необходимо зарегистрировать с помощью серверного кода, то используйте метод <font size="2" color="#2b91af"><font size="2" color="#2b91af">ScriptManager</font></font><font size="2">.RegisterStartupScript().</font> 
	
	</li>


Эти методы не являются панацеей от всех бед, но помогают экономить часть времени, необходимого на интеграцию скриптов. Иногда хватает только этого, иногда приходится часами отлаживать чужой javascript, но знать о них, как я думаю, должен каждый разработчик, использующий MS Ajax. 


