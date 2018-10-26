---
title: "Интересная особенность конструкции foreach в языке C#"
date: 2011-02-09T11:15:00+03:00
draft: False
category: [.NET Framework]
tags: [c#,foreach,ienumerable]
archives: [2011]
aliases:
    - post/One-interetsing-feature-of-the-foreach-statement.aspx
---


При написании кода на языке C# достаточно часто приходится использовать конструкцию **foreach**. Ведь так на много удобнее проходить по коллекциям, по сравнению с использованием цикла **for**. Безусловно, у каждого метода есть свои плюсы и минусы и выбор всегда зависит от конкретной задачи и ситуации. Но на днях меня удивила одни интересная особенность конструкции **foreach**, а  именно то, как это работает.

Рассмотрим простой пример:

<img src="/image.axd?picture=2011%2f2%2fforeach.png" alt="" />

У нас есть некая коллекция элементов и с помощью **foreach **мы выводим на консоль имена всех элементов.

При этом класс **MyCollection **выглядит так:

<img src="/image.axd?picture=2011%2f2%2fcollection.png" alt="" />

Класс  коллекции реализовывает единственный метод **GetEnumerator **интерфейса ** IEnumerable **для возможности использования класса в  конструкции **foreach**.

<img src="/image.axd?picture=2011%2f2%2fGetEnumerator.png" alt="" />

Особенности **enumerator**’а нас сейчас не интересуют, будем считать что он работает так, как ему положено.

Теперь    сделаем простую вещь, а именно, поменяем наш класс **MyCollection **так,    чтобы он больше не реализовывал интерфейс **IEnumerable**, при этом метод    GetEnumerator оставим без изменений.

К моему удивлению, код и дальше продолжил компиляцию и правильно работал. Первым делом, посмотрим какой IL-код у нас получился:

<img src="/image.axd?picture=2011%2f2%2fil.png" alt="" />

Тут    хорошо видно, что при создании IL-кода компилятор не обращает   внимания   на наличие интерфейса **IEnumerable**, а непосредственно вызывает   метод ** GetEnumerator**. На этом моменте мне стало интересно и я пошел   читать   спецификацию языка C# ([Standard ECMA-334 C# Language   Specification](http://www.ecma-international.org/publications/standards/Ecma-334.htm)),     которая, к слову, датирована далёким июнем 2006-го года.  В разделе    8.18  Итераторы сказано следующее:

****The foreach statement is used to iterate over the elements of an enumerable collection. In order to be <br />enumerable, a collection shall have a parameterless GetEnumerator method that returns an enumerator. <br />Generally, enumerators are difficult to implement, but the task is significantly simplified with iterators.****

Таким     образом, получается что для использования коллекции в конструкции ** foreach **достаточно только метода **GetEnumerator**, а наличие интерфейса -     необязательное условие.<br /><br />Пример кода доступен по адресу: [https://github.com/e0ne/BlogSamples/tree/master/ForeachTest](https://github.com/e0ne/BlogSamples/tree/master/ForeachTest)

