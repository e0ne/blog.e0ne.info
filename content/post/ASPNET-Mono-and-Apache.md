---
title: "ASP.NET + Mono + Apache"
date: 2009-09-22T01:23:00+03:00
draft: False
category: [Mono,Web Development]
tags: [asp.net,mono,linux,apache]
archives: [2009]
aliases:
    - post/ASPNET-Mono-and-Apache.aspx
---


Всё больше и больше можлно услышать о [Mono](http://go-mono.com/). Как изестно, основное его идеей является реализация действительно кроссплатформенной среды .NET. Таким образом, чеще всего Mono испльзуют в операционной системе, отличной от MS Windows. А если не Windows, то Linux или какой-то из Unix. И всё было бы хорошо, если б не 2 момента (в данном случае я не акцентрирую внимание на степень готовности реализации Mono: аналог WinForms и замена Internet Information Services (IIS).На за мену WinForms приходят GTK, QTи другие библиотеки. А вот с заменой IIS все не тах хорошо: либо Apache с соответствующими модуляли, либо "родной" для Mono веб-сервер XSP2. А так как Apache наиболее популярен, то будем пользоваться им.

Все примеры я буду приводить для Ubuntu linux, но для других nix-подобных ОС все будет делаться таким же способом, за исключением установки пакетов. 

Для начала нам все же надо установить Mono и IDE для нее. В качестве IDE  будем использовать MonoDevelop. Устанавливаем всё необходимое:

> 	**apt-get install mono-2.0-runtime mono-2.0-gac mono-2.0-service mono-2.0-devel mono-xsp2 mono-xsp2-base **	<br />	****	<br />

После чего можно запустить MonoDevelop, созать простое ASP.NET приложение и запустить. В результате получаем что-то похожее на это:

<img src="/image.axd?picture=blog.png" alt="" width="700" height="394" />

Теперь мы уже можем без проблем заниматься разработкой вплоть до момента, когда нужно запустить приложение на test-сервере, на которов, в качестве web-сервера, должен стоять Apache. Дело за малым - установить Apache и настроить его для работы с Mono.

Для наала, устанавливаем необходимы пакеты: 

> 	**sudo apt-get install apache2 mono-apache-server2 libapache2-mod-mono		**

 

Говорим веб-серверу о необходимости загрузки нового модуля:

> 	**sudo a2enmod mod_mono							**

И создаём новый конфиг (/etc/mono-server2/monotest.webapp) для нашего приложения:

> 	 	****<apps><br />	      <web-application><br />	         <name>Mono test</name><br />	         <vpath>/mono</vpath><br />	         <path>/var/www/</path><br />	        <vhost>localhost</vhost><br />	      </web-application><br />	</apps> 				<br />	****	<br />

Последние что нас осталось сделать - это подправить конфигурационный файл Apache'а для нашего сайта (/etc/mono-server2/mono-server2-hosts.conf). Добавляем в него такие строки: 

> 	**Alias /mono "/var/www"<br />	AddMonoApplications default "/mono:/var/www"<br />	          <Directory /var/www><br />	               SetHandler mono<br />	                    <IfModule mod_dir.c><br />	                          DirectoryIndex Default.aspx<br />	                    </IfModule><br />	    </Directory>**<br />

Перезагружаем Apache командой: 

> 	**sudo /etc/init.d/apache2 restart		**<br />	<br />

И смотрим в браузере что у нас получилось:

<img src="/image.axd?picture=mono.png" alt="" width="700" height="394" />

