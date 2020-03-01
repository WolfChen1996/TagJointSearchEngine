from bs4 import BeautifulSoup
from retrying import retry
import urllib
import urllib.request
import requests
import random
import ssl
import os
import time

#网址
urlo = "http://avmask.com/cn/released"
#起始页130
pageid=130

#################################################
my_headers=[
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
]
dirnow=os.getcwd()

def trygethtml(req,context):
    attempts = 0
    success = False
    while attempts < 10 and not success:
        try:
            response = urllib.request.urlopen(req,context=context,timeout=30)
            success = True
        except:
            print(response)
            attempts += 1
            if attempts == 10:
                break
    return response

def trygetimg(url):
    attempts = 0
    success = False
    while attempts < 10 and not success:
        try:
            r = requests.get(url,stream=True,timeout=20)
            success = True
        except:
            print("E")
            attempts += 1
            if attempts == 10:
                break
    return r

while pageid>0:
    print("-" * 50)
    print("第"+str(pageid)+"页")
    print("-" * 50)
    url=urlo+"/page/"+str(pageid)
    #爬虫防屏蔽脑袋
    randdom_header=random.choice(my_headers) 
    req = urllib.request.Request(url)
    req.add_header("User-Agent",randdom_header)
    req.add_header("GET",url)
    context = ssl._create_unverified_context()

    response=trygethtml(req,context)

    #开始表演
    html = response.read().decode('utf-8')
    print("Get Html")
    
    if not("404 Not Found" in html):

        soup = BeautifulSoup(html,'html.parser')
        body=soup.find(name='div',attrs={"id":"waterfall"})
        #print(body)
        itemlist=soup.findAll(name='div',attrs={"class":"item"})

        for i in range(0,len(itemlist)):
            print(pageid)
            #获取基础信息
            #print(itemlist[i])
            atag=itemlist[i].find(name='a',attrs={"class":"movie-box"})
            date=itemlist[i].findAll(name='date')
            img=atag.find(name='img')

            #基础信息
            href=atag['href']
            avname=img['title']
            avid=date[0].string
            avdate=date[1].string
            print("/" * 50)

            fileaddress=dirnow+'\\all\\'+avid+'_'+avdate+'.txt'
            imgaddress=dirnow+'\\img\\'+avid+'_'+avdate+'.jpg'
            
            if os.path.isfile(fileaddress):
                f = open(fileaddress, "r")
                str1 = f.readline()
                f.close()
                print(avid+"已存在")
            else:
                #先写先得
                f=open(fileaddress, "w+")
                f.write(href)
                #f.write('\r\n')
                #f.write(avname)
                f.close()
                
                print(avid)
                
                reqnew = urllib.request.Request(href)
                reqnew.add_header("User-Agent",randdom_header)
                reqnew.add_header("GET",href)
                responsenew=trygethtml(reqnew,context)
                htmlnew = responsenew.read().decode('utf-8')



                bs = BeautifulSoup(htmlnew,"html.parser")
                

                bsf=bs.find_all(name='a',attrs={"class":"bigImage"})

                r=trygetimg(bsf[0]['href'])
                if r.status_code == 200:
                    open(imgaddress, 'wb').write(r.content)
                    print("大图下载完成")
                del r

                '''
                #预览图部分
                dirnew=dirnow+'\\img\\'+avid+'_'+avdate
                if not os.path.isdir(dirnew):
                    os.mkdir(dirnew)
                localtime = time.asctime( time.localtime(time.time()) )
                print(localtime,"开始下载预览图")
                imgid=1
                for a in bs.find_all(name='a',attrs={"class":"sample-box"}):
                    r=trygetimg(a["href"])
                    if r.status_code == 200:
                        dirf=dirnew+"\\"+str(imgid)+".jpg"
                        open(dirf, 'wb').write(r.content)
                        print(imgid)
                        #print("预览图"+str(imgid)+"下载完成")
                    del r
                    imgid=imgid+1
                '''

                taglist=bs.findAll(name='span',attrs={"class":"genre"})
                for a in range(0,len(taglist)):
                    taghref=taglist[a].find(name='a')['href']
                    tagdir=taglist[a].string+taghref[-3]+taghref[-2]+taghref[-1]
                    if os.path.isdir(dirnow+'\\avmoo\\'+tagdir):
                        f=open(dirnow+'\\avmoo\\'+tagdir+"\\"+avid+'_'+avdate+'.txt', "w+")
                        f.write(href)
                        f.close()
                        
                #print("已添加")
		#详情页下载结束
            
        else:
            print("N")
            qp = os.system('cls')
    
    else:
        pageid=-2
    pageid=pageid+1
