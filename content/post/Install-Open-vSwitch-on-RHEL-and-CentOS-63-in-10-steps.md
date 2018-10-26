---
title: "Установка Open vSwitch на RHEL/CentOS 6.3 в 10 шагов"
date: 2012-12-20T23:50:00+03:00
draft: False
category: [Linux]
tags: [rhel,centos,openvswitch]
archives: [2012]
aliases:
    - post/Install-Open-vSwitch-on-RHEL-and-CentOS-63-in-10-steps.aspx
---


 

Open vSwitch ([http://openvswitch.org/](http://openvswitch.org/)) - это виртуальный свитч, котороый позволяет вам строить виртуальную сеть (SDN) поддерживает различные протоколы для мониторнига и управления (NetFlow, sFlow, SPAN, RSPAN, CLI, LACP, 802.1ag и др). Приставка “open” означает что он является opensource продуктом со всеми вытекающими плюсами и минусами.  На просторах интернета найти документацию по нему и руководства по установки не проблема, если вы знаете английский язык. На русском практически ничего нет:(. Далее я расскажу процесс установки его с исходников на Red Hat Enterprise Linux 6.3 (RHEL) и основанной на базе него бесплатной CentOS 6.3 с ядром 2.6.32-279.el6.x86_64. 

В оффициальной документации Open vSwitch по установке на RHEL достаточно подробно написано как это сделать, но я столкнулся с некоторыми проблемами, о которых следует сказать отдельно.

!!! В примере для простоты делаю все операции от root’а, что категорически рекомендуется делать только в образовательных целях.

 

1. Устанавливаем нужные пакеты для сборки RPM:<br />**# yum install -y gcc gcc-c++ make rpm-build rpm-devel rpmdevtools git  make python-devel openssl-devel kernel-devel kernel-debug-devel<br /><br />**
1. Клонируем себе исходный код Open vSwitch:<br />**# git clone git://openvswitch.org/openvswitch openvswitch-1.9.90<br /><br />**
1. Создаем в домашней директории пользователя, от которого будем создавать RPM нужную структуру папок командой:<br /># rpmdev-setuptree<br />
1. Т.к. на помент написания этого поста последняя версия Open vSwitch была 1.9.90, то создаем соответствующий архив:<br />**# tar pczf ~/rpmbuild/SOURCES/openvswitch-1.9.90.tar.gz ./openvswitch<br /><br />**
1. Далее для сборки необходима более новая версия утилиты autoconf, чем есть в репозитории. Скачиваем и устанавливаем последнюю:<br />**# wget http://ftp.gnu.org/gnu/autoconf/autoconf-latest.tar.gz<br /># ./configure<br /># make<br /># make install<br />**
1. Переходим в папку с исходниками Open vSwitch и выполняем следующие команды:<br />**# ./boot.sh<br /># ./configure**<br /><br />Далее можно просто выполнить “**make && make install**”, но тогда будут проблемы с обновлением/удалением приложения и для следующей установки нужно будет выполнить те же сымые действия.
1. В папке с Open vSwitch запускаем команду, которая соберет нужную нам rpm:<br />**# rpmbuild -bb rhel/openvswitch.spec**
1. Аналогичным образом собираем модули для текущей версии ядра:<br />**# rpmbuild -bb -D "kversion `uname -r`" --target=i686-unknown-linux rhel/openvswitch-kmod-rhel6.spec**
1. Если все прошло успешно (а у меня это было именно так), то устанавливаем полученные rpms:<br />**# rpm -i kmod-openvswitch-1.9.90-1.el6.x86_64.rpm<br /># rpm -i openvswitch-1.9.90-1.x86_64.rpm **<br />
1. Open vSwitch может заменить собой стандартный модуль bridge и тогда brctl будет работать с Open vSwitch как и с обычными мостами, не подозревая что что-то не так. Для этого отключаем модуль brigde и включаем brcompat, который появился после установки Open vSwitch:<br />**# rmmod bridge<br /># modprode openvswitch<br /># modprode brcompat**<br /><br />Для того, чтобы убедиться, что нужные модели ядра загружены, выполняем команду lsmod.

 

 

Ну и последнее, запускаем  Open vSwitch: 

**# service openvswitch restart**

… и проверяем, что он работает:

**# ovs-vsctl show**

 

