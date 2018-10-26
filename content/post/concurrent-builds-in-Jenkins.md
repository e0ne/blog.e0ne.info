---
title: "Параллельные билды в Jenkins"
date: 2013-11-15T14:16:00+03:00
draft: False
category: []
tags: [ci,jenkins]
archives: [2013]
aliases:
    - post/concurrent-builds-in-Jenkins.aspx
---


Разберем ситуацию, ставшую достаточно распространенной в наше время. Есть распределенная команда, допустим в двух городах (А и Б), которая работает над одним крупным проектом. Сборка проекта происходит на Jenkins’е в городе А и длится, например 3 минут. Скачать готовый продукт из города А в город Б можно в среднем за 30 минут (в зависимости от времени суток, загрузки канала, фазы луны и т.д.). Итого: команде из города Б нужно ждать час(60 минут) чтобы запустить/протестировать свежий билд. Очевидно, это достаточно много. Нужно ускорять.

Рассматривать вопросы вынесения этого всего (CI) в облако и прочее я не буду по двум причинам:

 

- это не всегда возможно
- и все-равно скачивать готовый билд приходится долго, только уже двум командам.

 

Также я пропущу вопросы синхронизации репозиториев с исходниками и прочие инфраструктурные вещи, не относящиеся к данной теме.

Решать данную проблему буду так: в обоих офисах настраивается Jenkins-нода, на которой можно собирать свежий билд. Главная задача - 2 одновременных билда одного проекта в разных офисах.

Делается это, примерно, так:

 

1. Заходим на наш Jenkins и устанавливаем нужные плагины (Jenkins => Manage Jenkins =>  Manage Plugins => Available). Нам нужен “Throttle Concurrent Builds Plugin” ([https://wiki.jenkins-ci.org/display/JENKINS/Throttle+Concurrent+Builds+Plugin](https://wiki.jenkins-ci.org/display/JENKINS/Throttle+Concurrent+Builds+Plugin)) и NodeLabel Parameter Plugin ([https://wiki.jenkins-ci.org/display/JENKINS/NodeLabel+Parameter+Plugin](https://wiki.jenkins-ci.org/display/JENKINS/NodeLabel+Parameter+Plugin)).
1. Настраиваем Slave node. Документация лежит тут: [https://wiki.jenkins-ci.org/display/JENKINS/Step+by+step+guide+to+set+up+master+and+slave+machines](https://wiki.jenkins-ci.org/display/JENKINS/Step+by+step+guide+to+set+up+master+and+slave+machines).
<li>Настраиваем нашу Job’у для параллельного выполнения на двух нодах. Я для примера создал Fake-long-job, которая выполняет простой bash-скрипт “sleep 20;”.        
<ul>
1. Отмечаем флаг “This build is parameterized”
<li>Добавляем параметр Node
<img src="/image.axd?picture=2013%2f11%2fnode-param.png" alt="" style="width:50%" />
</li>
<li>Выбираем на каких нодах можно выполнять билд
<img src="/image.axd?picture=2013%2f11%2fnodes.png" alt="" style="width:50%" />
</li>
<li>Настраиваем одновременные билды. В моем случае их может быть 2, по одному на каждой ноде
<img src="/image.axd?picture=2013%2f11%2fconcurrent.png" alt="" style="width:50%" />
.</li>
1. Нажимаем кнопку Save.
</ul>
</li>
<li>Проверяем, что все работает, запустив два билда на разных нодах.
<img src="/image.axd?picture=2013%2f11%2fbuilds.png" alt="" style="width:50%" />
</li>

 

Выше я описал только базовые настройки, которые подошли мне. Вам, возможно, прийдется дополнительно настраивать что либо еще.

