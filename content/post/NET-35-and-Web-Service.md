---
title: ".NET 3.5 и Web Service"
date: 2008-08-19T23:11:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [.net framework 3.5,javascript]
archives: [2008]
aliases:
    - post/NET-35-and-Web-Service.aspx
---



После переходна на новую ферсию .net framework, как и следовало ожидать, некоторый код потерял свою работоспособность. Перестали работать веб-службы. Точнее одна из них.



Серверный её код ничем не выделяется от остальных:


> 
	<font face="Courier New" size="2" color="black">[WebService(Namespace = <font color="#a31515">"myns"</font>)]<br />
	[WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]<br />
	[ScriptService]<br />
	<font color="#0000ff">public</font> <font color="#0000ff">class</font> MyService : WebService<br />
	{<br />
	  [WebMethod, ScriptMethod(ResponseFormat = ResponseFormat.Json)]<br />
	  <font color="#0000ff">public</font> List<<font color="#0000ff">string</font>> GetData()<br />
	  {<br />
	     List<<font color="#0000ff">string</font>> result;<br />
	     <font color="#008000">//вся необходимая логика</font><br />
	     <font color="#0000ff">return</font> result;<br />
	  }<br />
	}</font><font size="1" color="gray"><br />
	<br />
	</font>



 Главное отличие её от других заключается в том, что обращение к ней идёт не с помощью ScriptManager и ServiceReference (в таком случае всё работает), а вызывается методом POST по url напрямую с javascript.



 В .net 2.0 всё работало на ура, но в новой версии фреймворка от сервера приходил ответ слудующего вида:



{"d":__type":"typeName","name":"item1","value":"item2"}



Т.е. получался объект d, а не тот, что передавался служюой, из-за чего скипт работал неправильно. Похожая ситуация и её объяснение описываются [здесь](http://forums.microsoft.com/MSDN/ShowPost.aspx?PostID=3112422&SiteID=1). Security - это, конечно хорошо, но зачем было менять то, что работало в предыдущих версиях .net по умолчанию? Может это повод над тем, что пора отказываться от веб-служб и начинать использовать WCF? Ведь там это всё настраивается с помощью атрибутов.



А пока решение проблемы не найдено, приходится использовать обвёртку и закрывать от глаз тип d.



 



 


