---
title: "Установка компилятора gcc на Mac OS Lion"
date: 2011-10-28T14:47:00+03:00
draft: False
category: [Python]
tags: [python,mac os,gcc]
archives: [2011]
aliases:
    - post/Install-gcc-on-Mac-OS-Lion.aspx
---


При установке пакетов psycopg2 и lxml easy_install радостно падал с криками:

 

unable to execute gcc-4.2: No such file or directory<br />error: command 'gcc-4.2' failed with exit status 1

 

Вполне логично, т.к. gcc у меня не стоял :(. Странно только что в Snow Leopard все работало. Немного полазив по инету нашел, что gcc ставится вместе с XCode, который ставится бесплатно из Mac App Store. Но и это не сразу помогло. Ниже привожу список шагов, которые понадобились для установки gcc и psycopg2 после этого.

 

1. Из Mac App Store устанавливаем XCode.
1. Добавляем в переменную PATH путь к gcc: export PATH=$PATH:/Developer/usr/bin
1. Чтобы работало после перезагрузки и для всех пользователей прописываем этот путь и в /etc/paths

 

