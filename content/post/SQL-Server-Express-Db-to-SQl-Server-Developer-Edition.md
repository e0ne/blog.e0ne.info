---
title: "Подключаем базу от SQL Server Express к SQL Server Developer Edition"
date: 2009-02-06T16:32:00+03:00
draft: False
category: [.NET Framework]
tags: [sql server,sql server express]
archives: [2009]
aliases:
    - post/SQL-Server-Express-Db-to-SQl-Server-Developer-Edition.aspx
---



SQL Server Express хоть и бесплатен, но обладает некоторыми недостатками. Мне кажется для разработчика один из главных - это то, что он не соответствеут боевым условиям. Ведь мало кто использует Express версию в production. Поэтому разработчики часто ставят SQL Server Developer Edition (опустим вопрос о лицензировании). Вот только тут появляются новые проблемы: скачал новый starter kit, а он в качестве СУБД использует SQL Server Expres. Не ставить же его из-за этого? Хотя можно и поставить...  Но я для себя выбрал другой путь: подключить эту базу к полноценному MS SQL серверу.



 Что мы имеем:


	<li>Файлы базы данных: <br />
	Localization.mdf и Localization_log.ldf;</li>
	<li>Приложение, которое использует эту базу данных, подключаемую таким обрахом:<br />
	**connectionString="server=(local)\SQLExpress;AttachDbFileName=|DataDirectory|Localization.mdf;Integrated Security=true;User Instance=true".**</li>


Исправляем этот недостаток.



**Шаг 1.  **Подключаем базу к SQL Server Developer Edition (в примере я использую 2005-ю версию, но всё это работект и на SQL Server 2008).



 



<img src="/image.axd?picture=1.jpg" alt="" /><br />
<br />
Далее под полем "Databases to attach" нажимаем на кнопу Add и указываем свой файл Localization.mdf. Нажимаем ОК.



 



<img src="/image.axd?picture=2.jpg" alt="" /><br />
<br />
Теперь наша база данных подключена к SQL Server Developer Edition.



Также все вышесказанное можно сделать с помощю SQL скрипта:



 



**Шаг 2.** Меняем ConnectionString.


> 
	<p>
	**connectionString="Data Source=localhost;Initial Catalog=Localization;User ID=user;Password=password"**
	</p>



**Шаг 3.** Запускаем наше приложение.


