---
title: "OpenStack Metadata server"
date: 2012-10-03T00:15:00+03:00
draft: True
category: []
tags: [openstack]
archives: [2012]
aliases:
    - post/OpenStack-Metadata-server.aspx
---



<p>OpenStack Metadata server - достаточно небольшой, но полезный компонент OpenStack’а, о котором, к сожалению, знают далеко не все.

Как следует из названия - это какой-то сервер, который предоставляет какие-то метаданные. Далее коротко какие именно метаданне и зачем они нужны, но для начала немного предистории.

Ни для кого не секрет, что одна из основных целей OpenStack’а есть(была?) это конкуренция с Amazon EC2. Отсюда появилась и поддержка Amazon EC2 API, и Metadata Server, который, к слову, если и не полностью, то в большей части повторяет API своего прародителя-конкурента. Подробнее про AWSEC2 Instance Metadata можно почитать тут: [http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)

[](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)В OpenStack’е метаданные могут быть не только для инстансов(instances), но и для серверов(computes), образов(images). Т.к. метаданные для серверов доступны через Nova API, что рассматривать их сейчас не буду. Включается доступ к этим метаданным через API в nova.conf путем добавления значения metadata в секцию enabled_apis.

Остановимся подробнее на Instances Metadata API, которое в OpenStack’е называется Nova Metadata API и запускается через bin/nova-api-metadata, его реализация достаточно простая и практически поместилась в один модуль ([https://github.com/openstack/nova/blob/master/nova/api/metadata/base.py](https://github.com/openstack/nova/blob/master/nova/api/metadata/base.py)). 

В этих метаданных хранятся некоторые instance specific данные, такие как instance name, instance api, host name, public ssh keys и некоторые другие.

Алгоритм использования метадата сервера, примерно, такой:

<ol>
- На compute node запускается nova-api-metadata. Стоит заметить, что сервер слушает 80-й порт на 169.254.169.254 адресе (к слову, в более ранних релизах metadata api server был частью nova api, а посже, слушал не 80-й порт) и , и при установки devstack’ом он не запускается(без него вполне можно обойтись), поэтому в сучае конфигурации all-in-one прийдется сделать одно из двух: заставить работать apache/openstack dashboard на отличном от 80-порте (простой вариант) или заставить инстансы получать данные не с 80-го порта(более сложный путь). Т.к. адрес 169.254.169.254 доступен при еще не сконфигуренных сетевых интерфейсах, то инстансы смогут до него “достучаться”.
- У инстанса должен стоять пакет cloud-init или он должен быть настроен руками так, что бы при старте забрать с metadata api все нужные данные. Таким образом сетевой интерфейс инстанса (vNIC) может быть успешно сконфигурированный без DHCP сервера и иньекции (injection) файла /etc/network/interfaces (для Ubuntu).
</ol>

Также при использовании CloudPipe (VPN for tenant), CloudPipe инстанс с помощью Metadata API Server получает неоюходимые файлы сертификатов и настройки для OpenVPN сервера.

 

Полезные ссылки:


<ul>
- [http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html](http://docs.amazonwebservices.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)
- [http://docs.openstack.org/api/openstack-compute/programmer/content/setting-server-metadata.html](http://docs.openstack.org/api/openstack-compute/programmer/content/setting-server-metadata.html)
- [https://blueprints.launchpad.net/nova/+spec/openstack-api-metadata](https://blueprints.launchpad.net/nova/+spec/openstack-api-metadata)
- [http://api.openstack.org/](http://api.openstack.org/)
- [http://docs.openstack.org/api/openstack-compute/2/content/List_Metadata-d1e5089.html](http://docs.openstack.org/api/openstack-compute/2/content/List_Metadata-d1e5089.html)
- [http://docs.openstack.org/api/openstack-compute/2/content/Server_Metadata-d1e2529.html](http://docs.openstack.org/api/openstack-compute/2/content/Server_Metadata-d1e2529.html)
- [http://docs.openstack.org/api/openstack-compute/programmer/content/customizing-your-server-adding-metadata.html](http://docs.openstack.org/api/openstack-compute/programmer/content/customizing-your-server-adding-metadata.html)
- [https://blueprints.launchpad.net/nova/+spec/openstack-api-metadata](https://blueprints.launchpad.net/nova/+spec/openstack-api-metadata)
- [http://docs.openstack.org/trunk/openstack-compute/admin/content/creating-a-linux-image.html](http://docs.openstack.org/trunk/openstack-compute/admin/content/creating-a-linux-image.html)
</ul>


