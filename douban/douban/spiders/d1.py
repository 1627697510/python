# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
import os
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class D1Spider(scrapy.Spider):
    name = 'd1'
    allowed_domains = ['douban.com']
    #start_urls = ['http://douban.com/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
    # 编写start_requests()方法，第一次会默认调取该方法中的请求
    def start_requests(self):
        # 首先爬一次登录页，然后进入回调函数parse()
        return [Request("http://douban.com/", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        # 判断是否有验证码
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        if(len(captcha) > 0):
            print("此时有验证码")
            # 将验证码存储到本地
            localpath = "D:/tmp/douban/yzm/captcha.png"
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            captcha_value = input("请到D:/tmp/douban/yzm查看captcha.png中验证码是什么？")
            #cmd="D:/Python27/python.exe D:/Python27/yzm/YDMPythonDemo.py"
            #r = os.popen(cmd)
            #captcha_value = r.read()
            #print("当前验证码自动识别结果为：" + captcha_value)
            data = {
                "captcha - solution": captcha_value,
                "redir": "https://www.douban.com",
                "form_email": "202364932@qq.com",
                "form_password": "xh177151..",

            }
        else:
            #设置要传递的post信息，此时没有验证码字段
            data = {
                "redir": "https://www.douban.com",
                "form_email": "202364932@qq.com",
                "form_password": "xh177151..",
            }

        print("登录中…")
        # 通过FormRequest.from_response()进行登陆
        return [FormRequest.from_response(response,
                                          # 设置cookie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          # 设置headers信息模拟成浏览器
                                          headers=self.header,
                                          # 设置post表单中的数据
                                          formdata=data,
                                          # 设置回调函数，此时回调函数为next()
                                          callback=self.next,
                                          )]

    def next(self, response):
        # response是
        fh = open("C:/code/14douban/yzm/test.html", 'w')
        fh.write(response.text)
        fh.close()
        title = response.xpath("/html/head/title/text()").extract()
        print(title)

