---
title: "Network namespace - виртуальный сетевой стек в linux"
date: 2013-01-06T22:53:00+03:00
draft: False
category: [Linux]
tags: [networking]
archives: [2013]
aliases:
    - post/Network-namespace-virtual-network-stack-in-linux.aspx
---



<p style="text-align: right;">Почему-то, информации на тему “что такое network namespace” я практически не нашел, что в очередной раз доказыват: английский - основной язык для ИТ.

Почему-то, информации на тему “что такое network namespace” я практически не нашел, что в очередной раз доказыват: английский - основной язык для ИТ.

Network namespace - это логически отделенный от других стек сетевых протоколов в Linux. Такая себе контейнерная виртуализация для сетевых интервейсов, когда chroot LXC и нужна виртуализация только сетевых интерфейсов. Эмулируется полностью сетевой стек: сетевые интерфейсы, таблица маршрутизации, файрволл и т.д. Так, как это работает на уровне ядра и для определенных процессов, то вполне можно получить рабочую конфигурации, когда на одной машине есть несколько сетевых интерфейсов с одинаковыми IP-адресами и ничто не конфликтует. 

Их поддержка в виде патчей появилась еще в версии 2.6.20 (из коробки в дистрибутивах было замечено мной только начиная с 2.6.32) ядра Linux, а в 3-й ветке стали доступы из коробки. Также для работы с ними необходима утилита iproute2. Полный список дистрибутивов и поддерживаемых ядер можно наяти по ссылке [http://code.google.com/p/coreemu/wiki/NamespaceKernels](http://code.google.com/p/coreemu/wiki/NamespaceKernels). От себя добавлю, что с Ubuntu 12.04/12.10 проблем не было, а вот на RHEL 6.3 и, основанной на нем, CentOS 6.3 поддержки network namespaces нету на уровне ядра. Сростой способ проверки - посмотреть наличие директории **/proc/self/ns/**. 

Основные действия с ними можно выполнять с помощью команды ip netns (ip netns - process network namespace management):


<ul style="text-align: left;">
- **ip netns list** - посмотреть все network namespaces
- **ip netns add NAME** - создать новый network namespace
- **ip netns delete NAME** - удалить network namespace
- **ip netns exec NAME cmd** - выполнить команду внутри network namespace
</ul>


При запуске любого процесса с определенным network namespace у него в **/proc/ID/ns/** будут данные о данном неймспейсе, что поможет ядру правильно подставить сетевой стек. Также все network namespace можно будет найти в **/var/run/netns/ns_name** в виде обычных файлов. Пока файловые дескрипторы этих файлов открыты, считается, что network namespacе работает. Если создать файлы **/etc/netns/ns_name/{resolv.conf, hosts, ...}**, то ip-netns будет подставлять процессам именно эти файлы, а не системные, что очень удобно для отладки и не только.

Чтобы посмотреть в каком network namespace выполняется нужный процесс достаточно посмотреть содержимое директории **/proc/proc_id/ns/**.

Разные network namespace можно объединять между собой с помощью виртуальных сетевых интерфейсов (veth).

Для того, что бы добавить уже существующий сетевой интерфейс (физический или виртуальный) достаточно выполнить команду:

**ip link set eth1 netns samplens**

По умолчанию, все сетевые процессы находятся в так называемом initial network namespace, у которого нет имени :). Но все конманды для работы с network namespace кроме имени, в качестве параметров, могут принимать ID процесса, который управляет неймспейсом. Для initial network namespace ID равен 1, что равнозначно ID init процесса. Таким образовом, чтобы обрать интерфейс из неймспейса, его стоит добавить в неймспейс с ID=1:

**ip link set eth1 netns 1**

 

Дополнительные ссылке по теме:


<ul>
- [http://manpages.ubuntu.com/manpages/precise/man8/ip.8.html#contenttoc15](http://manpages.ubuntu.com/manpages/precise/man8/ip.8.html#contenttoc15)
- [http://manpages.ubuntu.com/manpages/precise/man2/setns.2.html](http://manpages.ubuntu.com/manpages/precise/man2/setns.2.html)
- [http://stuff.onse.fi/man?program=ip-netns&section=8](http://stuff.onse.fi/man?program=ip-netns&section=8)
- [http://code.google.com/p/coreemu/wiki/NamespaceKernels](http://code.google.com/p/coreemu/wiki/NamespaceKernels)
- [http://lwn.net/Articles/219794/](http://lwn.net/Articles/219794/)
- [http://lwn.net/Articles/219597/](http://lwn.net/Articles/219597/)
- [http://www.opennet.ru/tips/info/2683.shtml](http://www.opennet.ru/tips/info/2683.shtml)
</ul>


 

P.S. При виртуализации сетевых интерфейсов не могу не упомянуть про tun/tap устройста ([http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/tuntap.txt](http://www.kernel.org/pub/linux/kernel/people/marcelo/linux-2.4/Documentation/networking/tuntap.txt), [http://backreference.org/2010/03/26/tuntap-interface-tutorial/](http://backreference.org/2010/03/26/tuntap-interface-tutorial/)). Что это такое я уже крато писал в одном из предыдущих постов. Сам подход, что они реализовываются через файловые дескрипторы(файлы), существует и по сей день. В Linux - почти все файлы, и сетевые интерфейсы не исключение :)

