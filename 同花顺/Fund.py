import requests
import ast
from prettytable import PrettyTable
from colorama import Fore
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def lottery():
    # url地址通过抓包工具Charles获取
    url = 'http://qd.10jqka.com.cn/quote.php?cate=real&type=fund&return=json&callback=jQuery18304160648138230669_1592190412830&code=159949&_=1592190413216'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Cookie': 'historystock=002204; spversion=20130314; __utma=156575163.511228193.1589859093.1589859093.1591925746.2;'
                  ' __utmz=156575163.1591925746.2.2.utmcsr=download.10jqka.com.cn|utmccn=(referral)|utmcmd=referral|utmcct=/;'
                  ' user=MDpteF81MjMyMDU3OTg6Ok5vbmU6NTAwOjUzMzIwNTc5ODo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7M'
                  'SwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDoxNjo6OjUyMzIwNTc5ODoxNTkxOTI1O'
                  'DUxOjo6MTU4OTE3MjAwMDo0MDA5NDk6MDoxMjljMmRiMTRlMjMyMWFlMjg2ZTFmMmMxNTEyYWU2MjE6ZGVmYXVsdF80OjE%3D; userid=523205798;'
                  ' u_name=mx_523205798; escapename=mx_523205798; ticket=c70d83f8d9120c5fd3cdd0bc738bdfbc; log=; Hm_lvt_78c58f01938e4d85ea'
                  'f619eae71b4ed1=1589859089,1589939884,1591925740,1592190309; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1592190312;'
                  ' v=Aj-bCTuXXZB_61mMJPH7TciKzhjKJJPPrXiXutEM2-414FHO2fQjFr1IJwzi',
        'Accept': '*/*',
        'Referer': 'http://fund.10jqka.com.cn/zixuan/index.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep - alive'
    }

    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    json_object = ast.literal_eval(res.text[41:len(res.text) - 1])

    pt = PrettyTable()
    pt._set_field_names(" 基金代码 基金名称 最新报价 涨跌幅度 昨收 今开 最高 最低 换手率".split())

    for item in json_object:
        if (item == 'data'):
            for item1 in json_object[item]:
                up_and_down_range = ''
                # 判断涨停情况，进行不同的颜色标记
                if json_object[item][item1]['199112'] > '0':
                    up_and_down_range = '\n'.join([Fore.RED + json_object[item][item1]['199112'] + "%" + Fore.RESET])
                else:
                    up_and_down_range = '\n'.join([Fore.BLUE + json_object[item][item1]['199112'] + "%" + Fore.RESET])
                pt.add_row([
                    # 基金代码
                    item1,
                    # 基金名称
                    json_object['info'][item1]['name'],
                    # 最新报价
                    json_object[item][item1]['10'],
                    # 涨跌幅度
                    up_and_down_range,
                    # 昨收
                    json_object[item][item1]['6'],
                    # 今开
                    json_object[item][item1]['7'],
                    # 最高
                    json_object[item][item1]['8'],
                    # 最低
                    json_object[item][item1]['9'],
                    # 换手率
                    json_object[item][item1]['1968584']
                ])
    print(pt)


scheduler = BlockingScheduler()
# 定时任务，5秒一次
scheduler.add_job(id='shares', func=lottery, trigger='cron', hour='9-15', second='*/5')
time_hour = time.strftime('%H:%M', time.localtime())

if '15:00' <= time_hour:
    scheduler.shutdown()
else:
    scheduler.start()

# if __name__ == "__main__":
#     lottery()
