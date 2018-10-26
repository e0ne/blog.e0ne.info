---
title: "OpenStack + RHEL + iptables = buffer overflow detected"
date: 2011-12-30T02:42:00+03:00
draft: False
category: [Offtopic,Python]
tags: [openstack,opensource,rhel,linux,iptables]
archives: [2011]
aliases:
    - post/OpenStack-and-RHEL-and-iptables-and-buffer-overflow-detected.aspx
---


 

**Никогда не знаешь, где упадет OpenStack(c) **<br />Я, в процессе очередного дебагга.

Те, кто читает мой твиттер ([@e0ne](http://twitter.com/e0ne)), должны знать, что в последнее время я работаю с [OpenStack](http://openstack.org)’ом, а именно занимаюсь(конечно, не один я) попытками его запуска на Red Hat Enterprise Linux (RHEL), CentOS, Scientific Linux, etc. Т.к. все это построено на базе полной и непросветной enterpise в виде RHEL, то сборка нового дистрибутива, как правило, у меня начинается со сборки именно под эту ОС. 

Вот я и хочу поделиться своими впечатлениями от сборки последней версии OpenStack’а под RHEL. Началось все с попытки запустить чуть менее чем полностью поломанную версию essex-1. Потом все продолжилось с версией essex-2. Основные моменты, которые мешали мне радоваться жизни - переделки в glance, связанные и security, которые на время поломали работоспособность EC2 API. 

Проект Glance - это услуги по отбору, регистрации и поиску виртуальных «machine images» (VMI). В рамках Glance используется RESTful API, что позволяет делать запрос метаданных VMI и выполнять поиск фактического образа (VMI). ([http://openstack.ru/openstack_glance.html](http://openstack.ru/openstack_glance.html))

И тут я решил попробовать запустить все из последней версии исходников, с master’а...

После небольших усилий инстансы (виртуалки) начали запускаться, но были проблемы с сетью. Команда “**killall dnsmasq**”, подсказанная моим коллегой, решила часть проблем, а именно - выдачу IP адреса виртуальной машине. Далее в логах при загрузке неворуженым глазом были замечены такие проблемы:

<img src="/image.axd?picture=2011%2f12%2fmetadata_error.png" alt="" />

 

Что означало, что запущенный инстанс не может получить данный от [Metadata Server’а](https://blueprints.launchpad.net/nova/+spec/openstack-api-metadata). Т.к. Metadata Server нормально работал в [Diablo](http://wiki.openstack.org/ReleaseNotes/Diablo), то сразу вспомнились 2 вещи:

 

- файл nova-api-metadata, который помешал успешно собрать RPM с essex-2 используя [spec-файл](http://www.rpm.org/max-rpm/ch-rpm-inside.html) из Diablo
- и то, что в essex-2 Metadata Server теперь существует отдельно от Nova API ([http://fnords.wordpress.com/2011/12/20/ending-the-year-well-openstack-essex-2-milestone/](http://fnords.wordpress.com/2011/12/20/ending-the-year-well-openstack-essex-2-milestone/), [https://blueprints.launchpad.net/nova/+spec/separate-nova-metadata](https://blueprints.launchpad.net/nova/+spec/separate-nova-metadata)).

 

Далее по аналогии с Nova API был создан файл /etc/init.d/openstack-nova-api-metadata, который предназначался для запуске сервиса Metadata Server’а. Metadata Server, на первый взгляд, успешно запустился, то я попытался запустить снова инстанс, что мне привело к предыдущей ошибке. Логи Metadata Server’а немного испугали:

<img src="/image.axd?picture=2011%2f12%2fiptables_error.png" alt="" />

 

Мозг сразу начал представлять кошмары, связанные с выводом [strace](http://en.wikipedia.org/wiki/Strace), linux kernel debugger’ом и так далее. Вовремя опомнившись, я полез в Google. Поиск по “**exit code 134**” ничего полезного не дал. А вот поиск по “**iptables-restore buffer overflow**” дал нужный результат в виде двух багов iptables: [http://bugzilla.netfilter.org/show_bug.cgi?id=641](http://bugzilla.netfilter.org/show_bug.cgi?id=641) и[https://bugzilla.redhat.com/show_bug.cgi?id=545600](https://bugzilla.redhat.com/show_bug.cgi?id=545600). Довольно-таки стандартное, на сколько мне известно, переполнение буфера, вызванное функцией strcpy, которую, к слову, не очень-то и рекомендуют использовать. Подробности в этом комментарии: [https://bugzilla.redhat.com/show_bug.cgi?id=545600#c6](https://bugzilla.redhat.com/show_bug.cgi?id=545600#c6)

 

<img src="/image.axd?picture=2011%2f12%2fiptables_version.png" alt="" />

 

Т.к. обновление iptables в RHEL 6.1 - не самая приоритетная для меня задача, то я решил зайти с другой стороны - посмотреть что же делает OpenStack для получения такого результата.

 

<img src="/image.axd?picture=2011%2f12%2fmd1.png" alt="" />

 

[https://github.com/openstack/nova/blob/master/bin/nova-api-metadata](https://github.com/openstack/nova/blob/master/bin/nova-api-metadata)

Metadata Server запускается таким же способом, как и другие REST-сервисы Nova, поэтому проблему нужно было искать где-то дальше. Об этом же говорили и логи, и ошибка, связанная с iptables.

[https://github.com/openstack/nova/blob/master/nova/network/linux_net.py](https://github.com/openstack/nova/blob/master/nova/network/linux_net.py)

<img src="/image.axd?picture=2011%2f12%2fmd2.png" alt="" />

 

Метод **metadata_accept()** отрабатывает без ошибок и падает все в **iptables_manager.apply()**.

<img src="/image.axd?picture=2011%2f12%2fmd3.png" alt="" />

 

Т.к. данный метод используется далеко не в одном месте

 

<img src="/image.axd?picture=2011%2f12%2fmd4.png" alt="" />

 

то ошибка где-то в передаваемых параметрах. В качестве параметров к **iptables-restore** у меня передавалось такое:

 ip-restore-full.jpg

 

<img src="/image.axd?picture=2011%2f12%2fip-restore-full.png" alt="" />

 

Зная о баге в iptables и то, что падало все только при запуске Metadata Server’а, то получилось быстро найти нужную команду, которая все ломала:

**iptables-restore <<EOF<br />*nat<br />:nova-api-metadata-POSTROUTING - [0:0]<br />-A POSTROUTING -j nova-api-metadata-POSTROUTING<br />COMMIT<br />EOF**

len(‘nova-api-metadata-POSTROUTING’)==29, что вместе с символом конца строки в языке С давало нам 30 символов и при копировании их в массив из 29 символов давало нам переполнение буффера (см. ссылки на баги выше). Хорошо, проблема найдена, теперь нужно ее устранить. Для этого находим код, где у нас генерируется имя chain’а:

chain1.jpg, chain2.jpg

<img src="/image.axd?picture=2011%2f12%2fchain1.png" alt="" />

<img src="/image.axd?picture=2011%2f12%2fchain2.png" alt="" />

 

где:

**binary_name = os.path.basename(inspect.stack()[-1][1])**

Таким образом проблема была в имени исполняемого файла. Переименовав “**/usr/bin/nova-api-metadata**” в “**/usr/bin/nova-metadata **” все заработало. Вопрос лишь в том, насколько долго оно будет работать с таким “фиксом”? 

Более правильное решение нужно делать исправляя код OpenStack’а и/или обновляя iptables. Также интересно как это себя ведет на других RHEL-based дистрибутивах(версия iptables) и ubuntu, но это уже проверю завтра, а пока поставил качаться нужные образы дистрибутивов...

### [Update]

Баг с iptables проверен после установки чистой ОС после установки всех апдейтов с помощью команды "**yum update**" на следующих ОС:

- RHEL 6.1 x86_64 - iptables v1.4.7, buffer overflow detected
- RHEL 6.2 x86_64 - iptables v1.4.7, buffer overflow detected
- CentOS 6.1 x86_64 - iptables v1.4.7 buffer overflow detected
- CentOS 6.2 x86_64 - iptables v1.4.7 buffer overflow detected
- Scientific Linux 6.1 x86_64 - iptables v1.4.7 buffer overflow detected
- Fedora 15 x86_64 - testing in process
- Fedora 16 x86_64 - testing in process

 

