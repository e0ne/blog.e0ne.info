---
title: "Встречаем новый язык программирования от Microsoft - Axum"
date: 2009-05-24T14:33:00+03:00
draft: False
category: [.NET Framework]
tags: [axum,paraller development]
archives: [2009]
aliases:
    - post/Microsoft-Axum.aspx
---



Не успели мы ещё познакомитя с F# и новыми возможнастями .NET 4.0, как Microsoft представила новый язык программирования [Axum](http://msdn.microsoft.com/en-us/devlabs/dd795202.aspx) (на самом деле Axum был представлен ещё до выпуска первой бета-версии .NET 4.0). Раньше он имел коддовое название Maestro.



Что же представляет собой Axum? Это язык для паралельной разработки (parallel model language), который позволяетлегко создавать легкомасштабируемые, распределённые и многопоточные приложения. Лично мне синтаксис этого языка напомнил [Erlang](http://erlang.org/), которые имеет изменённый синтаксис и является полностью .net-совместимым языком программирования. Текущяя версия - CTP. В данный момент не известно о дальнейшей судьбе и планах о релизе. 



Чтобы посмотреть на этот язык вживую необходимо скачать небольшой 4.2МБ) плагин для Visual Studio 2008, на момент написание этого поста плагина для Visual Studio 2010 ещё нет. 



<img src="/image.axd?picture=axum.jpg" alt="" /><br />
<br />
Так же с сайта Axum можно скачать [спецификицию языка](http://download.microsoft.com/download/B/D/5/BD51FFB2-C777-43B0-AC24-BDE3C88E231F/Axum%20Language%20Spec.pdf) и [руководство разработчкика](http://download.microsoft.com/download/B/D/5/BD51FFB2-C777-43B0-AC24-BDE3C88E231F/Axum%20Programmers%20Guide.pdf) на 42 и 36 страниц соответственно. Некоторую информацию можно узнать из [блога ](http://blogs.msdn.com/maestroteam/default.aspx)команды разработчиков. Информации пока не много, но и её достаточно для знакомства с языкам и написанием приложений.



И на завершении, по традиции привожу пример "Hello World!".



 


	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	using System;
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	using System.Concurrency;
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	using Microsoft.Axum;
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	 
	
	</li>
	<li style="vertical-align: top; font-weight: bold; color: #006060">
	
	namespace ConsoleApplication1
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	{
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	    public domain Program
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	    {
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	        private writer agent MainAgent : channel Microsoft.Axum.Application
	
	</li>
	<li style="vertical-align: top; font-weight: bold; color: #006060">
	
	        {
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	            public MainAgent()
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	            {
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	                String [] args = receive(PrimaryChannel::CommandLine);
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	 
	
	</li>
	<li style="vertical-align: top; font-weight: bold; color: #006060">
	
	                Console.WriteLine(String.Format("Hello, {0}!", args[0]));
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	 
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	                PrimaryChannel::Done <-- Signal.Value;
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	            }
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	        }
	
	</li>
	<li style="vertical-align: top; font-weight: bold; color: #006060">
	
	    }
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	}
	
	</li>
	<li style="vertical-align: top; font-family: 'Courier New',Courier,monospace; font-style: normal; font-variant: normal; font-weight: normal; font-size: 130%; line-height: normal; font-size-adjust: none; font-stretch: normal; color: #003030">
	
	 
	
	</li>

