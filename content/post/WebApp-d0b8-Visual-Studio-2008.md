---
title: "WebApp и Visual Studio 2008"
date: 2008-01-20T02:05:00+03:00
draft: False
category: [Web Development]
tags: [asp.net,visual studio]
archives: [2008]
aliases:
    - post/WebApp-d0b8-Visual-Studio-2008.aspx
---



В новой студии, по умолчанию, при создании веб-приложения на master page добавляется ещё один ContentPlaceHolder:


> 
	<br />
	<head runat="server"><br />
	<asp:ContentPlaceHolder ID="head" runat="server"><br />
	</asp:ContentPlaceHolder><br />
	</head><br />


> 
	<br />
	<title> Untitled Page </title> <title>My page</title>


	<br />
	<li>Явно присвоить в коде свойству Title страницы название:<br />
	Title = “My page”;</li><br />
	<li>Указать атрибут страице:<br />
	<%@ Page Language="C#" MasterPageFile="~/MyMaster.Master" AutoEventWireup="true" CodeBehind="MyPage.aspx.cs" Inherits="MySite.Pages" Title="My Page" %></li><br />
	<li>Установить тег title:<br />
	<blockquote>
		<br />
		<asp:Content ID="Content1" ContentPlaceHolderID="head" runat="server"><br />
		<title>My Page
	</blockquote>
	</li>

