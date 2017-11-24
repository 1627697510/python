# -*- coding: utf-8 -*-
import scrapy
import random
import urllib.request
import re
from zhaopin.items import ZhaopinItem
from scrapy.http import Request


class GaoxiaoSpider(scrapy.Spider):
    name = 'gaoxiao'
    allowed_domains = ['gaoxiaojob.com']
    #start_urls = ['http://gaoxiaojob.com/']
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
    list=['anhui', 'beijing', 'chongqing', 'fujian', 'gansu', 'guangdong', 'guangxi', 'guizhou', 'hainan', 'huabei', 'henan', 'heilongjiang', 'hubei', 'hunan', 'jilin', 'jiangsu', 'jiangxi', 'liaoning', 'neimenggu', 'ningxia', 'qinghai', 'shandong', 'shanxisheng', 'shaanxi', 'shanghai', 'sichuan', 'tianjin', 'xicang', 'xinjiang', 'yunnan', 'zhejiang', 'gangaotai', 'haiwai']

    def start_requests(self):
        req1=urllib.request.Request('http://www.gaoxiaojob.com/zhaopin/diqu/')
        req1.add_header("User-Agent", random.choice(self.ua))
        data1=urllib.request.urlopen(req1).read().decode("gb2312")
        pat1="<li><a href='(.*?)'>.*?</a></li>"
        rst1=re.compile(pat1).findall(data1)
        #print(rst1)
        urls=[]
        for k in range(0,len(self.list)):
            for i in range(1,len(rst1)):
                thisurl='http://www.gaoxiaojob.com/zhaopin/diqu/'+self.list[k]+'/index_'+str(i)+'.html'
                urls.append(thisurl)
            #print(len(urls))
            for url in urls:
                yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item=ZhaopinItem()
        item["title"]=response.xpath("//span[@class='ltitle']/a/b/text() | //span[@class='ltitle']/a/text()").extract()
        item["deadline"]=response.xpath("//span[@class='ltime']/text()").extract()
        item["location"]=response.xpath("//span[@class='lcompany']/text()").extract()
        item["num"]=response.xpath("//span[@class='lsalary']/text()").extract()
        #print(item["title"])
        yield item

