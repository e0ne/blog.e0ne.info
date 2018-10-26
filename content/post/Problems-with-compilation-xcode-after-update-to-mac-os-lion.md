---
title: "Пролемы с компиляцией (Xcode) после перехода на Mac OS Lion"
date: 2012-04-30T23:50:00+03:00
draft: False
category: []
tags: [mac os,xcode]
archives: [2012]
aliases:
    - post/Problems-with-compilation-xcode-after-update-to-mac-os-lion.aspx
---


После перехода на Mac OS X Lion многие приложения, которые нужно устанавливать с исходноков перестали компилироваться с примерно такой ошибкой:

 

**error trying to exec 'cc1plus': execvp: No such file or directory**

В список таких приложений попали macports, MacVim, питоновские библиотеки, которые имели расширения на C и т.д. Суть проблемы заключается в том, что Xcode 4.3 или предыдущая версия (Xcode'ом не польщуюсь, поэтому особо не слежу за апдейтами) начал ставиться со всеми зависимостями и тулами в другую папку, а именно в ****/Applications/Xcode.app/Contents/Developer/**** вместо ****/Developer/****. А так, как у меня стояла предыдущая версия, то новая, по каким-то причинам оставило старую как дефолтную. 

Исправить это просто, достаточно выполнить одну команду:

**$ sudo /usr/bin/xcode-select -switch /Applications/Xcode.app/Contents/Developer**

 

