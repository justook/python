import requests
import re

def gethtmltext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parserage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")


def printgoodslist(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt :
        count += 1
        print(tplt.format(count,g[0],g[1]))
        
    
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q='+ goods
    infolist = []
    for i in range(depth):
        try :
             url = start_url + '&s=' + str(44*i)
             html = gethtmltext(url)
             parserage(infolist,html)
        except :
            continue
    printgoodslist(infolist)

main()
