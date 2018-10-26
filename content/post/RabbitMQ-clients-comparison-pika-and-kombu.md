---
title: "Сравнение библиотек pika и kombu на примере работы с RabbitMQ"
date: 2012-02-21T23:26:00+03:00
draft: False
category: [Python]
tags: [rabbitmq,pika,kombu,ampq]
archives: [2012]
aliases:
    - post/RabbitMQ-clients-comparison-pika-and-kombu.aspx
---


[RabbitMQ](http://www.rabbitmq.com/) - одна из реализаций сервера для обмена сообщениями на базе протокола AMPQ([http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol](http://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol), [http://amqp.org/](http://amqp.org/)). Подробно описывать его работу, достоинства и недостатки я сейчас не буду. Цель этого поста - сравнить две библиотеки для работы с ним с помощью Python. На самом деле, этих библиотек значительно больше, краткий список их доступен на сайте RabbitMQ: [http://www.rabbitmq.com/devtools.html#python-dev](http://www.rabbitmq.com/devtools.html#python-dev).

Сравнивал по принципу "нужно это, это и еще вооон то". Детальное описание фич на сайте - ниже только те, которые были критичные для меня.

[Pika](http://pypi.python.org/pypi/pika) - Python AMQP Client Library - изначально разрабатывалась для работы с RabbitMQ и предоставляет собой реализацию протокола [AMQP 0-9-1](http://www.rabbitmq.com/amqp-0-9-1-reference.html), в следствии чего, все примеры работы с RabbitMQ на Python в официальной документации написаны с использованием этой библиотеки.

[Kombu](http://packages.python.org/kombu/) известна тем, кто работал с OpenStack.

### Небольшая сравнительная таблица с комментариями:


<table border="0">
<tbody>
<tr>
|<br />
|pika
|kombu
</tr>
</tbody>
<tbody>
<tr>
|Репозиторий
|[https://github.com/pika/pika](https://github.com/pika/pika)
|[https://github.com/ask/kombu](https://github.com/ask/kombu)
</tr>
<tr>
|Дата последнего обновления
|19.02.2012
|21.02.2012
</tr>
<tr>
|Последняя версия
|0.9.6-pre0
|2.1.0
</tr>
<tr>
|Лицензия
|MPL 1.1 / GLP 2
|BSD License / As is
</tr>
<tr>
|Подход к написанию кода
|простой и понятный код
|явно прослеживается [Publish–subscribe pattern](http://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern)
</tr>
<tr>
|Поддержка SSL
|+(последняя версия из репозитория)
|+(последняя версия из репозитория)
</tr>
<tr>
<td>
<p>Интеграция с Django из коробки<br />(есть документация и примеры)
|Интеграция с Django из коробки<br />(есть документация и примеры)|-|+
|Асинхронная работа|+|+
|Поддрежка Tornado/Twisted|+/+|-/-
|Кеширование из коробки|-|+
|Поддержка разных транспортов для очереди сообщений|ampq|amqplib<br />librabbitmq<br />pika<br />pika2<br />memory<br />redis<br />beanstalk<br />mongodb<br />couchdb<br />django (django models)
|Документация|+, примеры работы с RabbitMQ на сайте “кролика”|+, примеры кода более сложные, чем “hello world”

 

В целом, после незначительного использования обоих библиотек (читать как “написал “hello world”” и чтения документации пришел к таким выводам:

 

- для простых задач pika предпочтительнее, уровень вхождения ниже;
- kombu имеет больше всевозможных настроек и легче поддается расширению;
- производительность обоих библиотек на очереди до 100 сообщений была примерно одинакова.

 

 

Небольшой пример кода: [https://github.com/e0ne/BlogSamples/tree/master/rabbitmq-sample](https://github.com/e0ne/BlogSamples/tree/master/rabbitmq-sample)

 

P.S. Хочется посмотреть еще [celery](http://ask.github.com/celery/) и [py-ampqlib](http://barryp.org/software/py-amqplib/), но пока до них руки не дошли.

P.S.S. Комментарии, замечания и дополнения приветствуются.

 

