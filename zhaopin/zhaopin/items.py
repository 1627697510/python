# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title=scrapy.Field()
    #工资
    salary=scrapy.Field()
    #公司
    company=scrapy.Field()
    #工作地点
    location=scrapy.Field()
    #发布时间
    rt=scrapy.Field()
    #截止日期
    deadline=scrapy.Field()
    #招聘人数
    num=scrapy.Field()

