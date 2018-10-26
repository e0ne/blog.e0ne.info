---
title: "О времени и выборе инструментов для разработки"
date: 2014-01-09T19:22:00+03:00
draft: False
category: [Offtopic]
tags: []
archives: [2014]
aliases:
    - post/about-time-and-devtools-selection.aspx
---


Безусловно, выбор языка программироания, текстового редактора, IDE, операционной системы и многого другого лежит на плечах каждого отдельно взятого разработчика. Даже если он работает в команде.

По сути, всем все-равно в какой IDE пишете код, если он работает так, как надо и написан вовремя. Унификация средст разработки внутри компании/команды лишь облегчает жизть менеджерам, ИТ, новым членам команды и упрощает коммуникацию между разработчиками. Ведь на много легче один раз написать инструкцию по установки всего нужного для запуска проекта ПО, например, для Ubuntu 13.10 x64 и запуск проекта в PyCharm, чем каждый раз сталкиваться с проблемой как запустить X в окружении Y.

Но каждый разработчик в праве решать сам чем он будет пользоваться. Вот только к выбору инструментов нужно подходить “с умом”. Главное - хорошо знать инструменты, которыми вы пользуетесь. Иначе будет ситуация, когда используется Photoshop только для изменения размера картинки. Досконально знать OS, IDE, текстовый редактор, которым пользуетесь каждый день не только приятно, но и полезно. Это может экономить массу времени. Всем известно, что использования горячих клавиш, в некоторых условиях, в разы быстрее, чем совершать нужные действия мышкой. Аналогичная ситуация с разнообразными инструментами автоматизации. Если мне нужно выполнить действиее более 2-3х раз - я пишу небольшой скрипт на bash или python. Иногда скрипты получаются не очень и маленькими, иногда в помощь приходят fabric/chef/puppet. Готовые настройки для используемых редактором и систем (профайлы bash, zsh) - упрощают жизь и экономят время, которое можно потратить на более полезные и интересные вещи.

Все вышесказанное всем известно и описано в множестве книг и постов. Захотелось повторить, т.к. я в очередной раз наступил на эти грабли: потратил почти час на написание простого скрипта на bash’е, аналог которого на python мне удалось написать за 10 минут. Да, я узнал кое-что новое о bash, но это не мой основной язык программирования, и скрипт писался исключительно для себя (и не важно, что любой может скачать его с github и пользоваться), но я потратил массу времени из-за того, что выбрал не тот инструмент. Нельзя путать процесс обучения и процесс разаботки. Между ними очень тонкая грань, которую легко перейти и потерять время напрасно.
