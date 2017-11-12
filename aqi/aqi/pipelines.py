# -*- coding: utf-8 -*-
import pymysql
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AqiPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="aqi", charset="utf8")
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            print("正在处理：" + title)
            link=item["link"][i]
            tostar=item["tostar"][i].strip()
            print(tostar)
            #print(title + ":" + link + ":" + tostar)
            sql= "insert into dy(title,link,tostar) values ('" + title + "','" + link + "','" + tostar + "')"
            print(sql)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as err:
                print(err)
        conn.close()
        return item
