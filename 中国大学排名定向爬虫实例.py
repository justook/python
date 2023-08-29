import requests as r
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        rr = r.get(url,timeout= 30)
        rr.raise_for_status
        rr.encoding = rr.apparent_encoding
        return rr.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    soupinfo = soup.find_all("tr")
    soupinfo.pop(0)
    for tr in soupinfo:
         school = []
         for name in tr.descendants:
            #  ulist.append(str(name.string))
             school.append(name.string)
         ulist.append(school)    
             

def printUnivList(ulist,num):
    for i in range(num):
        print(ulist[i])

def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2023'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20 univ

main()
input()