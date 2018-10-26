---
title: "А вы говорите индусский код..."
date: 2009-08-31T16:47:00+03:00
draft: False
category: [.NET Framework]
tags: []
archives: [2009]
aliases:
    - post/bad-usa-code.aspx
---


internal class LinqConnection: BaseDatabaseConnection<br />{<br />

   /// <summary><br />   /// Should never be called<br />   /// </summary><br />   internal LinqConnection()<br />   {<br />       throw new Exception();<br />   }<br />   ...

} 

 

Написали программисты из США. И это ещё далеко не самый плохой кусок кода в проекте....

