---
title: "Избавляемся от ошибки socket.error: [Errno 98] Address already in use в python"
date: 2012-02-08T13:45:00+03:00
draft: False
category: [Python]
tags: [python,socket,server,error,exception]
archives: [2012]
aliases:
    - post/socket-error-Errno-98-Address-already-in-use-in-python.aspx
---


 

Время от времени, при разработке очередного API, которое работает поверх HTTP или создается Socket-сервер после остановки и попытки запуска сервера получаю ошибку:

**socket.error: [Errno 98] Address already in use**

Проблема заключается в том, что при аварийном (Ctrl+Z) завершении сервера в операционной системе остается запущенным процесс, который слушает нужный мне порт. В разных ОС время жизни такого процесса разное: в RHEL это около двух минут, в Ubuntu - больше. 

Решение достаточно простое. Т.к. при нажатии клавиш Ctrl+Z процесс получает команду “keyboard interrupt”, то достаточно обработать нужное исключение и корректно завершить процесс:

 

<img src="/image.axd?picture=2012%2f2%2ftry-except.png" alt="" />

 

Надеюсь теперь не буду забывать писать нужный try-except...

 

Пример кода на GitHub: [https://github.com/e0ne/BlogSamples/tree/master/SocketError](https://github.com/e0ne/BlogSamples/tree/master/SocketError). Для его запуска необходимо наличие утановленного пакета SOAPPy.

