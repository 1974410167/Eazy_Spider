import requests
from lxml import etree

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
}
urlbase="http://218.198.176.244"
url="http://218.198.176.244/etses/face/userLogin.jsp"
r=requests.get(url,headers=headers)
html=etree.HTML(r.text)
a=html.xpath('//div[@style="margin-top: -13px;"]/span[@class="span"]/img/@src')
for i in a:
    print(urlbase+i)

