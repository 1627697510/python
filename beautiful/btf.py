Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> from bs4 import BeautifulSoup as bs
>>> import urllib.request
>>> data=urllib.request.urlopen("http://edu.iqianyue.com/").read().decode("utf-8","ignore")
>>> bs1=bs(data)

Warning (from warnings module):
  File "D:\python\lib\site-packages\bs4\__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "lxml")

>>> bs1
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<title>韬云教育</title>
<link href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"/>
<script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<link href="./css/mybs.css" rel="stylesheet"/>
</head>
<body>
<div class="container">
<div class="row clearfix">
<div class="col-md-12 column">
<nav class="navbar navbar-default" role="navigation">
<div class="container-fluid">
<div class="navbar-header">
<button class="navbar-toggle" data-target=".navbar-collapse" data-toggle="collapse">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</button>
<a class="navbar-brand" href="#">
<img src="static/images/logo.png" style="height: 50px;margin-top:-15px;"/>
</a>
</div>
<div>
<ul class="nav navbar-nav">
<li class="active"><a href="static/../index">韬云教育</a></li><li><a href="static/../index_index_course">课程中心</a></li><li><a href="static/../index_index_teacher">专家师资</a></li><li><a href="/live/index.php">教学直播间</a></li>
<li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>
</ul>
<ul class="nav navbar-nav navbar-right">
<li><a href="static/../index_user_register">注册</a></li><li><a href="static/../index_user_login">登录</a></li>
</ul>
</div>
</div>
</nav>
</div>
</div>
</div>
</body>
</html>
<!--
轮播开始
-->

