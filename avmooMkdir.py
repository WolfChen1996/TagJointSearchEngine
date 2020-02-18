from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import random
import ssl
import re
import os
print("Resdy?")

my_headers=[
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

#新建标签目录
url = "https://avmask.com/cn/genre"
randdom_header=random.choice(my_headers)  
  
req = urllib.request.Request(url)
req.add_header("User-Agent",randdom_header)
req.add_header("GET",url)

response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print("Get Html")
#print(html)


html=re.findall(r'主题.*其他',html,re.S)
#print(html)

reg1 = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)'
reg_url = re.compile(reg1)
urllist = reg_url.findall(html[0])
#for url in urllist:
#    print(url[0])

reg2 = r'>.*<'
reg_tag = re.compile(reg2)
taglist = reg_tag.findall(html[0])
print("Go!")
id=0
while id<len(urllist):
    url=urllist[id]
    tag=taglist[id]
    name=tag.replace('<','')
    name=name.replace('>','')
    dirnow=os.getcwd()
    dirnew=dirnow+'\\avmoo\\'+str(id)+name
    os.mkdir(dirnew)
    print(str(id)+name,url[0])
    id=id+1
print("Done")
