import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
vid="1744194068"
cid="6313059303104884898"
num=""
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
         "Content-Type":"application/javascript"
}
opener=urllib.request.build_opener()
headall=[]
for key, value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
for j in range(0,100):
    print("page " + str(j))
    thisurl="https://coral.qq.com/article/" + vid + "/comment?commentid=" + cid
    data=urllib.request.urlopen(thisurl).read().decode("utf-8")
    contentpat='"content":"(.*?)"'
    contentall=re.compile(contentpat, re.S).findall(data)
    lastpat='"last":"(.*?)"'
    cid=re.compile(lastpat, re.S).findall(data)[0]
    for i in range(0,len(contentall)):
        try:
            print("conent:" + eval('u"'+contentall[i]+'"'))
            print("----------")
        except Exception as err:
            print(err)
