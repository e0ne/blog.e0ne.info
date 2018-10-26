---
title: "OpenStack и Quantum: начало"
date: 2012-09-11T13:45:00+03:00
draft: False
category: [Python]
tags: [openstack,quantum]
archives: [2012]
aliases:
    - post/OpenStack-and-Quantum-begining.aspx
---


 

Из wiki.openstack.org:

**Quantum is an OpenStack project to provide "network connectivity as a service" between interface devices (e.g., vNICs) managed by other Openstack services (e.g., nova).**

Из описания можно предположить, что в будущем это станет заменой nova network, что не далеко от правды. Ниже я расскажу об установки OpenStack + Quantum и немного о самом Quantum.

Установка OpenStack c помощью скриптов [devstack](http://devstack.org/) является одной из самых простых и быстрых. В простейшем случае, это выглядит так:

$ git clone https://github.com/openstack-dev/devstack.git<br />$ cd devstack && ./stack.sh

После этого нужно будет лишь ввести свой root-пароль, пароль к MySql серверу и пароли к Openstack’у. При установке Quantum нужно создать и/или отредактировать файл localrc в каталоге с Devstack’ом и добавить туда следующие строчки:

disable_service n-net<br />enable_service q-svc<br />enable_service q-agt<br />enable_service q-dhcp<br />enable_service quantum<br />LIBVIRT_FIREWALL_DRIVER=nova.virt.firewall.NoopFirewallDriver<br />Q_PLUGIN=openvswitch

Разберем эти строчуки подробнее:

 

- LIBVIRT_FIREWALL_DRIVER=nova.virt.firewall.NoopFirewallDriver - настраивваем libvirt для корректной работы файрволла с Quantum
- Q_PLUGIN=openvswitch - указываем, что в качестве плагина (back-end’а) использовать [Open vSwitch](http://openvswitch.org/).
- disable_service n-net - отключение nova-network, теперь вместо этого компонента будет работать Quantum.
- enable_service q-svc - включаем Quantum Server. По сути, после скачивания исходников и первоначальной настройки выполнится такая команда: “**/opt/stack/quantum/bin/quantum-server --config-file /etc/quantum/quantum.conf --config-file /etc/quantum/plugins/openvswitch/ovs_quantum_plugin.ini**”. На момент написания этого поста есть баг, в котором описано что Quantum plugins должны использовать тот жу конфигурационный файл, что и Quantum. Но пока это не пофикшено.
- enable_service q-agt - запустить Quantum agent. Т.к. в качестве плагина был выбран Open vSwitch, то и запустится, соответственно, Open vSwitch Plugin:** $ sudo python /opt/stack/quantum/quantum/plugins/openvswitch/agent/ovs_quantum_agent.py --config-file /etc/quantum/quantum.conf --config-file /etc/quantum/plugins/openvswitch/ovs_quantum_plugin.ini**
- enable_service q-dhcp - Quantum DHCP Agent, который управляет DHCP сервером внутри нашей виртуальной сети. Запускается он следующей командой:  **sudo python /opt/stack/quantum/bin/quantum-dhcp-agent --config-file /etc/quantum/quantum.conf --config-file=/etc/quantum/dhcp_agent.ini**.  Из коробки это dnsmasq, но можно написать поддержку любого сервера.

 

После правки localrc можно запускать stack.sh и подождать пока все будет установленно.

Кроме установки самого OpenStack’а, devstack так же создает тестовых пользователей, проектов и сети. Т.к. говорим о Quantum, то о сетях подробнее.

Сам по себе Quantum (так сказать, его core) предоставляет только API для создания и управления сетями. Самим управлением занимаются его плагины (plugins), которые, imho, правильнее было бы назвать бэк-ендами (back-ends). В текущей версии (Folsom) возможна одновременная работа только одного плагина. Т.к. мы установили Open vSwitch, то далее буду описывать работу Quantum с ним.

Основные понятия в Quantum:

 

- **network** - изолированный L2 сегмент сети, аналог VLAN;
- **subnet** - блок IPv4 или IPv6 адресов и их конфигурация (маршрутизатор, DNS-сервер)
- **port** - точка подключения устройств (vNICs) в сеть Quantum.

 

Если смотреть на взаимодействие Quantum Network и OpenStack, то это выглядит так:

У каждого тенанта может быть одна и более сетей. У каждой сети может быть от 1 до n подсетей (конечно, может быть и 0 сетей/подсетей, по смысла в этом нет). Если смотреть на то, как все рабтало без Quantum, то теперьешине subnets это аналоги nova networks. При замуске виртуалки (инстанса), ей нужног передать к какой из сетей тенанта она подключена. Для каждой подсети будет создан отдельный vNIC у инстанса, который будет подключен к какому-либо порту. В нашем случае - это порт в Open vSwitch.

Посмотрим как это работает на практики:

Open vSwitch работает поверх бриджей (bridge), поэтому посмотрим какие “мосты” у нас есть:

**$ sudo ovs-vsctl list-br<br />****br-int<br />****br-tun**

Сейчас нас интересует br-int, поэтому посмотрим какие у него есть порты:

**$ sudo ovs-vsctl list-ports br-int<br />******

**patch-tun<br />****tap6d98326d-5a<br />****tap6e1a8612-27<br />****tapf842abe0-27**

В данной конфигурации, у меня запущено два инстанса, которые подключены к портам tap6e1a8612-27 и tapf842abe0-27. Порт patch-tun служит для “проброса” трафика между виртуальной сетью и физической через TUN-интерфейс. К порту tap6d98326d-5a подключен DHCP-сервер(dnsmasq) для инстансов внутри subnet.

Посмотрим, какие у нас есть сети в Quantum:

**$ quantum net-list**

<img src="/image.axd?picture=2012%2f9%2fnets.png" alt="" />

 

И подсети:

**$ quantum subnet-list**

<img src="/image.axd?picture=2012%2f9%2fsubnets.png" alt="" />

 

Порты:

**$ quantum port-list**

<img src="/image.axd?picture=2012%2f9%2fports.png" alt="" />

 

Тут мы видем, что у нашего DHCP-сервера адрес 10.0.1.2, а у инстансов 10.0.1.3 и 10.0.1.4.

 

Теперь, когда мы хоть немного имеем представление о сети, попробуем запустить новый инстанс:

**$ nova boot --flavor 1 --image 4032fc9c-4688-4e71-ba2d-5a90e7698230 --nic net-id=3d5a9b8d-40cf-4f7b-a344-3db20f1a4783 test_vm_3**

Синтаксис стандартный за исключением того, что я явно передал к какой сети подключать инстанс “--nic net-id=3d5a9b8d-40cf-4f7b-a344-3db20f1a4783”

Убедимся, что инстанс запустился командой “nova list”. И если у него статус ACTIVE, то можно попробовать попинговать или зайти по SSH:

<img src="/image.axd?picture=2012%2f9%2fping-fail.png" alt="" />


<p>Тут мы обнаруживае, что из хоста у нас нет доступа к виртуалкам :(. Хотя, если зайти через VNC на виртуалки, то они нормально будут видет другие инстансы в той же подсети.

 

Все дело в том, что Quantum организует работу с сетями через network netspace (http://stuff.onse.fi/man?program=ip-netns&section=8), поэтому, алгоритм работы немного усложняется:

смотрим список текущих неймспейсов:

**$ ip netns**

Выполняем ping/ssh внутри нужного неймспейса:

**~$ sudo ip netns exec qdhcp-3d5a9b8d-40cf-4f7b-a344-3db20f1a4783 ssh 10.0.1.4**

 

Ссылки по теме:


<ul>
- [http://openstack.org/](http://openstack.org/)
- [http://devstack.org/](http://devstack.org/)
- [http://wiki.openstack.org/Quantum](http://wiki.openstack.org/Quantum)
- [http://openvswitch.org/](http://openvswitch.org/)
- [http://ru.wikipedia.org/wiki/TUN/TAP](http://ru.wikipedia.org/wiki/TUN/TAP)
- [http://stuff.onse.fi/man?program=ip-netns&section=8](http://stuff.onse.fi/man?program=ip-netns&section=8)
- [https://github.com/openstack/](https://github.com/openstack/)
</ul>


 

Продолжение следует...

