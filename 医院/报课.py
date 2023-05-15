import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import urllib3
from network.mailDemo import sendMail

def lottery():
    # url地址通过抓包工具Charles获取
    print("=================")
    url = "https://bm.qsng.cn/eduplat/api/public/ic/iclass/list?area=0&pageNo=1&pageSize=500&orgId=FF8080813362474F0133683E90B70701&year=2022&term=2&hasSyme=1&spelId="
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'sec - ch - ua': '".Not/A)Brand";v = "99", "Google Chrome";v = "103", "Chromium";v = "103"',
        'sec - ch - ua - mobile': '?0',
        'Sec - Fetch - Dest': 'empty',
        'sec - ch - ua - platform': '"macOS"',
        'Sec - Fetch - Mode': 'cors',
        'Sec - Fetch - Site': 'same - origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'edu.session.id=62afabe3-a474-45e7-81f6-b5da71c180c6',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://bm.qsng.cn/edufront',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-length': '100',
        'Content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'https://bm.qsng.cn',
        'Host': 'bm.qsng.cn'
    }
    params = {
        "area": '0',
        "pageNo": 1,
        "pageSize": 500,
        "orgId": "FF8080813362474F0133683E90B70701",
        "year": '2022',
        "term": '2',
        "hasSyme": 1,
        'spelId': ''
    }
    res = requests.post(url, json=params, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    jsonData = json.loads(res.text)
    # degree 1:高级 3：初级  2：启蒙
    if '0' == jsonData['code']:
        lists = jsonData["data"]['rows']
        surplusNum=[]
        for listData in lists:
            data = listData['bean']
            # if ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum']-data['payNum']) > 1:
            if '中国画' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum']-data['payNum'])>=1 and "3" == data['degree']:
                surplusNum.append("科目名称："+data['spelName']+",程度："+data['caption']['degree']+",上课时间："+data['schedule']+",剩余数量："+str(data['recruitNum']-data['payNum'])+",区域："+data['caption']['area']+"，简介："+data['description'])
                surplusNum.append("\\n")
            elif '卡通画' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum']-data['payNum'])>=1 and "2" == data['degree']:
                surplusNum.append("科目名称："+data['spelName']+",程度："+data['caption']['degree']+",上课时间："+data['schedule']+",剩余数量："+str(data['recruitNum']-data['payNum'])+",区域："+data['caption']['area']+"，简介："+data['description'])
                surplusNum.append("\\n")
            elif '少儿硬笔书法' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum'] - data['payNum']) >= 1 and "3" == data['degree']:
                surplusNum.append("科目名称：" + data['spelName'] + ",程度：" + data['caption']['degree'] + ",上课时间：" + data[
                    'schedule'] + ",剩余数量：" + str(data['recruitNum'] - data['payNum']) + ",区域：" + data['caption'][
                                      'area'] + "，简介：" + data['description'])
            elif '中国舞' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum'] - data['payNum']) >= 1 and "2" == data['degree']:
                surplusNum.append("科目名称：" + data['spelName'] + ",程度：" + data['caption']['degree'] + ",上课时间：" + data[
                    'schedule'] + ",剩余数量：" + str(data['recruitNum'] - data['payNum']) + ",区域：" + data['caption'][
                                      'area'] + "，简介：" + data['description'])
            elif '小学主持人' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum'] - data['payNum']) >= 1 and "3" == data['degree']:
                surplusNum.append("科目名称：" + data['spelName'] + ",程度：" + data['caption']['degree'] + ",上课时间：" + data[
                    'schedule'] + ",剩余数量：" + str(data['recruitNum'] - data['payNum']) + ",区域：" + data['caption'][
                                      'area'] + "，简介：" + data['description'])
            elif '古筝' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum'] - data['payNum']) >= 1 and "3" == data['degree']:
                surplusNum.append("科目名称：" + data['spelName'] + ",程度：" + data['caption']['degree'] + ",上课时间：" + data[
                    'schedule'] + ",剩余数量：" + str(data['recruitNum'] - data['payNum']) + ",区域：" + data['caption'][
                                      'area'] + "，简介：" + data['description'])
            elif '电子琴' in data['name'] and ('周日' in data['schedule'] or '周六' in data['schedule']) and (data['recruitNum'] - data['payNum']) >= 1 and "3" == data['degree']:
                surplusNum.append("科目名称：" + data['spelName'] + ",程度：" + data['caption']['degree'] + ",上课时间：" + data[
                    'schedule'] + ",剩余数量：" + str(data['recruitNum'] - data['payNum']) + ",区域：" + data['caption'][
                                      'area'] + "，简介：" + data['description'])
        if(len(surplusNum)>0):
            # sendMail(str(surplusNum),"1246118299@qq.com","zk","pjj","报名课程剩余数量")
            print(len(surplusNum))

urllib3.disable_warnings()
# scheduler = BlockingScheduler()
# # 定时任务，5秒一次
# scheduler.add_job(id='shares', func=lottery, max_instances=10, trigger='cron', second='*/10')
# time_hour = time.strftime('%H:%M', time.localtime())
#
# scheduler.start()

if __name__ == "__main__":
    lottery()
