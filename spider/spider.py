#coding=utf-8
from bs4 import BeautifulSoup
import requests

class TY:
    def __init__(self,baseurl,args):
        self.baseurl=baseurl
        self.args='/'+str(args)

    # def login(self,uname,pwd):
    def gotoPage(self,pageNum):
        st=self.args.split('.')[0]
        templist=st.split('-')
        templist[-1]=str(pageNum)
        # print templist
        newurl='-'.join(templist)+'.shtml'
        print newurl
        url = self.baseurl + newurl
        # r = requests.get(url)
        return url

    def getTotalPages(self):
        url = self.baseurl + self.args
        r = requests.get(url)
        soup=BeautifulSoup(r.content,'html.parser')
        # href=soup.select('form > a')[-2]['href']
        totalpageNum=soup.select('form > a')[-2].string
        return int(totalpageNum)

    def getContent(self,lzid,filepath):
        page = self.getTotalPages()
        contents=''
        for i in range(1,page+1):
            url=self.gotoPage(i)
            r=requests.get(url)
            content=r.content
            soup = BeautifulSoup(content, 'html.parser')
            for j in soup.find_all('div',{'_hostid':lzid}):
                 contents=j.select('.bbs-content')[0].get_text().strip()+'\n'
                 self.saveContent(filepath,contents)
        # return contents

    def saveContent(self,filepath,content):
        # content=self.getContent(lzid)
        f = open(filepath,'a+')
        f.write(content)
        f.close()

baseurl='http://bbs.tianya.cn'
page='post-funinfo-6783939-1.shtml'
t=TY(baseurl,page)
t.getContent('91106994','tianya.txt')

