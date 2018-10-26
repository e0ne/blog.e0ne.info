---
title: "Байты, строки и кодировки"
date: 2009-10-16T15:18:00+03:00
draft: False
category: [.NET Framework]
tags: [encoding]
archives: [2009]
aliases:
    - post/bytes-symbols-and-encoding.aspx
---


 

> 		byte[]	byteArray = GetBytes();<br />		var retval = Encoding.ASCII.GetString(byteArray);

 

И что самое страшное в этом, так это то, что если байты представляют собой символы латинского алфавита, то, в большинстве случаев, всё будет замечательно работать. А когда работать оно перестаёт в содержимое строки примерно такое:

 

> 		"\u0000"\u0000a\u0000"\u0000:\u00002\u00000...." 

 

Тогда все начинают громко ругаться и рвать на себе волосы со словами: "Ну ведь работало же! Да и вот в этом([http://www.google.com.ua/search?rlz=1C1GGLS_enUA335US335&sourceid=chrome&ie=UTF-8&q=c%23+byte+array+to+string](http://www.google.com.ua/search?rlz=1C1GGLS_enUA335US335&sourceid=chrome&ie=UTF-8&q=c%23+byte+array+to+string)) примере так написано!".

Хорошо, если мысль о неправильной кодировке прийдёт сразу, а если нет... Сколько времени/нервов потритит разработчик, прежде чем всё станит на свои места?

вышеприведённый пример лучше заменить на:

> 		byte[]	byteArray = GetBytes();<br />		var retval = Encoding.Unicode.GetString(byteArray); 

Или даже на:

 

> 	byte[]	byteArray = GetBytes();

> 	var retval = Encoding.Default.GetString(byteArray); 

 

 

 

