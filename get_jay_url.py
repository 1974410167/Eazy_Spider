import requests
from urllib import error
from lxml import etree
from bs4 import BeautifulSoup
import json

headers1={
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Content-Length": "42",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Cookie":"migu_cookie_id=963b271b-fe41-4fe9-89ef-72a040d92316-n41573887195933; migu_music_status=true; migu_music_uid=0554c735-1740-4d61-8a2d-d1d6994ab957; migu_music_avatar=%252F%252Fcdnmusic.migu.cn%252Fv3%252Fstatic%252Fimg%252Fcommon%252Fheader%252Fdefault-avatar.png; migu_music_nickname=%E5%92%AA%E5%92%95%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=15738698290; migu_music_email=; migu_music_passid=6101841419911; migu_music_sid=s%3AVej67mTsFNiH6_kSyc1Os7RHN7MFbMfG.A20EteeV7uIypwPxjdwP6nVxElmd3KUasNmdrYkO26M; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574154618148:ss=1574154618148; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574154618655:ss=1574154618655",
"Host": "music.migu.cn",
"Origin": "http://music.migu.cn",
"Referer": "http://music.migu.cn/v3/music/order/download/60054701923",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
"X-Requested-With": "XMLHttpRequest",
}

vip=["60054704106","60054704093"]

def get_url():
    dict={}
    headers={
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        "Cookie": "migu_cookie_id=963b271b-fe41-4fe9-89ef-72a040d92316-n41573887195933; migu_music_status=true; migu_music_uid=0554c735-1740-4d61-8a2d-d1d6994ab957; migu_music_avatar=%252F%252Fcdnmusic.migu.cn%252Fv3%252Fstatic%252Fimg%252Fcommon%252Fheader%252Fdefault-avatar.png; migu_music_nickname=%E5%92%AA%E5%92%95%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=15738698290; migu_music_email=; migu_music_passid=6101841419911; migu_music_sid=s%3Az2Btt-Or5WdaeQABqjp_RIt_FIiQKKjb.x%2BY23hZX%2BVSEtf2HgRRrCaNbmiQ%2FVifEWSBMrKvEuJc; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574073433347:ss=1574073433347; WT_FPC=id=2c2cd0d12fa075a03851573887196501:lv=1574073433854:ss=1574073433854",
    }
    for i in range(2,16):
        url="http://music.migu.cn/v3/music/artist/112/song?page="+str(i)
        Xpth1 = "//a[@data-type='crbt']/@data-id"
        Xpth2 = "//a[@class='song-name-txt']/@title"


        r=requests.get(url,headers=headers)
        html=etree.HTML(r.text)

        xpth1=html.xpath(Xpth1)
        xpth2=html.xpath(Xpth2)

        L=len(xpth1)
        for aa in range(L):
            dict[xpth2[aa]]=xpth1[aa]
            if aa in [0,1]:
                for j in vip:
                    if j in dict.values():
                        del dict[xpth2[aa]]

    url = "http://music.migu.cn/v3/api/order/download"
    for k in dict:
        data={
            "copyrightId":dict[k],
            "payType": "00",
            "type": "1",
        }
        r = requests.post(url, data=data, headers=headers1)

        print(r.text)
        print(type(r.text))

        a = json.loads(r.text)
        urls = a.get("downUrl")
        dict[k]=urls

    with open("dict_url.txt", "a", encoding="utf-8") as f22:
        f22.writelines(json.dumps(dict, ensure_ascii=False))

    print(dict)
    print(len(dict))
    return dict

if __name__=="__main__":

    get_url()
