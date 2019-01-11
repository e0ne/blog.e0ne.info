---
title: "GIT: некоторые полезные команды"
date: 2013-01-07T23:32:00+03:00
draft: False
category: []
tags: [git]
archives: [2013]
aliases:
    - post/git-some-useful-commands.aspx
---

NOTE: English translation is here: [post/some-useful-git-commands-en/](post/some-useful-git-commands-en/)
 

Надоело постоянно гуглить одно и то же, решил записать в отдельную заметку.

 

1. Установить значения username/email:<br />**$ git config --global user.email "e0ne@e0ne.info"<br />$ git config --global user.name "e0ne"<br />**<br />через .gitconfig это делать не всегда удобно, т.к. иногда нужно разные name/email для разных upstream repos
1. Установить upstream branch:<br />$ git branch --set-upstream master upstream/master
1. Поменять последний коммит:<br />$ git commit --amend -a
1. Поменять автора нескольких коммитов:<br />$ git filter-branch --commit-filter '<br />        if [ "$GIT_COMMITTER_NAME" = "<Old Name>" ];<br />        then<br />                GIT_COMMITTER_NAME="<New Name>";<br />                GIT_AUTHOR_NAME="<New Name>";<br />                GIT_COMMITTER_EMAIL="<New Email>";<br />                GIT_AUTHOR_EMAIL="<New Email>";<br />                git commit-tree "$@";<br />        else<br />                git commit-tree "$@";<br />        fi' HEAD<br />$ git push
1. После мерджа пометить конфиликт как resolved:<br />$ git add file
1. Откатить локальные коммиты:<br />reset --soft HEAD^
1. Переместить тег на другой коммит:<br />$ git tag -d ver_0.1<br />$ git push origin :refs/tags/ver_0.1
1. Лучший мануал по git’у:<br />[http://git-scm.com/book](http://git-scm.com/book)
1. Мой .gitconfig лежит тут: [https://github.com/e0ne/dot-files/blob/master/.gitconfig](https://github.com/e0ne/dot-files/blob/master/.gitconfig)
1. Мой .gitignore лежит тут: [https://github.com/e0ne/dot-files/blob/master/.gitignore](https://github.com/e0ne/dot-files/blob/master/.gitignore)
1. Cоздаем branch из tag'а: [http://blog.e0ne.info/post/Git-create-branch-from-tag.aspx](http://blog.e0ne.info/post/Git-create-branch-from-tag.aspx)
1. Мерджим апдейты с другого репозитория: [http://korenkov.info/fetching-updates-from-another-git-repo](http://korenkov.info/fetching-updates-from-another-git-repo)<br /><br />[Updated 26.04.13]
1. Обновить исходники, затирая локальные изменения:<br />$ git fetch --all<br />$ git reset --hard origin/master
1. Удалить все недобавленные в репозиторий файлы и директории:<br />$ git clean -f -d

 

