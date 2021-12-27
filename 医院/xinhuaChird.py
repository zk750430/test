import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import urllib3



def lottery():
    # url地址通过抓包工具Charles获取
    print("=================")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    url = 'http://xinhua.51tingyi.com/common/api?cmd=DoctorDetailApp&doctorid=27409&nowday=0&platform=m&sectionname='
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B)'
                      ' WindowsWechat(0x63040026)',
        'Cookie': 'JSESSIONID=4AF43B9A18D59A5499BE2A5BD50319EF',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'http://xinhua.51tingyi.com/doctor/detail?id=27409&hospitalid=34&sectionname=&nowday=0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive'
    }
    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    str1 = res.text[48:len(res.text) - 1]
    json_object = json.loads(str1)
    clinicinfo =json_object["clinicinfo"]
    if len(clinicinfo) == 0 :
        list = json.loads(str1)["cliniclist"]
        for index, item in enumerate(list):
            list1 = item["list"]
            for item1 in list1:
                if item1["statustext"] != "约满" and item1["date"]<"2021-11-30":
                    print(item["name"])
                    print("日期：" + item1["date"]+" "+item1["time"] + "，状态：" + item1["statustext"]+"，价钱："+item1["regfee"])
        print("                 ")

urllib3.disable_warnings()
scheduler = BlockingScheduler()
# 定时任务，5秒一次
scheduler.add_job(id='shares', func=lottery, max_instances=10, trigger='cron', second='*/5')
time_hour = time.strftime('%H:%M', time.localtime())

scheduler.start()

# if __name__ == "__main__":
#     lottery()