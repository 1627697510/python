# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import ssl





user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }
for i in range(1,6):
    url = 'http://www.neihan.net/tags/4_'+str(i)+'.html'
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    #爬取内涵段子的标题
    content_pattern = re.compile('<span class="title"><a.*?>(.*?)</a></span>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #爬取内涵段子的内容
    content_pattern = re.compile('<dd class="content">(.*?)</dd>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的作者
    content_pattern = re.compile('<p class="user">.*?<a.*?>(.*?)</a>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的顶数
    content_pattern = re.compile('<a.*?title="顶">.*?<div class="dingcai">.*?<span></span>.*?<i>(.*?)</i>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的踩数
    content_pattern = re.compile('<a.*?title="踩">.*?<div class="dingcai">.*?<span></span>.*?<i>(.*?)</i>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
