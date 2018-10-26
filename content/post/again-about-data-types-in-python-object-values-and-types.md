---
title: "Снова о типах данных в Python: объекты, значения и типы (object, values and types)"
date: 2014-01-10T23:05:00+03:00
draft: False
category: [Python]
tags: []
archives: [2014]
aliases:
    - post/again-about-data-types-in-python-object-values-and-types.aspx
---


Если коротко, то типы в Python делятся либо на встроенные и пользовательские, либо на mutable и immutable (сразу так и не подобрал подходящего перевода на русский язык). Ну а если немного подробнее, то как-то так:

Рассмотрим простой пример кода (здесь и далее примеры кода будут писаться и выполняться в ipython’е):

In [1]: a =** 1000<br />In [2]: a<br />Out[2]: 1000<br />In [3]: type(a)<br />Out[3]: int**

Здесь мы объявляем переменую создаем объект (object) a, со значением(value) 1000 типа(type) int. Объекты в python - это абстрация над данными. Поэтому любой объект содержит в себе идентификатор(identity), тип и значение. Идентификатор - это адрес объекта в памяти, который никогда не меняется. Но мы можем присвоить объекту новое значение, написав, следующий код:

In [4]: a =** 'hello'<br />In [5]: a<br />Out[5]: 'hello'<br />In [6]: type(a)<br />Out[6]: str**

Теперь мы присвоили объекту a новое значение типа string. За кулисами этого всего, интерпритатор сделал, примерно, такое: создал новый объект ‘hello’, и поменялл ссылку переменной a на новый объект в памяти. При этом старое значение 1000 все еще хранится в памяти и будет удалено сборщиком мусора, т.к. на него нет ни одной ссылки. Тоже самое происходит и присвоении переменной нового значений такого же типа:

**In [7]: b = 1000<br />In [8]: id(b)<br />Out[8]: 40235856<br />In [9]: b = 1001<br />In [10]: id(b)<br />Out[10]: 39189680**

Интересный эффект будет при использовании целых чисел в диапазоне от -5, до 256 - их id всегда будет одинаковый, т.к. для улучшения быстродействия интерпритатор при старте создает объекты с этими значениями.

Стандартные типы в CPython делятся на два типа: mutable и immutable. Mutable — это обекты, значения которых могут быть изменены(например, list), а immutable — это обекты, значения которых не может меняться (например, string). Но это не значит, что если у нас есть переменная immutable типа, то ее нельзя изменить. Например, с типом string все привыкли работать так:

**In [11]: text = 'Hello'<br />In [12]: text<br />Out[12]: 'Hello'<br />In [13]: text = 'Hello, World'<br />In [14]: text<br />Out[14]: 'Hello, World'**

Как мы видим, начение переменной text поменялось. На самом деле, при присвоении переменной text нового значения, в памяти создается новый объект, и переменная text начинает на него ссылаться. В этом легко убедится при помощи функции id - получить идентификатор до и после изменения переменной.

Mutable типы ведут себя так:<br />**In [15]: l = [1, 2, 3]<br />In [16]: l<br />Out[16]: [1, 2, 3]<br />In [17]: id(l)<br />Out[17]: 139901299808088<br />In [18]: l.append(4)<br />In [19]: l<br />Out[19]: [1, 2, 3, 4]<br />In [20]: id(l)<br />Out[20]: 139901299808088**

Основываясь на этом свойстве(и не только), ключами в словаре (dict) могут быть только immutable обекты:

In [21]: d = {'one': 1}**<br />In [22]: type(d)<br />Out[22]: dict<br />In [23]: d[1]=1<br />In [24]: d<br />Out[24]: {1: 1, 'one': 1}<br />In [25]: d[l] = 'list'<br />---------------------------------------------------------------------------<br />TypeError                                 Traceback (most recent call last)<br /><ipython-input-25-4f49b18d7af7> in <module>() ----> 1 d[l] = 'list'<br />TypeError: unhashable type: 'list'**

Immutable типы в Python — это числа(numbers), строки (strings) и кортежи (tuples).

Для облегчения привжу список некоторых всторенных типов (built-in types):

 

- Numbers (числа) — int, long, float, complex(3+4j), Decimal, Fraction
- Sequence Types (последовательности) — str, unicode, list, tuple, bytearray, buffer, xrange
- Sets — set, frozenset
- Maps (хеш-таблицы) — dict
- Files, context managers и другие.

 

Ссылки по теме:

- [http://docs.python.org/2/library/index.html](http://docs.python.org/2/library/index.html)
- [http://docs.python.org/2/library/datatypes.html](http://docs.python.org/2/library/datatypes.html)
- [http://docs.python.org/2/library/types.html](http://docs.python.org/2/library/types.html)
- [http://docs.python.org/2/library/stdtypes.html](http://docs.python.org/2/library/stdtypes.html)
- [http://docs.python.org/2/reference/datamodel.html](http://docs.python.org/2/reference/datamodel.html)
- [http://docs.python.org/2/c-api/int.html](http://docs.python.org/2/c-api/int.html)
- [http://blog.e0ne.info/post/Python-objects-equals-or-not-equals.aspx](http://blog.e0ne.info/post/Python-objects-equals-or-not-equals.aspx)

 

 

 

