import requests
import re
import json
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
def get_one_page(url):
    resposnse=requests.get(url,headers=headers)
    if resposnse.status_code==200:
        return resposnse.text
    return None
def pase_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items=re.findall(pattern,html)
    for i in items:
        with open('top100.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(i, ensure_ascii=False) + '\n')
def main():
    url='http://maoyan.com/board/4'
    c=[x for x in range(0,101) if x%10==0]
    for i in c:
        url='http://maoyan.com/board/4'+"?offset="+str(i)
        html=get_one_page(url)
        pase_one_page(html)
main()
