---
title: "Интересная особенность Enum"
date: 2009-07-17T13:45:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [.net framework]
archives: [2009]
aliases:
    - post/One-interesting-Enum-feature.aspx
---


> Те, кто знает на память книгу Дж.Рихтера C# via .NET, в этом врядли найдут для себя что-то новое/интересное.

>  

 Всё началось с того, что было у меня два похожих enum'ов (к примеру Numbers и BigNumbers) и нужно было как-то переменные первого типа приводить к другом, и наоборот. 

> ** enum Numbers**

> **     {**

> **         One,**

> **         Two,**

> **         Three**

> **     }**

> **<br /> **

> **     enum BigNumbers**

> **     {**

> **         One,**

> **         Two,**

> **         Three,**

> **         Four,**

> **         Five**

> **     }**

На практике такие преобразования выглядят примерно так :

> ** Numbers n1 = Numbers.One;**

> ** Numbers n2 = (Numbers) 2;**

> ** Int32 i1 = (Int32) n1;**

> **<br /> **

> ** BigNumbers b1 = BigNumbers.Five;**

> **<br /> **

> ** Numbers n3 = (Numbers) b1;**

> **<br /> **

> ** Console.WriteLine(String.Format("n1 = {0}", n1));**

> ** Console.WriteLine(String.Format("n2 = {0}", n2));**

> ** Console.WriteLine(String.Format("i1 = {0}", i1));**

> ** Console.WriteLine(String.Format("b1 = {0}", b1));**

> ** Console.WriteLine(String.Format("n3 = {0}", n3));**

>  

В результате на экране мы получим следующее:

> ** n1 = One<br /> n2 = Three<br /> i1 = 0<br /> b1 = Five<br /> n3 = 4 **

  Здесь мы видим, что n3 теперь равняется 4-м. Логичный, но не совсем ожидаемый для меня результат. В таком случае хотелось бы получить какой-то Exception.

 Теперь разберёмся что представляет собой enum и почему он так работает.

Enum (перечесляемый тим, enumerated type) предоставляет нам возможность хранить пару имя-значение и пришли в дополнение к константом (например: вместо того, чтоб в методе возвращать код ошибки, можно создать enum с именами ошибок).  По сути, System.Enum представляет обёкт размерного (value) типа, пронаследованного от System.ValueType:

> **  ****public abstract class Enum : ValueType, IComparable, IFormattable, IConvertible**<br />

<br />И, по умолчию, запись  "enum Numbers" соответствует "enum Numbers : int". В этом можно убедится, посмотрев на наше приложение с помощью IL DASM, который входит в комплект поставки .NET Framework SDK.

> ** .class private auto ansi sealed Enums.Numbers       extends [mscorlib]System.Enum{} // end of class Enums.Numbers<br /> .field public static literal valuetype Enums.Numbers One = int32(0x00000000)**<br />

 <br />Таким образом мы видим, что все элементы нашего enum являются целыми числами (int). Вместо int, можно указать byte, sbyte, short, ushort, int, long, и ulong. Интересно что если указать имя типа так, как они именуются в FCL (Byte, Int32 и т.д.), то мы получим ошибку: <br />** Type byte, sbyte, short, ushort, int, uint, long, or ulong expected**<br /> <br /> <br />Вернёмся к нашему примеру. Чтоб в нём всё работало так, как ожидалось, достаточно добавить такой код:

>  **if (!Enum.IsDefined(typeof(Numbers), b1)){throw new ArgumentException();}**

 

[Enums.zip (3.01 kb)](/file.axd?file=Enums.zip)

