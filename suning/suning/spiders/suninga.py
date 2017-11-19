#! /usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from suning.items import SuningItem
from scrapy.http import Request
from lxml import etree
import json
import io
from selenium import webdriver
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
class SuningaSpider(scrapy.Spider):
    name = 'suninga'
    allowed_domains = ['https://suning.com']
    #start_urls = ['http://https://suning.com/']
    ua = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]
    def start_requests(self):
        req1= urllib.request.Request("https://book.suning.com/")
        req1.add_header("User-Agent", random.choice(self.ua))
        data1=urllib.request.urlopen(req1).read().decode("utf-8","ignore")
        pat1='<h3><a.*?href.*?</a></h3>'
        pat2='<a href="..list.suning.com.*?.html" target="_blank">.*?</a>'
        pat3='<li><a.*?..list.suning.com.*?">.*?</a></li>'
        rst1 = re.compile(pat1).findall(data1)
        rst2=re.compile(pat2).findall(data1)
        rst3=re.compile(pat3).findall(data1)
        #print(len(rst3))
        rst4=rst1+rst2+rst3
        #print(rst4)
        catall=[]
        for cat in rst4:
            treedata=etree.HTML(cat)
            cat1_link=treedata.xpath("//a/@href")
            cat1_name=treedata.xpath("//a/text()")
            #print(cat1_link)
            #print(cat1_name)
            cat2_link=treedata.xpath("//li/a/@href")
            #print(cat2_link)
            #print(len(cat2_link))
            for i in cat2_link:
                thisurl=i
                req2=urllib.request.Request(i)
                req2.add_header("User-Agent", random.choice(self.ua))
                data2=urllib.request.urlopen(req2).read().decode("utf-8","ignore")
                #print(len(data2))
                pat4='href="..list.suning.com.*?.html#search-path-box'
                rst5=re.compile(pat4).findall(data2)
                cat_id=rst5[0][26:32].replace("-",",")
                #print(type(cat_id))
                #print(type(rst5))
                #print(rst5)
                urls=[]
                for j in range(0,len(rst5)):
                    current_url='https://list.suning.com/emall/showProductList.do?ci='+str(cat_id)+'&pg=03&cp='+str(j)+''
                    urls.append(current_url)
                #print(urls)
                for url in urls:
                    yield Request(url=url,callback=self.parse)
    def parse(self, response):
        item=SuningItem()
        item["name"]=response.xpath("//div[@class='img-block']/a/img/@alt").extract()
        item["link"]=response.xpath("//div[@class='img-block']/a/@href").extract()
        item["seller"]=response.xpath("//p[@class='seller no-more']/a/text()").extract()
        item["evalute"]=response.xpath("//a[@class='num']/text()").extract()
        #print(item["evalute"])
        yield item

