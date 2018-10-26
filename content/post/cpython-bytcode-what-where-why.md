---
title: "CPython: bytecode -  что, где, зачем?"
date: 2012-04-03T10:28:00+03:00
draft: False
category: [Python]
tags: []
archives: [2012]
aliases:
    - post/cpython-bytcode-what-where-why.aspx
---



<p>Хотя python и является интерпретируемым языком программирования, но все-же какае-то компиляция в нем есть. Это не такая компиляция, которую многие привыкли в C/C++. Скорее это нечно похожее на JVM (java virtual machine) и CLR (Common Language Runtime). 

Это компиляция в bytecode - низкоуровневый платформонезависимый язык, который выполняется внутри Python Virtual Machine (PVM). Более полное и официалное определение с сайта python.org:

**Python source code is compiled into bytecode, the internal representation of a Python program in the CPython interpreter. The bytecode is also cached in .pyc and .pyo files so that executing the same file is faster the second time (recompilation from source to bytecode can be avoided). This “intermediate language” is said to run on a virtual machine that executes the machine code corresponding to each bytecode. Do note that bytecodes are not expected to work between different Python virtual machines, nor to be stable between Python releases.**

Работает это так:

При первой загрузке модуля интерпритатор python (имеется в виду реализация CPython) парсит исходный код и компилирует его в bytecode, который размещает в файле .pyc (compiled python source) рядом с исходным файлом. При следующей загрузки модуля интерпритатор ищет pyc-файл и если нахотит, то сравнивает его время создания с py-файлом. Если время последнего меньше, чем время создания pyc-файла, то повторная “компиляция” не происходит. На самом деле время создания лишь один из критериев, но он, как правило, является решающим. К примеру в Python 2.7 так же сравнивается атрибут co_filename. Таким образом уменьшается время на загрузку модуля. Стоит отметить, что время выполнения кода остается таким же, т.к. он исполняется на той же PVM, что и первый раз. Из этого свойста не совсем явно вытекеает другое - для загрузки модулей нужны только pyc-файл, исходники в виде py-файлов не обязательны. Рассмотрим это на простом примере:

Я создал два очень простых файла. world.py:

**def hello():<br />    print ‘hello’**

И hello.py:

**from world import hello<br />hello()**

При первом запуске командой “$ python hello.py”, который произойдет немного медленнее интерпритатор создаст pyc-файл. Теперь “выполнение” (время выполнения кода осталось прежним, но время запуска уменьшилось, что в данном примере играет большую роль, в более сложных и реальных ситуациях время загрузки модуля зачастую чем время выполнения кода) этих скриптов занимает меньше времени. 

Идем дальше. Удаляем world.py и запускаем все ту же команду “$ python hello.py”. Результат оказался неизменным - на экран напечаталась слово ‘hello’. Такой жке результат получаем и при изменении файла hello.py. 

Особенности pyc-файлов заключаются в том, что они являются платформо-независимые, из-за чего их можно распространять вместо исходников своего приложения. Должно лишь соблюдаться одно условие - одна и та же версия PVM (CPython) как для компиляции, так и для запуска.

Внимательые читатели должны были заметить, что упоминались так же pyo-файлы. Для получения их необходимо передать интерпритатору опцию -O или -OO. Первая немного оптимизирует код путем удаления инструкций, необходимых для дебага (assert  и т.е.) (из python --help: -O     : optimize generated bytecode slightly). Вторая добавляет к такой оптимизации так же и удаления docstring-ов, что позволяет имень меньший размер “скомпилированного” файла.

И в завершении несколько копеек о распространении приложения в виде pyc/pyo-файлов. Хотя это и можно, но лично я не встречал такого пока, не считая разных вариция на тему py2exe. Если верить гуглу, то при запуске и развертывании таких прихожений часто возникают проблемы. В основном из-за версии CPython и, наверное всеми нелюбимого, случая с неправильной датой/временем/часовым поясом.  Также стоит отметить, что при установки пакета с помощью setup.py, pyc-файлы генерируются в момент установки. При создании RPM в с помощью setup.py также гененрируются эти файлы и кладутся внутрь RPM.

 

Несколько ссылок по теме:

модуль для компиляции в bytecode: [http://docs.python.org/library/compileall.html](http://docs.python.org/library/compileall.html)

ну и куда же без disassempler’а [http://docs.python.org/library/dis.html](http://docs.python.org/library/dis.html)?
