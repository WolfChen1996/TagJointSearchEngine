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


#标签名字
tagname="130空中小姐"
#标签网址
urlo = "https://avmask.com/cn/genre/b8b2bd826e38bb9a"
pageid=6
while pageid<=200:
    pageid=pageid+1
    print("-" * 50)
    print("第"+str(pageid)+"页")
    url=urlo+"/page/"+str(pageid)
    randdom_header=random.choice(my_headers) 

    req = urllib.request.Request(url)
    req.add_header("User-Agent",randdom_header)
    req.add_header("GET",url)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)

    html = response.read().decode('utf-8')
    #print("Get Html")
    #print(html)
    if not("404 Not Found" in html):
        html=re.findall(r'waterfall.*class="hidden-xs',html,re.S)
        #print("Get Body")
        #print(html[0])

        soup = BeautifulSoup(html[0],'html.parser')

        #链接
        a_href=soup.findAll("a")

        #图片
        img_src=soup.findAll("img")

        #番号
        reg3 = r'date>.*> / <'
        reg_id = re.compile(reg3)
        idlist = reg_id.findall(html[0])

        #保存
        dirnow=os.getcwd()
        while len(idlist)>0:
            id=idlist.pop()
            id=id.replace('date>','')
            id=id.replace('</ / <','')
            href=a_href.pop()
            img=img_src.pop()
            fhref=href.get('href')
            fimg=img.get('src')
            #print("番号: "+id+" 链接:"+fhref+" 封面:"+fimg)
            print(id)
            
            fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'.txt'
            imgaddress=dirnow+'\\avmoo\\img\\'+id+'.jpg'
            if os.path.isfile(fileaddress):
                f = open(fileaddress, "r")
                str1 = f.readline()
                f.close()
                if(str1==fhref):
                    print("已存在")
                else:#请忽略这种沙雕写法
                    fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                    imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                    dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                    if os.path.isfile(fileaddress):
                        fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                        imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                        dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                        if os.path.isfile(fileaddress):
                            fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                            imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                            dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                            if os.path.isfile(fileaddress):
                                fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                                imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                                dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                                if os.path.isfile(fileaddress):
                                    fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                                    imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                                    dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                                    if os.path.isfile(fileaddress):
                                        fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                                        imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                                        dirnew=dirnow+'\\avmoo\\img\\'+id+"a"
                                        if os.path.isfile(fileaddress):
                                            fileaddress=dirnow+'\\avmoo\\'+tagname+'\\'+id+'a.txt'
                                            imgaddress=dirnow+'\\avmoo\\img\\'+id+'a.jpg'
                                            dirnew=dirnow+'\\avmoo\\img\\'+id+"a"

                    
                    f=open(fileaddress, "w+")
                    f.write(fhref)
                    f.close()

                    reqnew = urllib.request.Request(fhref)
                    reqnew.add_header("User-Agent",randdom_header)
                    reqnew.add_header("GET",fhref)

                    responsenew = urllib.request.urlopen(reqnew,context=context)
                    htmlnew = responsenew.read().decode('utf-8')
                    #print("Get Html")
                    #print(html)

                    htmlnew=re.findall(r'bigImage.*title',htmlnew,re.S)
                    #print("Get Body")
                    #print(html[0])

                    reqnew = urllib.request.Request(fhref)
                    reqnew.add_header("User-Agent",randdom_header)
                    reqnew.add_header("GET",fhref)

                    responsenew = urllib.request.urlopen(reqnew,context=context)
                    htmlnew = responsenew.read().decode('utf-8')
                    #print("Get Html")
                    #print(htmlnew)

                    bs = BeautifulSoup(htmlnew,"html.parser")

                    bsf=bs.find_all(name='a',attrs={"class":"bigImage"})
                    #大图url
                    #print(bsf[0]['href'])
                    r = requests.get(bsf[0]['href'], stream=True)
                    #print(r.status_code)
                    if r.status_code == 200:
                        open(imgaddress, 'wb').write(r.content)
                        print("大图下载完成")
                    del r
                    os.mkdir(dirnew)
                    imgid=1
                    for a in bs.find_all(name='a',attrs={"class":"sample-box"}):
                        #print(a["href"])
                        r = requests.get(a["href"], stream=True)
                        #print(r.status_code)
                        if r.status_code == 200:
                            dirf=dirnew+"\\"+str(imgid)+".jpg"
                            open(dirf, 'wb').write(r.content)
                            #print("预览图"+str(imgid)+"下载完成")
                        del r
                        imgid=imgid+1
                    print("已添加")
                    
            else:
                f=open(fileaddress, "w+")
                f.write(fhref)
                f.close()


                reqnew = urllib.request.Request(fhref)
                reqnew.add_header("User-Agent",randdom_header)
                reqnew.add_header("GET",fhref)

                responsenew = urllib.request.urlopen(reqnew,context=context)
                htmlnew = responsenew.read().decode('utf-8')
                #print("Get Html")
                #print(html)

                htmlnew=re.findall(r'bigImage.*title',htmlnew,re.S)
                #print("Get Body")
                #print(html[0])

                reqnew = urllib.request.Request(fhref)
                reqnew.add_header("User-Agent",randdom_header)
                reqnew.add_header("GET",fhref)

                responsenew = urllib.request.urlopen(reqnew,context=context)
                htmlnew = responsenew.read().decode('utf-8')
                #print("Get Html")
                #print(htmlnew)

                bs = BeautifulSoup(htmlnew,"html.parser")

                bsf=bs.find_all(name='a',attrs={"class":"bigImage"})
                #大图url
                #print(bsf[0]['href'])
                r = requests.get(bsf[0]['href'], stream=True)
                #print(r.status_code)
                if r.status_code == 200:
                    open(imgaddress, 'wb').write(r.content)
                    print("大图下载完成")
                del r

                dirnow=os.getcwd()
                dirnew=dirnow+'\\avmoo\\img\\'+id
                os.mkdir(dirnew)
                imgid=1
                for a in bs.find_all(name='a',attrs={"class":"sample-box"}):
                    #print(a["href"])
                    r = requests.get(a["href"], stream=True)
                    #print(r.status_code)
                    if r.status_code == 200:
                        dirf=dirnew+"\\"+str(imgid)+".jpg"
                        open(dirf, 'wb').write(r.content)
                        #print("预览图"+str(imgid)+"下载完成")
                    del r
                    imgid=imgid+1
                print("已添加")

    else:
        pageid=201