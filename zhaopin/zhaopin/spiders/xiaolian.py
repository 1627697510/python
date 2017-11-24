# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from zhaopin.items import ZhaopinItem
from scrapy.http import Request
from lxml import etree

class XiaolianSpider(scrapy.Spider):
    name = 'xiaolian'
    allowed_domains = ['http://m.job9151.com/']
    #start_urls = ['http://m.job9151.com/index.php?m=Mobile&c=Jobs&a=index&m=Mobile&page=1']
    ua=["ozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36",
    ]
    def start_requests(self):
        req = urllib.request.Request("http://m.job9151.com/index.php?m=Mobile&c=Jobs&a=index&m=Mobile&page=1")
        req.add_header("User-Agent", self.ua)
        urls=[]
        for i in range(1,51):
            thisurl='http://m.job9151.com/index.php?m=Mobile&c=Jobs&a=index&m=Mobile&page='+str(i)
            urls.append(thisurl)
        print(urls)
        for url in urls:
            yield Request(url=url, callback=self.parse)


    def parse(self, response):
        pass
        '''
        item=ZhaopinItem()
        item["title"]=response.xpath("//div[@class='job-name substring font16']/text()").extract()
        item["salary"]=response.xpath("//div[@class='salary']/text()").extract()
        item["company"]=response.xpath("//div[@class='company-name substring']/text()").extract()
        item["location"]=response.xpath("//div[@class='district substring']/text()").extract()
        print(item["title"])
        #yield item
        '''

