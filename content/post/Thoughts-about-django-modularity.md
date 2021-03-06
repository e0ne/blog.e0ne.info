---
title: "Мысли в влух о модульности Django"
date: 2012-01-03T15:10:00+03:00
draft: False
category: [Python]
tags: [django,python]
archives: [2012]
aliases:
    - post/Thoughts-about-django-modularity.aspx
---



<p>**Все сказанное ниже является личным мнением автора и не является объективной точкой зрения и/или истиной последней инстанции.**

Я всегда считал и продолжаю это делать, что Django - не очень-то и модульный фреймворк. Он расширяемый, но не модульный, IMHO. В моем понимании модульный фреймворк, это фреймворк, который состоит из ядра (core), и каких-то модулей, которые можно к нему подключать при желании/необходимости. Но и без них будет доступна минимальная функциональность. В случае же Django - выкинуть из него некоторые модули (e.g. models, template engine) достаточно сложно. Что-бы сделать что-то подобное, необходимо самостоятельно удалять ненужные куски кода, что тянет за собой проверку работоспособности оставшихся частей и прочие неприятности в виде сложной поддержки полученного кода и обновление фреймворка.

Django - легко расширяемый фреймворк. Это видно по django.contrib и многочисленных сторонних дополнений и приложений. Но при добавлении нового, все-равно есть возможность пользоваться старыми стандартными модулями Django.

Т.к. этот вопрос интересует меня давно, я его задавал одному из Django Core Developers, Andrew Goodwin’уб на прошедшем в октябре UA Pycon. Далее в вольном пересказе пишу **его слова так, как я их понял**:

“Мы знаем об этой проблеме и у нас есть в планах заняться этой задачей. Но есть еще масса более важных задач, которые нужно делать. Поэтому я не могу сказать, когда мы начнем это реализовывать. Также по идеологии Django нужно совместимость версий: код, написанный для текущей версии, должен без изменений работать на следующей.

И есть еще одна проблема: community хочет не только модульность самого Django, но и возможность использование его компонентов, например models, вне Django. В данной это невозможно, но мы хотим когда-нибудь это сделать”

Несколько ссылок по теме из википедии:


<ul>
- [http://en.wikipedia.org/wiki/Extensibility](http://en.wikipedia.org/wiki/Extensibility)
- [http://en.wikipedia.org/wiki/Modularity_(programming)](http://en.wikipedia.org/wiki/Modularity_(programming))
</ul>
<br />


