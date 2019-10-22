import requests
from lxml import etree

ss=input("输入Cookie:")
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Cookie":ss,
}
def get_teacherdata():
    teacherdata_url = "http://218.198.176.244/etses/student/studentEvalAction_evaTeacher.action?_=1571648340787"
    r1=requests.get(teacherdata_url,headers=headers)
    html=etree.HTML(r1.text)
    rr=html.xpath('//select[@id="courseSelect"]//option[@value]/@value')
    list=rr[1::]
    for j in list:
        teacher_name_url="http://218.198.176.244/etses/student/studentEvalAction_getTeachByCountId.action"
        data={
            "couno":j,
        }
        r2=requests.post(teacher_name_url,headers=headers,data=data)
        a=r2.text
        write_mk_url="http://218.198.176.244/etses/student/studentEvalAction_validateAndSaveEval.action"
        data={
            "stutotea.counid":j, "stutotea.teano":a[0][0],  "eid": "1000000017", "weight": "15", "mark": "4",
            "eid": "1000000018", "weight":"10", "mark": "5", "eid": "1000000019", "weight":"20", "mark": "3",
            "eid": "1000000020", "weight":"15", "mark": "4", "eid":  "1000000021","weight":"15", "mark":"5",
            "eid":"1000000022","weight": "10","mark": "4","eid": "1000000023","weight": "10","mark": "4",
            "eid": "1000000024","weight": "5","mark": "4","stutotea.othcomments":"满意！"
                }
        r3=requests.post(write_mk_url,headers=headers,data=data)
        print("评价成功 ！！！")

if __name__=="__main__":
    get_teacherdata()
