

import requests
from lxml import etree
import re

Cookie = input("请输入Cookie:")
print(Cookie)

pattern = re.compile(r'id=(\d{2});')
semesterId = pattern.findall(Cookie)[0]
print(semesterId)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    "Cookie": Cookie,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Content-Type':'application/x-www-form-urlencoded',
    'Connection':'keep-alive'
}


pingjiao_url = 'http://218.29.109.240/eams/quality/stdEvaluate.action'

# 请求评教主页，获得老师与课程id相关字符串
resp = requests.get(pingjiao_url, headers=headers)

print(resp.text)
html = etree.HTML(resp.text)

print(html)
# 解析获得老师与课程id列表
lesson_teacher_id = html.xpath("//tbody//a/@href")

evaluationLesson_name = html.xpath("//tbody//tr//td[2]//text()")
teacher_name = html.xpath("//tbody//tr//td[4]//text()")

print(lesson_teacher_id)
print(type(lesson_teacher_id))

submit_url = 'http://218.29.109.240/eams/quality/stdEvaluate!finishAnswer.action'

for i in range(len(lesson_teacher_id)):
    dict = {}

    pattern = re.compile(r'\d+')

    # id_list为一个列表，包含两项，第一项是课程id,第二项是老师id
    id_list = pattern.findall(lesson_teacher_id[i])
    print(id_list)

    # 如果id_list长度为2，则说明未对此老师进行评教
    if len(id_list) == 2:
        print(id_list[1])
        print(id_list[0])
        print("=================================")

        submit_data = {
            "teacher.id": id_list[1],
            "semester.id": semesterId,
            "evaluationLesson.id": id_list[0],
            "result1_0.questionName": "合理利用优质教学资源，备课充分，教态端正，认真组织教学，各环节安排合理，教学有序，辅导答疑、作业批改及时有效，尊重和关爱学生",
            "result1_0.content": "4",
            "result1_0.score": "18.000000000000004",
            "result1_1.questionName": "开课初提供课程提纲和丰富的课程参考资料，告知学生教学目标和要求，明确课程考核标准；充分利用泛雅平台进行教学",
            "result1_1.content": "4",
            "result1_1.score": "9.000000000000002",
            "result1_2.questionName": "教学内容科学充实，逻辑性强，重点、难点突出，具有较丰富的观点、视角和深度、广度",
            "result1_2.content": "4",
            "result1_2.score": "9.000000000000002",
            "result1_3.questionName": "理论与实践相结合，教学内容能较好反映学科发展新思想、新概念、新成果",
            "result1_3.content": "4",
            "result1_3.score": "9.000000000000002",
            "result1_4.questionName": "注重课堂管理与师生互动，有效组织学习活动促进师生、生生之间进行资源共享、问题交流和协作学习，培养学生学习主动性和创新意识",
            "result1_4.content": "5",
            "result1_4.score": "15",
            "result1_5.questionName": "结合课程特点精心设计教学活动，灵活运用恰当的教学方法及新媒体手段进行教学",
            "result1_5.content": "5",
            "result1_5.score": "15",
            "result1_6.questionName": "掌握了这门课程的知识、技能并产生了浓厚的兴趣，收获很大且愿意深入学习",
            "result1_6.content": "5",
            "result1_6.score": "10",
            "result1_7.questionName": "该教师在本课程中的教学表现优秀，愿意把这名教师推荐给其他同学",
            "result1_7.content": "5",
            "result1_7.score": "10",
            "result1Num": "8",
            "result2Num": "0"
        }
        print(submit_data)
        print("=================================")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            "Cookie": Cookie,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            "Referer":"http://218.29.109.240/eams/quality/stdEvaluate!answer.action?evaluationLesson.id="+id_list[0]+"&teacher.id="+"id_list[1]",
        }
        r = requests.post(submit_url, data=submit_data, headers=headers)
        print(r.status_code)
        if r.status_code == 200:
            print(f"{evaluationLesson_name[i]}--{teacher_name[i]}--评教完成！")

print("所有老师皆已评教完成，请在评教页面刷新查看。")

