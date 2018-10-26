---
title: "Настройка PHP+Nginx для 'Hello, world'"
date: 2013-09-06T23:52:00+03:00
draft: False
category: [Web Development]
tags: [nginx,php]
archives: [2013]
aliases:
    - post/setup-PHP-Nginx-for-Hello-world.aspx
---


Иногда приходится делать удивительные и неожиданные для себя вещи. Например, писать что-то на PHP. Но написать мало - надо еще проверить что написанный код работает. В моем случае приложение было немного сложнее классического "hello, world", но все-равно требовалось проверить его работоспособность.

Т.к. это всего-лишь тестовая версия/PoC или что-то такое, интересовала самая простая схема его запуска. Apache не виртуалке c Ubuntu не стоял, под руку попал Nginx. Далее все происходило так:


<ul>
- установка необходимого пакета (PHP уже стоял): <br />**$ sudo apt-get install php5-fpm**<br />Не знаю насколько FastCGI хорош и применим в мире PHP, но мне подошел
- выключаем работу с unix socket и вешаем FastCGI процесс на локальный порт 9000; для этого правим конфигурационный файл "**/etc/php5/fpm/pool.d/www.conf**" следующим образом:<br />;listen = /var/run/php5-fpm.sock<br />listen = 127.0.0.1:9000
- настраиваем Nginx ("**/etc/nginx/sites-available/default**"):<br />location ~ \.php$ {<br />                try_files $uri =404;<br />                fastcgi_split_path_info ^(.+\.php)(/.+)$;<br />                fastcgi_pass 127.0.0.1:9000;<br />                fastcgi_index index.php;<br />                include fastcgi_params;<br />        }
- копируем нужный PHP-скрипт в директорию, на которую смотрит веб-сервер
- проверяем работу скрипта
</ul>
Все. Решение не претендует на правильность и полноту. Просто иногда **надо**.


