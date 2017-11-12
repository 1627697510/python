# -*- coding: utf-8 -*-
import scrapy
import re
from aqi.items import AqiItem
from scrapy.http import Request
import time
import urllib.request
import random



class AiSpider(scrapy.Spider):
    name = 'ai'
    allowed_domains = ['http://iqiyi.com/']
    start_urls = ['http://www.iqiyi.com/lib/dianying/%2C%2C_11_1.html']
    ua = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    ]

    def start_requests(self):
        allid = ['dianying', 'dianshiju', 'zogyi', 'dongman']
        urls = []
        for k in range(0, len(allid)):
            for i in range(1, 101):
                current_url = 'http://www.iqiyi.com/lib/'+allid[k]+'/%2C%2C_11_'+str(i)+'.html'
                urls.append(current_url)
            print(urls)
            for url in urls:
                yield Request(url=url, callback=self.parse)

    def parse(self, response):
        item=AqiItem()
        item["title"]=response.xpath("//a[@class='site-piclist_pic_link']/@title").extract()
        item["link"]=response.xpath("//a[@class='site-piclist_pic_link']/@href").extract()
        item["tostar"]=response.xpath("//div[@class='role_info']/em/a/text()").extract()
        print(item["tostar"])
        yield item

