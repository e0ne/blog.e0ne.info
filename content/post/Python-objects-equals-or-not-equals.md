---
title: "Объекты в Python: equals or not equals"
date: 2011-12-22T15:15:00+03:00
draft: False
category: [Python]
tags: []
archives: [2011]
aliases:
    - post/Python-objects-equals-or-not-equals.aspx
---


 

Рассмотрим задачу сравнения двух инстансов простого класса A в Python. Сам класс A выглядит так:

**class A(object):<br />    def __init__(self, int_param):<br />        self.int_value = int_param**

В данном случае, если мы выполним такой код:

**a1 = A(1)<br />a2 = A(1)**

то инстансы этого классы не будут равны между собой:

**a1 == a2 - False<br />a1 is a2 - False**

Чтобы понять как это все работает и почему получается такой результат рассмотрим функцию [id(object)](http://docs.python.org/library/functions.html#id). Функция id() возвращает идентификатор объекта, который будет уникальным и неизменным на протяжении времени жизни объекта. В CPython эта функция возвращает адрес объекта в памяти. В моем случае это:

**id(a1)=4299743824<br />id(a2)=4299743888**

Теперь, если мы посмотрим на документацию оператора [is](http://docs.python.org/reference/expressions.html#notin), то увидем, что он возвращает True, только в случае, если, в нашем случае a1 и a2, - один и тот же объект. В таком случае, если сделать a3=a1, то получим:

**a3 == a1 - True<br />a3 is a1 - True**

Оператор “==” сравнивает объекты с помощью метода [__cmp__](http://docs.python.org/reference/datamodel.html#object.__cmp__), который может возвращать одно из 3-х значений:

 

- -1  - в случае, когда один объект “меньше” (<) другого;
- 1  - в случае, когда один объект “больше” (>) другого;
- 0  - объекты равны (==).

 

 

Самая простая реализация этого метода выглядит так:

**class B(object):<br />    def __init__(self, int_param):<br />        self.int_value = int_param<br /><br />    def __cmp__(self, other):<br />        if self.int_value < other:<br />            return -1<br />        elif self.int_value > other:<br />            return 1<br />        else:<br />            return 0**

После этого получаем такой вывод:

**b1 = B()<br />b2 = B()<br />b1 == b2 - True<br />b1 is b2 - False**

Примеры кода, традиционно, на GitHub’e: [https://github.com/e0ne/BlogSamples/tree/master/PythonEquals](https://github.com/e0ne/BlogSamples/tree/master/PythonEquals)

 

