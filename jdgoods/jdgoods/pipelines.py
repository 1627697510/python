# -*- coding: utf-8 -*-
import pymysql
import urllib.request
import random
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdgoodsPipeline(object):
    ua = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    ]
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="jd", charset="utf-8")
        for i in range(0, len(item["book_id"])):
            book_id = item["book_id"][i]
            print("正在存储图书（id）:" + str(book_id))

            # 根据book_id，获取price, rate_count
            # 获取价格
            price_url = "http://p.3.cn/prices/mgets?skuIds=J_" + str(book_id)
            price_request = urllib.request.Request(price_url)
            price_request.add_header("User-Agent", random.choice(self.ua))
            # 返回的数据是字符串：[{"op":"61.40","m":"78.00","id":"J_11254622","p":"61.40"}]
            price_data_json = urllib.request.urlopen(price_request).read().decode("gb2312", "ignore")
            print(price_data_json)
            # loads方法可将字符串转化为List
            price_data = json.loads(price_data_json)
            # item["price"] = price_data
            price = price_data[0]['p']
            # item["price"] = price

            # 获取rate_count
            rate_url = "http://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(book_id)
            rate_request = urllib.request.Request(rate_url)
            rate_request.add_header("User-Agent", random.choice(self.ua))
            # 返回的数据是字符串：[{"op":"61.40","m":"78.00","id":"J_11254622","p":"61.40"}]
            rate_data_json_str = urllib.request.urlopen(rate_request).read().decode("gb2312", "ignore")
            print(rate_data_json_str)
            # loads方法可将字符串转化为List(python对象)
            rate_data_json = json.loads(rate_data_json_str)
            # item["price"] = price_data
            rate_count = rate_data_json['CommentsCount'][0]['CommentCountStr']

            book_name = item["book_name"][i].strip()
            # 作者1
            author1 = item["author1"][i].strip()
            # 作者2
            # author2 = item["author2"][i]
            # 出版社
            pub = item["pub"][i].strip()
            # 店铺名
            seller = item["seller"][i].strip()
            # 书的详情链接
            book_link = item["book_link"][i].strip()
            # 1级分类
            cat1_name = item["cat1_name"]
            # 2级分类
            cat2_name = item["cat2_name"]

            print("一级目录：" + cat1_name)
            print("二级目录：" + cat2_name)
            print("书名：" + book_name.strip())
            print("书链接：" + book_link)
            print("作者：" + author1)
            print("出版社：" + pub)
            print("价格：" + price)
            print("店铺名：" + seller)

            sql = "insert into jd_book(" \
                  "id, book_name, price, rate_count, author1, " \
                  "pub, seller, book_link, cat1_name, cat2_name) values('" \
                  + book_id + "','" + book_name + "','" + price + "', '" \
                  + rate_count + "','" + author1 + "','" \
                  + pub + "','" + seller + "','" + book_link + "','" + cat1_name + "', '" + cat2_name + "')"
            print("sql:" + sql)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as err:
                print(err)
        conn.close()
        return item
