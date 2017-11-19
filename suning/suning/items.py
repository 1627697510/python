# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #书名
    name=scrapy.Field()
    #书链接
    link=scrapy.Field()
    #店铺名称
    seller=scrapy.Field()
    #评价
    evalute=scrapy.Field()


