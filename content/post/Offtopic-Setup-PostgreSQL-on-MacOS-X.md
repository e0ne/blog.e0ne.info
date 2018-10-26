---
title: "[Offtopic] Установка PostgreSQL на MacOS X или ностальгия по MS DOS"
date: 2009-12-10T23:25:00+03:00
draft: False
category: [Offtopic]
tags: [postgresql,mac os,dos]
archives: [2009]
aliases:
    - post/Offtopic-Setup-PostgreSQL-on-MacOS-X.aspx
---


Первая попытка установить PostgreSQL на MacOS X потерпела крах. Пошел читать **readme**:

<img src="/image.axd?picture=2009%2f12%2fScreen+shot+2009-12-10+at+08.03.39.png" alt="" />

 

Вспомнились танцы с бубном в MS Dos, чтоб тот увидел больше 640К оперативной памяти, работа с extension memory (привет Паскалю). А чего стоит знаменитая фраза одного известного всем человека, о том, что нам таки хватит 640К ОЗУ. А ностальгия скорее не о ДОСе, а о том, как раньше писал код (некоторые и сейчас так пишут): оптимизировали память так, чтоб лишнего байта не занимало. А как доставалось тогда Windows'у? Лишние лишние файлы, процессы, записи в реестре дезжалостно удалялись для прибавления 1-2 мегабайт свободной оперативной памяти и нескольких десятков мег на винте. А сейчас словил OutOfMemoryException, когда процесс IIS'а в виртуалке начал есть более одного гига... Завтра буду искать memory leaks...

 

P.S. Интересный пост в тему DOS & .NET [http://www.codeproject.com/KB/cs/ExpressionCompiler86.aspx](http://www.codeproject.com/KB/cs/ExpressionCompiler86.aspx)

