---
title: "Сборка mod_security для nginx под Ubuntu"
date: 2014-01-08T22:02:00+03:00
draft: False
category: [Web Development]
tags: [nginx]
archives: [2014]
aliases:
    - post/compile-mod_security-for-nginx-and-Ubuntu.aspx
---


Всегда недолюбливал Apache из-за формата его конфига. Конфиг Nginx’а мне вседа было порще читать и писать. Да и статику им раздавать хорошо и быстро, поэтому от Apache я, по возможности, отказываюсь. Но частая проблема с nginx в том, что приходится собирать необходимые модули из исходников самому, со всемы вытикаюющими плюсами и минусами. И, как полагается любому популярному и быстро развивающемуся проекту, документация по сборке этих самих модулей не всегда полная и актуальная.

Ниже (очень) короткое изложение того, что мне пришлось сделать для сборки mod_security. Надеюсь, это сэкономит кому-то время и нервы.

Оффициальная документация расположена [тут](http://www.modsecurity.org/projects/modsecurity/nginx/) и [тут](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#wiki-Installation_for_NGINX). При этом сложилось впечатление, что на github’е она более актуальная и полная. По ним можно собрать все, при условии, что у вас уже стоят нужные пакеты. Мне понадобились:

**$ sudo apt-get install autoconf automake libtool libcurl4-openssl-dev**

Тажке, не забыть выполнить “**./autogen.sh**” перед “**./configure**”. Почему-то, в секции “Installation for NGINX” документации написаны только общие сведения. Мне, например, не хотелось и не нужно было собирать mod_security для apache, устанавливать пакет apache2-dev и т.д. Поэтому выполнил configure со следующими параметами:

**$ ./configure --prefix=/usr --disable-apache2-module --enable-standalone-module**

Далее сборка, установка и настройка у меня прошла без проблем.

