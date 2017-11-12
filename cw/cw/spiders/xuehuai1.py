# -*- coding: utf-8 -*-
import scrapy


class Xuehuai1Spider(scrapy.Spider):
    name = 'xuehuai1'
    allowed_domains = ['wxit.edu.cn']
    start_urls = ['http://wxit.edu.cn/']

    def parse(self, response):
        pass
