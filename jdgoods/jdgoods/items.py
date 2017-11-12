# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdgoodsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # book_id:可以用于获取price与评价数
    book_id = scrapy.Field()
    # 书名
    book_name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 评价数
    rate_count = scrapy.Field()
    # 作者1
    author1 = scrapy.Field()
    # 作者2
    # author2 = scrapy.Field()
    # 出版社
    pub = scrapy.Field()
    # 店铺名
    seller = scrapy.Field()
    # 书的详情链接
    book_link = scrapy.Field()
    # 1级分类
    cat1_name = scrapy.Field()
    # 2级分类
    cat2_name = scrapy.Field()
