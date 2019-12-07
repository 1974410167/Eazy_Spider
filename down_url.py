import requests
import json
from urllib import error
from concurrent.futures import as_completed,thread,ThreadPoolExecutor
url="http://218.200.160.7/wlansst?pars=CI=600547004982600902000003281403/F=020007/T=56160775624100/CH=2a257d4c-1ee0-4ad8-8081-b1650c26390a/S=17a5b425e6/FN=%E5%A5%BD%E4%B9%85%E4%B8%8D%E8%A7%81_%E5%91%A8%E6%9D%B0%E4%BC%A6_128K.mp3"

headers1 = {
    #"Accept": "",
    "Accept - Encoding": "gzip, deflate",
    "Accept - Language": "zh - CN, zh;q = 0.9",
    "Connection": "keep - alive",
    "Host": "218.200.160.7",
    "Referer": "http: // music.migu.cn / v3 / music / order / download / 60054701934",
    "Upgrade - Insecure - Requests": "1",
    "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
}
f = open("dict_url.txt", "r",encoding="utf-8")

v=json.load(f)

def aaa(i):
    if v[i]:
        r=requests.get(v[i],headers=headers1,timeout=(3,7))
        cc=".mp3"
        with open("D://jaymusic//"+i+cc,"wb") as f:
            f.write(r.content)

with ThreadPoolExecutor(max_workers=10) as pool:

    results=pool.map(aaa,v)
    print("--------")
    for j in results:
        print(j)
