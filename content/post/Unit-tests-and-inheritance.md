---
title: "Unit тесты и наследование"
date: 2008-12-23T14:33:00+03:00
draft: False
category: [.NET Framework]
tags: [unit tests,visual studio]
archives: [2008]
aliases:
    - post/Unit-tests-and-inheritance.aspx
---



При разработке unit тестов в Visual Studio часто хочется создать какой-то базовый клас для тестирования базовой лоники. Например у нас есть такой класс:



 



        [TestClass]<br />
        public class PersonTestBase<br />
        {<br />
            [TestMethod]<br />
            public virtual void GetNameTest()<br />
            {



                //...<br />
            }<br />
        }



 и его класс наследник:<br />
        [TestClass]<br />
    public class CustomerTest: PersonTestBase<br />
    {<br />
        [TestMethod]<br />
        public override void GetNameTest()<br />
        {<br />
            base.GetNameTest();<br />
        }<br />
    }



 Плюсы такого подхода:


				
	- полная поддержка визуальных средств Visual Studio (Test List Editor);			
	- простота реализации.

				
	- избыточность кода;			
	- создание наследника является по сути copy&paste.	

				
	-  создаётся два проекта: BaseTests и CustomTests;		
	- в проект CustomTests добавляются необходимые файлы из BaseTests таким образом: Project -> Add Existing Item -> Выбираем необходимые файлы -> Add As Link.

				
	- фактически, в классе у реализоано 2 тестовы метода: один перешел из базового класса и один мы реализовали сами.		
	- Visual Studio Test List Editor говорит что у нас только один тетовый медов - метода из бащового класс не отображается и, соответственно, не запускается.

				
	- мы избавились от минусов предыдущего метода;

				
	- нету интеграции с Visual Studio. 

