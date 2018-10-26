---
title: "Мобильные сайты на Django"
date: 2011-12-27T15:53:00+03:00
draft: False
category: [Python,Web Development]
tags: [django,mobile]
archives: [2011]
aliases:
    - post/Mobile-sites-on-django.aspx
---



<p>Как правило, адаптация сайтов под мобильные устройства заключается в выполнении одного или нескольких пунктов из следующего списка:


<ul>
- подключения специальной версии CSS;
- подключения нужных JavaScript’ов;
- создание мобильных шаблонов (templates) с версткой (html).
</ul>


Сразу оговорюсь, что вопрос мобильной верстки сейчас затрагивать не буду.

Исходя из этого списка, шаблоны, которые предназначенные для мобильных устройст будут выглядеть, примерно, так:

**{% if request.mobile %}<br />    Mobile<br />{% else %}<br />    Not mobile<br />{% endif %}**

 

Или же наша view поменяет вид на такой:

**def index(request):<br />    if not request.mobile:<br />        return render_to_response('index.html’)<br />    else:<br />        return render_to_response('mobile_index.html’)**

Теперь дело за малым - сделать так, чтоб в объекте нашего запроса (request’а) появилось свойство mobile. Один из самых простых и достаточно эффективных способов - посмотреть какой [USER_AGENT](http://en.wikipedia.org/wiki/User_agent) у браузера, который делает запрос. Для этих целей уже есть небольшой, но удобный компонент [minidecector](http://code.google.com/p/minidetector/), который анализирует USER_AGENT из запроса и выставляет нужное значение свойства request.mobile.

minidetector можно подключать двумя способами:


<ul>
- добавление декоратора detect_mobile к нужной view;
- добавление уже готового Middleware; в этом случае будут обрабатываться все запросы к нашему приложению.
</ul>


Небольшой пример использования minidetector лежит на GitHub’e: [https://github.com/e0ne/BlogSamples/tree/master/MobileTest](https://github.com/e0ne/BlogSamples/tree/master/MobileTest)

 

Другие ссылки по теме:


<ul>
- [http://stackoverflow.com/questions/164427/change-django-templates-based-on-user-agent](http://stackoverflow.com/questions/164427/change-django-templates-based-on-user-agent)
- [http://code.google.com/p/minidetector/](http://code.google.com/p/minidetector/)
- [http://stackoverflow.com/questions/2321172/detect-mobile-browser-not-just-iphone-in-python-view](http://stackoverflow.com/questions/2321172/detect-mobile-browser-not-just-iphone-in-python-view)
</ul>
Напомню, что протестировать это на встроеном в Django веб-сервере не получится, т.к. он работает только локально и вы не зайдете на него со своего мобильного устройста. Настройка Django+Apache+mod_wsgi описана тут: [https://code.djangoproject.com/wiki/django_apache_and_mod_wsgi](https://code.djangoproject.com/wiki/django_apache_and_mod_wsgi)


