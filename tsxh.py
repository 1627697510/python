import urllib.request
import random
import re
from scrapy.http import Request
from lxml import etree
uapools = [
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 OPR/37.0.2178.32",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    ]

#使用用户代理
def ua(uapools):
    this_ua=random.choice(uapools)
    headers=("User-Agent",this_ua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
fh=open("D:/tsxh/tsxh.txt","w")
ua(uapools)
url="http://www.xxbiquge.com/0_547/"
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
#print(len(data))
pat='<dd>(<a href=".*?">.*?</a>)</dd>'
rst=re.compile(pat).findall(data)
#print(rst)
for i in rst:
    treedata=etree.HTML(i)
    cat_link=treedata.xpath("//a/@href")
    cat_name=treedata.xpath("//a/text()")
    #print(cat_link)
    cat_id=cat_link[0][7:18]
    #print(cat_id)
    urls=[]
    for j in cat_link:
        ua(uapools)
        try:
            thisurl='http://www.xxbiquge.com'+str(j)
            thisdata=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
            thispat='<div id="content">.*?<br /><br />(.*?)</div>'
            thisrst=re.compile(thispat,re.S).findall(thisdata)
            print(thisrst)
            for z in range(0,len(thisrst)):
                fh.write(str(thisrst[z])+"\n")
                print(len(thisrst))
        except Exception as err:
            print(err)
fh.close()



