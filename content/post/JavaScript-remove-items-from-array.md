---
title: "JavaScript: удаляем элементы из массива"
date: 2009-07-03T10:18:00+03:00
draft: False
category: [Web Development]
tags: [javascript]
archives: [2009]
aliases:
    - post/JavaScript-remove-items-from-array.aspx
---



Решая на первый взгляд простую задачу я столкнулся с некоторыми поблемами. Задача состоит в том, чтобы из массива удалить один из его элементов. Оказалось, что стандартными средствами JavaScript этого не сделать.



Итак, у нас есть исходный массив:


> 
	<p>
	<em>var arr = new Array();<br />
	arr.push('q');<br />
	arr.push('w');<br />
	arr.push('a');<br />
	arr.push('e');<br />
	arr.push('r');<br />
	arr.push('t');<br />
	arr.push('z');<br />
	arr.push('y'); </em>
	</p>



 Задача состоит в том, чтобы удалить из него элементы со значениями "a" и "z". Первой же идеей было использование оператора delete:


> 
	**var i = arr.indexOf('a');**<br />
	**delete arr[i];**<br />
	**i = arr.indexOf('z');**<br />
	**delete arr[i];**



 И было вы всё хорошо, еслиб не реализация этого самого оператора delete: элементы из массива на самом не удаляются, просто их значение стоновится undefined и, соответственно, свойство lenght не меняется. Можно, конечно, при обходе массива проверять значение элементов и таким образом проверять, удалённый он или нет, но в моём случае это несло за собой изменение логики на сервере, что делать не хотелось и было принято решение реализовать нужную функциональность в классе Array:


> 
	<p>
	<em>Array.prototype.removeByValue = function(item){<br />
	        var itemIndex = -1;<br />
	        for (var index = 0; index < this.length; index++)<br />
	        {<br />
	            if (this[index] == item){<br />
	                itemIndex=index;<br />
	            }<br />
	        }<br />
	        <br />
	        if (itemIndex == -1){<br />
	            return this;<br />
	        }<br />
	        <br />
	        var resultLeft = this.slice(0, itemIndex);<br />
	        var resultRight = this.slice(itemIndex+1, this.length);<br />
	        var resultTotal = resultLeft.concat(resultRight);<br />
	<br />
	        return resultTotal;</em>
	</p>
	<p>
	** };**
	</p>



 Способ использования:


> 
	<em>var a = arr.removeByValue('a'); <br />
	arr = a.removeByValue('z'); </em>



Стоит отетить, что описанный выше способ не являтся оптимальным с точки зрения производительности, но на небольших массивах ето не является существенным.


