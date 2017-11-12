# -*- coding: utf-8 -*-
import scrapy
from dangdang1.items import DangdangItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'mydangdang'
    allowed_domains = ['http://www.dangdang.com/']
    start_urls = ['http://search.dangdang.com/?key=%CD%E2%CC%D7%C5%AE&act=input&page_index=1']
    def start_requests(self):
        urls = []
        for i in range(1, 81):
            current_url = 'http://search.dangdang.com/?key=%CD%E2%CC%D7%C5%AE&act=input&page_index=' + str(i)
            urls.append(current_url)
        print(urls)
        for url in urls:
            yield Request(url=url, callback=self.parse)
    def parse(self, response):
        item=DangdangItem()
        item["title"] = response.xpath('//a[@name="itemlist-picture"]/@title').extract()
        item['link'] = response.xpath('//a[@name="itemlist-picture"]/@href').extract()
        item['comment'] = response.xpath("//a[@dd_name='单品评论']/text()").extract()
        yield item
