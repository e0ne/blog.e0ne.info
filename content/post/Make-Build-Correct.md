---
title: "Делаем Build правильно"
date: 2009-03-20T11:00:00+03:00
draft: False
category: [.NET Framework,Web Development]
tags: [project,msbuild,visual studio]
archives: [2009]
aliases:
    - post/Make-Build-Correct.aspx
---



Осталось реализовать ещё несколько методов... Сейчас допишу последнюю строчку... Проект пока что не компилируется... Ура! Вот эта заветная строчка в окне Output Visual Studio:


> 
	========== Build: 1 succeeded or up-to-date, 0 failed, 0 skipped ==========


> 
	 



 Теперь предстоит запустить проект. Но все не так просто. Часто для проектов, которые больше чем знаменитый "Неllo World!" и который пишет команда из нескольких человек, необходимы какие-то условия для запуска:


	- скопировать конфигурационный файл;			
	- запустить веб-службу;			
	- отправить письмо о успешном билде;			
	- и т.д. и т.п.


 



Как правило, на первых порах это все делается вручную, но по мере роста проекта таки задач становится все больше, приходят новые люди и кто-то что-то обязательно забудет и потеряет n-е количество времени, которого всегда и так не хватает, для запуска проекта. После нескольких таких случаев, эти вещи начинают документировать (wiki проекта, спецификация, текстовый файл в репозитарии рядом с исходниками), иногда появляется инсталлятор, который делает вместо пользователя, но никак не помогает в процессе разработки.



Но тут к нам приходит на помощь всеми (не)любимая компания Microsoft со своей утилитой MS Build, которая достаточно хорошо интегрирована в Visual Studio. Msbuild.exe запускается каждый раз при сборке проекта или солюшена. 



Посмотрим на свойства проекта на вкладке [Build Events](http://msdn.microsoft.com/en-us/library/e2s2128d(VS.80).aspx).  



 
<img src="/image.axd?picture=build_tab.jpg" alt="" width="735" height="517" />



<img src="/image.axd?picture=build_macroses.jpg" alt="" /><br />
<br />
Перейдем к практике и напишем команду, которая будет выполняться после успешной сборки проекта. Допустим у нас в solution есть два проекта: консольное приложение и библиотека с классами.



 



<br />
  
<img src="/image.axd?picture=silution2.jpg" alt="" /><br />
Вот только, почему-то, MyClass из проекта MyClassLibrary использует CustomData.xml, предполагая что этот файл будет находится в той же папке, где находится наш solution. Поэтому, если просто добавить ссылку в проекте BuildEvents на проект MyClassLibrary, то ничего у нас работать не будет. Исправляем это добавлением Post Build event commad в проект MyClassLibrary:


> 
	<p>
	 copy $(ProjectDir)\CustomData.xml $(SolutionDir)
	</p>



Собираем solution и получаем:


> 
	<p>
	------ Build started: Project: BuildEvents, Configuration: Debug Any CPU ------<br />
	BuildEvents -> d:\Projects\Samples\BuildEvents\BuildEvents\bin\Debug\BuildEvents.exe<br />
	------ Build started: Project: MyClassLibrary, Configuration: Debug Any CPU ------
	</p>
	<p>
	... 
	</p>
	<p>
	Compile complete -- 0 errors, 0 warnings<br />
	MyClassLibrary -> d:\Projects\Samples\BuildEvents\MyClassLibrary\bin\Debug\MyClassLibrary.dll<br />
	copy d:\Projects\Samples\BuildEvents\MyClassLibrary\\CustomData.xml d:\Projects\Samples\BuildEvents\<br />
	        1 file(s) copied.<br />
	========== Build: 2 succeeded or up-to-date, 0 failed, 0 skipped ==========
	</p>



 Все успешно собралось и файл скопировался - в этом можно убедиться, открыв в проводнике папку с нашим solution. Теперь, если посмотреть содержимое файла MyClassLibrary.csproj, то увидем такие строчки:


> 
	<p>
	<PropertyGroup><br />
	    <PostBuildEvent>copy $(ProjectDir)\CustomData.xml $(SolutionDir)</PostBuildEvent><br />
	  </PropertyGroup><br />
	 
	</p>



Выше была описана выдуманная мной ситуация. Из практики столкнулся с таким: все config-файлы хранились в одной папке, а при сборке они копировались в Bin-папки проектов. 


