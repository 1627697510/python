# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SuningPipeline(object):
    def process_item(self, item, spider):
        conn= pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="suning", charset="utf8")
        for i in range(0,len(item["name"])):
            name=item["name"][i]
            print("正在处理:"+name)
            link=item["link"][i]
            seller=item["seller"][i]
            evalute=item["evalute"][i]
            #print(name+":"+link+":"+seller+":"+evaluate)
            sql="insert into sunings(name,link,seller,evalute) values ('"+name+"','"+link+"','"+seller+"','"+evalute+"')"
            print(sql)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as err:
                print(err)
        conn.close()
        return item
