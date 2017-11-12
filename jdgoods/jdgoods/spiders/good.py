# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jdgoods.items import JdgoodsItem
from scrapy.http import Request
from lxml import etree
import json

import ssl
ssl._create_default_https_context = ssl._create_unverified_context



class GoodSpider(scrapy.Spider):
    name = 'good'
    allowed_domains = ['jd.com']
    #start_urls = ['http://jd.com/']
    ua = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    ]
    def start_requests(self):
        all_channel_request = urllib.request.Request("http://book.jd.com/booksort.html")
        all_channel_request.add_header("User-Agent", random.choice(self.ua))
        # 字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
        # 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
        # decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
        # encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
        all_channel_data = urllib.request.urlopen(all_channel_request).read().decode("gb2312", "ignore")
        pat_cat1_cat2 = '(<dt>.*?</dd>)'
        all_cat_list = re.compile(pat_cat1_cat2).findall(all_channel_data)
        sort_kv = {}
        # x = 0
        for cat in all_cat_list:
            # if x > 1:
            #     break
            treedata = etree.HTML(cat)
            # 取出某个一级目录，包含其二级目录
            cat1_link = treedata.xpath("//dt/a/@href")
            cat1_name = treedata.xpath("//dt/a/text()")
            # 获得的url是//list.jd.com/1713-3258-3297.html
            # 需要转换为http://list.jd.com/list.html?cat=1713,3258,3297
            cat2_link = treedata.xpath("//dd//a/@href")
            cat2_id = cat2_link[0][14:-5].replace("-", ",")
            cat2_url = "http://list.jd.com/list.html?cat=" + cat2_id
            cat2_name = treedata.xpath("//dd//a/text()")
            print("当前一级目录的链接：" + cat1_link[0])
            print("当前一级目录的名字：" + cat1_name[0])
            # x += 1
            for i in range(0, len(cat2_link)):
                # if i > 0:
                #     break
                print("当前二级目录的链接：" + cat2_url)
                print("当前二级目录的名字：" + cat2_name[0])
                url = cat2_url
                first_page_request = urllib.request.Request(url)
                first_page_request.add_header("User-Agent", random.choice(self.ua))
                first_page_data = urllib.request.urlopen(first_page_request).read().decode("gb2312", "ignore")
                treedata = etree.HTML(first_page_data)
                sum_page_count = treedata.xpath("//div[@class='f-pager']//i/text()")[0]
                for page_num in range(0, int(sum_page_count)):
                    # if page_num > 1:
                    #     break
                    page_url = url + "&page=" + str(page_num + 1)
                    print("正在处理第" + str(page_num + 1) + "页" + page_url)
                    request = Request(url=page_url, callback=self.parse)
                    request.meta['cat1_name'] = cat1_name[0]
                    request.meta['cat2_name'] = cat2_name[i]
                    request.meta['request_url'] = page_url
                    yield request

    def parse(self, response):
        # 开始抓取某个2级目录（cat）中的每一本书的详情
        item = JdgoodsItem()
        item['cat1_name'] = response.meta['cat1_name']
        item['cat2_name'] = response.meta['cat2_name']
        item['book_name'] = response.xpath("//div[@id='plist']//div[@class='p-name']/a/em/text()").extract()
        item['book_link'] = response.xpath("//div[@id='plist']//div[@class='p-name']/a/@href").extract()
        item['author1'] = response.xpath(
            "//div[@id='plist']//div[@class='p-bookdetails']//span[@class='author_type_1']/a/text()").extract()
        # 作者2有可能为空
        # item['author2'] = response.xpath(
        #     "//div[@id='plist']//div[@class='p-bookdetails']//span[@class='author_type_2']/a/text()").extract()
        item['pub'] = response.xpath(
            "//div[@id='plist']//div[@class='p-bookdetails']//span[@class='p-bi-store']/a/text()").extract()
        item['seller'] = response.xpath(
            "//div[@id='plist']//div[@class='p-shopnum']//span[@class='curr-shop']/text()").extract()
        item['book_id'] = response.xpath("//div[@class='gl-i-wrap j-sku-item']/@data-sku").extract()
        yield item