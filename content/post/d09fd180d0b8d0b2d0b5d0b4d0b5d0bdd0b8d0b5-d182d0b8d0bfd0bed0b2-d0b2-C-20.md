---
title: "Приведение типов в C# 2.0"
date: 2008-01-17T01:48:00+03:00
draft: False
category: []
tags: [.net framework,c#]
archives: [2008]
aliases:
    - post/d09fd180d0b8d0b2d0b5d0b4d0b5d0bdd0b8d0b5-d182d0b8d0bfd0bed0b2-d0b2-C-20.aspx
---



Приведение типов на практике встречается довольно часто. Из-за того, что в языке C# существует два оператора, позволяющих решить эту задачу, время от времени возникают InvalidCastException. Остановимся на этих операторах подробнее.<br />
<br />
1. () оператор. На уровне IL-кода генерирует вызов функции castclass Выдержка из msdn: A cast explicitly invokes the conversion operator from one type to another; the cast fails if no such conversion operator is defined. <br />
Оператор можно использовать только в том случае, если это предусмотрел разработчик. <br />
Плюсы: простота в использовании, читабельность кода. Работает как с value, так и с reference типами.<br />
Минусы: можно использовать не со всеми типами данных; источник InvalidCastException в случае неудачного вызова. 


> 
	<p>
	<br />
	int? i1 = 2;<br />
	// вычисление значения i2<br />
	int i2 = (int)i1; // к этому моменту возможна ситуация, когда i1 будет равным null.
	</p>


> 
	<br />
	public void MyMethod(object intObj)<br />
	{<br />
	if (intObj != null)<br />
	{<br />
	int intO = (int) intObj;<br />
	// ...<br />
	}<br />
	}<br />


> 
	string s = someObject as string;<br />
	if (s != null)<br />
	{<br />
	// someObject is a string.<br />
	}