>>> bs1.prettify()
'<html xmlns="http://www.w3.org/1999/xhtml">\n <head>\n  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>\n  <title>\n   韬云教育\n  </title>\n  <link href="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet"/>\n  <script src="http://cdn.static.runoob.com/libs/jquery/2.1.1/jquery.min.js">\n  </script>\n  <script src="http://cdn.static.runoob.com/libs/bootstrap/3.3.7/js/bootstrap.min.js">\n  </script>\n  <link href="./css/mybs.css" rel="stylesheet"/>\n </head>\n <body>\n  <div class="container">\n   <div class="row clearfix">\n    <div class="col-md-12 column">\n     <nav class="navbar navbar-default" role="navigation">\n      <div class="container-fluid">\n       <div class="navbar-header">\n        <button class="navbar-toggle" data-target=".navbar-collapse" data-toggle="collapse">\n         <span class="icon-bar">\n         </span>\n         <span class="icon-bar">\n         </span>\n         <span class="icon-bar">\n         </span>\n        </button>\n        <a class="navbar-brand" href="#">\n         <img src="static/images/logo.png" style="height: 50px;margin-top:-15px;"/>\n        </a>\n       </div>\n       <div>\n        <ul class="nav navbar-nav">\n         <li class="active">\n          <a href="static/../index">\n           韬云教育\n          </a>\n         </li>\n         <li>\n          <a href="static/../index_index_course">\n           课程中心\n          </a>\n         </li>\n         <li>\n          <a href="static/../index_index_teacher">\n           专家师资\n          </a>\n         </li>\n         <li>\n          <a href="/live/index.php">\n           教学直播间\n          </a>\n         </li>\n         <li class="dropdown">\n          <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n           联系我们\n           <b class="caret">\n           </b>\n          </a>\n          <ul class="dropdown-menu">\n           <li>\n            <a href="static/../index_index_company">\n             公司资质\n            </a>\n           </li>\n           <li class="divider">\n           </li>\n           <li>\n            <a href="static/../index_index_about">\n             联系我们\n            </a>\n           </li>\n          </ul>\n         </li>\n        </ul>\n        <ul class="nav navbar-nav navbar-right">\n         <li>\n          <a href="static/../index_user_register">\n           注册\n          </a>\n         </li>\n         <li>\n          <a href="static/../index_user_login">\n           登录\n          </a>\n         </li>\n        </ul>\n       </div>\n      </div>\n     </nav>\n    </div>\n   </div>\n  </div>\n </body>\n</html>\n<!--\r\n轮播开始\r\n-->\n'
>>> bs1.title
<title>韬云教育</title>
>>> bs1.title.string
'韬云教育'
>>> bs1.title.name
'title'
>>> bs1.name
'[document]'
>>> bs1.attrs
{}
>>> bs1.a.attrs
{'class': ['navbar-brand'], 'href': '#'}
>>> bs1.a["class"]
['navbar-brand']
>>> bs1.a.get("class")
['navbar-brand']
>>> bs1.find_all('a')
[<a class="navbar-brand" href="#">
<img src="static/images/logo.png" style="height: 50px;margin-top:-15px;"/>
</a>, <a href="static/../index">韬云教育</a>, <a href="static/../index_index_course">课程中心</a>, <a href="static/../index_index_teacher">专家师资</a>, <a href="/live/index.php">教学直播间</a>, <a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>, <a href="static/../index_index_company">公司资质</a>, <a href="static/../index_index_about">联系我们</a>, <a href="static/../index_user_register">注册</a>, <a href="static/../index_user_login">登录</a>]
>>> bs1.find_all(['a','ul'])
[<a class="navbar-brand" href="#">
<img src="static/images/logo.png" style="height: 50px;margin-top:-15px;"/>
</a>, <ul class="nav navbar-nav">
<li class="active"><a href="static/../index">韬云教育</a></li><li><a href="static/../index_index_course">课程中心</a></li><li><a href="static/../index_index_teacher">专家师资</a></li><li><a href="/live/index.php">教学直播间</a></li>
<li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>
</ul>, <a href="static/../index">韬云教育</a>, <a href="static/../index_index_course">课程中心</a>, <a href="static/../index_index_teacher">专家师资</a>, <a href="/live/index.php">教学直播间</a>, <a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>, <ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>, <a href="static/../index_index_company">公司资质</a>, <a href="static/../index_index_about">联系我们</a>, <ul class="nav navbar-nav navbar-right">
<li><a href="static/../index_user_register">注册</a></li><li><a href="static/../index_user_login">登录</a></li>
</ul>, <a href="static/../index_user_register">注册</a>, <a href="static/../index_user_login">登录</a>]
>>> bs1.ul.contents
['\n', <li class="active"><a href="static/../index">韬云教育</a></li>, <li><a href="static/../index_index_course">课程中心</a></li>, <li><a href="static/../index_index_teacher">专家师资</a></li>, <li><a href="/live/index.php">教学直播间</a></li>, '\n', <li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>, '\n']
>>> bs1.ul.children
<list_iterator object at 0x0000000003E106A0>
>>> bs1.ul.contents
['\n', <li class="active"><a href="static/../index">韬云教育</a></li>, <li><a href="static/../index_index_course">课程中心</a></li>, <li><a href="static/../index_index_teacher">专家师资</a></li>, <li><a href="/live/index.php">教学直播间</a></li>, '\n', <li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>, '\n']
>>> bs1.ul.children
<list_iterator object at 0x0000000003DF7780>
>>> for i in k:
	print(k)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    for i in k:
NameError: name 'k' is not defined
>>> print i in k:
	
SyntaxError: Missing parentheses in call to 'print'
>>> for i in k:
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    for i in k:
NameError: name 'k' is not defined
>>> k=bs1.ul.children
>>> for i in k:
	print(k)

	
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
<list_iterator object at 0x0000000003E106A0>
>>> k=bs1.ul.children
>>> for i in k:
	print(i)

	


<li class="active"><a href="static/../index">韬云教育</a></li>
<li><a href="static/../index_index_course">课程中心</a></li>
<li><a href="static/../index_index_teacher">专家师资</a></li>
<li><a href="/live/index.php">教学直播间</a></li>


<li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>


>>> k=bs1.ul.children
>>> k2=[for i in k]
SyntaxError: invalid syntax
>>> k=bs1.ul.children
>>> k2=[i for i in k]
>>> k2
['\n', <li class="active"><a href="static/../index">韬云教育</a></li>, <li><a href="static/../index_index_course">课程中心</a></li>, <li><a href="static/../index_index_teacher">专家师资</a></li>, <li><a href="/live/index.php">教学直播间</a></li>, '\n', <li class="dropdown">
<a class="dropdown-toggle" data-toggle="dropdown" href="#">
					联系我们
					<b class="caret"></b>
</a>
<ul class="dropdown-menu">
<li><a href="static/../index_index_company">公司资质</a></li><li class="divider"></li><li><a href="static/../index_index_about">联系我们</a></li>
</ul>
</li>, '\n']
>>> bs1.title.string
'韬云教育'
>>> 
