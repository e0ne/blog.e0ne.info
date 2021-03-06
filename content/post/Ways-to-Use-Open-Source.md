---
title: "Пути использования Open Source"
date: 2009-03-27T14:37:00+03:00
draft: False
category: [Offtopic]
tags: []
archives: [2009]
aliases:
    - post/Ways-to-Use-Open-Source.aspx
---


> 		На мысль натолкнуло исправление очередного бага в Ajax Control Toolkit.

> 	 

Часто мы в проектах, чтобы не изобретать велосипед, используем уже готовые инструменты. Иногда это open source приложения/библиотеки. И что делать, если нам не хватает функциональности этих библиотек или надо срочно исправить какуе-то ошибку? Первая же мысль - это взять исходники, подправить/дописать, после чего скомпилировать и радоваться жизни. Но радоваться будем недолго, до выхода новой версии этой замечательной библиотеке, в которой есть необходимые изменения. Приходится качать исходники, опять вносить туда свои изменение, компилировать и т.д. В процессе этого пишуться письма авторам библиотеке, создаются новые запись в ихнем багтрекере, но необходимых изменений в очередной версии мы так и не получаем.

После нескольких таких итераций голову приходит очередная мысль (нет, не отказаться от этого продукта): "А, может, не будем изменять исходники? Может, просто приспособимся к их API или сделаем класс-наследник и добавим в него недостающую функциональность?". В этот момент начинает казаться, что пользы от open source становится всё меньше и меньше. При таком подходе переход на новую версию используемой библиотеке становится менее болезненным, но мы не застрахованы, что в новой версии ничего не изменится и не поломает нашу функциональность.

И вот с выходом новой версии библиотеки, в которой, конечно же, есть новые, жизненно-важные, для нас функции, мы долго размышляем, сомневаемся, но всё же приходим к решению использовать её. Но всё оказалось не так хорошо, как хотелось: API поменялся, наши изменения не работают, а проект вообще не компилируется. В этот появляется третья мысль, относительно используемой библиотеке: "Ведь нам не нужна все её функциональность?! Давайте напишем свою! Там будет только то, что нам нужно и не будет лишних багов, нас не будет волновать выход новой версии...". И все дружно начинают писать свою версию open source библиотеки, стараясь не сделать ошибок своих предшественников и делаю новые, но свои, ошибки... 

Возможен так же сценарий, в котором на каком-то из этапов принимается решение отказаться от библиотеки А и использовать библиотеку В. А знаю, что использование готовых продуктов на первых порах ускоряет написание и выпуск своего продукта, но, в будущем, вполне вероятно что прийдётся отказаться и использовать что-то другое. И это займет намного больше времени, чем внедрять это в начальных стадиях разработки проекта. 

Нет определенного ответа на вопрос "Использовать библиотеку А, В,заплатить за библиотеку С или написать свою?". Все зависит от конкретного случая и выбор, временами, сделать очень трудно. Интересно, какие у вас мысли по этому поводу? Аналогичная, по моему мнению, и ситуация с использованием CMS для сайта: писать свою, взять готовую или на основе готового написать свою? 

P.S. Всё это я рассмотрел со стороны рядового разработчика и не учитывал влияния заказчика PM-а и других заинтересованных сторон. 

