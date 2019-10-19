import requests
from bs4 import BeautifulSoup
url="https://www.zhihu.com/hot"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Cookie":'_zap=ac4edd70-2815-4ffa-97a7-046c4ed8216f; d_c0="AMCqKBc7fg-PTsU649pVCIFLejex19RNH5M=|1558949244"; q_c1=76cd5474ffe74ca1931d5938b0cad2d4|1558949245000|1558949245000; _xsrf=Em4zSlDwOcrCnKogYrcMlmj9nmlV5NTJ; capsion_ticket="2|1:0|10:1559539043|14:capsion_ticket|44:NDdlMzczZmNmYTE0NDJiMTkxNjcyYWJlNDEzZWM0NWU=|386fa632684b6ff62497660102c9e0f980fc508341b8a4130ed43e85b41cae96"; z_c0="2|1:0|10:1559539052|4:z_c0|92:Mi4xT3p3YUJ3QUFBQUFBd0tvb0Z6dC1EeWNBQUFDRUFsVk5hem9jWFFCbnJsWFFMSFJBc21GTkpfRWRPTERNMWhhMFln|ce14189a0bbb2c19ede433d2ee1ea9cc40a27642317541d653e8156736d47d71"; tst=r; tgw_l7_route=116a747939468d99065d12a386ab1c5f'
}
#获取txt
r=requests.get(url,headers=headers)
#用两个参数初始化soup
soup=BeautifulSoup(r.text,"lxml")
#获取title
c=soup.find_all(attrs={"class":"HotItem-title"})
#获取title的url
d=soup.select("a")

def geturl(d):
    list=[]
    for i in d:
        if type(i.get("href"))==str and len(i.get("href"))>35:
            if i.get("href") not in list:
                list.append(i.get("href"))
    return list
def gettitle(c,list):
    n=0
    for i in c:
        n=n+1
        with open("zhihu.txt","a",encoding="utf-8") as g:
            g.write("{0}.{1}".format(n,i.string))
            g.write("-----{0}".format(list[n-1]))
            g.write("\n")
#soup.prettify()格式化输出html
print(soup.prettify())
if __name__=="__main__":
    list=geturl(d)
    gettitle(c,list)



