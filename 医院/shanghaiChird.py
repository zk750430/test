import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import urllib3



def lottery():
    # url地址通过抓包工具Charles获取
    print("=================")
    url = 'https://wxsrv.scmc.com.cn/common/api?cmd=DoctorDetailApp&doctorid=4187&nowday=0&platform=m&clinname=%E5%84%BF%E4%BF%9D%E7%A7%91'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 '
                      'NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63040026)',
        'Cookie': 'https_waf_cookie=df70664a-f988-414a213111108141665a2bdf7c51066f518a; JSESSIONID=CA960FBDEB68E05B12C8FCD2060E4172',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://wxsrv.scmc.com.cn/doctor/detail?id=4187&hospitalid=32&clinname=%E5%84%BF%E4%BF%9D%E7%A7%91',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive'
    }
    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    str1 = res.text[4:len(res.text) - 1]
    list = json.loads(str1)["cliniclist"]
    for index, item in enumerate(list):
        list1 = item["list"]
        for item1 in list1:
            if item1["statustext"] != "约满" and item1["date"]<"2021-11-30":
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
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