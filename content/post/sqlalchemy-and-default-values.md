---
title: "SQLAlchemy и значения по умолчанию"
date: 2014-02-23T23:55:00+03:00
draft: False
category: [Python]
tags: [sqlalchemy]
archives: [2014]
aliases:
    - post/sqlalchemy-and-default-values.aspx
---


Проблема пришла от туда, от куда не ждали. А именно от таких 5-ти строчек кода:

**class CustomModel(Base):<br />    __tablename__ = 'custom_model'<br />    id = Column(Integer,)<br />    name = Unicode(100)<br />    datetime = Column(DateTime, default=datetime.now())**

Когда-то давно я или неправильно понял доку, недочитал или прочитал не то, но был уверен в том, что этот код “компилируется” в примерно такой SQL (код приведен только в целях примера и может не работать:) ):

**CREATE TABLE custom_model (<br />     id integer,<br />     name varchar(20),<br />    created_at datetime default getdate().now<br />)**

Проблема проявилась в том, что order by по полю created_at не работал. Все дело в том, что вышеприведенный код генерируется в такой SQL:

**CREATE TABLE test (<br />     id integer,<br />     name varchar(20),<br />     created_at<br />)**

Т.е. значение по умолчанию выставляются не на уровно СУБД, а на уровне модели при вставке. Более того, код “**default=datetime.now()**” отрабатывает только раз при создании модели и все значения будут одинаковыми. Для исправления этого достаточно сделать что бы значение по умолчанию вычислялось каждый раз новое. Для этого в параметр default можно передать любой callable объект, например lambda-функцию (**default=lambda: datetime.now()**). Если копнуть дальше в исходники, что значение default - это инстанс типа **ColumnDefault**, спрятанный за удобным синтаксисмом.

Что бы значения по умолчанию выставлялись на уровне СУБД в SQLAlchemy необходимо использовать параметр server_default (к слову, onupdate и другие триггеры на сервере ставятся с помощью добавления префикса “server_”, например server_onupdate). Если необходимо в качестве значения по умолчанию задать какое-то выражение (sql expression), то делается это с помощью следующей конструкции:

server_default=text("sysdate")

К слову о  Django - там все работает так же, только про server_default я ничего не нашел:(.

Ссылки по теме:

 

- [http://docs.sqlalchemy.org/en/latest/core/defaults.html#server-side-defaults](http://docs.sqlalchemy.org/en/latest/core/defaults.html#server-side-defaults)
- [https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/sql/schema.py#L1764](https://github.com/zzzeek/sqlalchemy/blob/master/lib/sqlalchemy/sql/schema.py#L1764)
- [https://docs.djangoproject.com/en/dev/ref/models/fields/#default](https://docs.djangoproject.com/en/dev/ref/models/fields/#default)

 

