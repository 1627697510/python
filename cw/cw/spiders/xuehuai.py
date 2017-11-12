# -*- coding: utf-8 -*-
import scrapy


class XuehuaiSpider(scrapy.Spider):
    name = 'xuehuai'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
