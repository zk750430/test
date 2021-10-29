import requests
import ast
from prettytable import PrettyTable
from colorama import Fore
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def lottery():
    # url地址通过抓包工具Charles获取
    url = 'http://d.10jqka.com.cn/multimarketreal/17,33/600196_600418_600030_600036_600598_601990,002600_000063_000725_002142_000100_300603/' \
          '1968584_13_19_3541450_526792_6_7_8_9_10_2034120_199112_264648?callback=multimarketreal&_=1607665572270'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Cookie': 'historystock=300033; spversion=20130314; user=MDpteF81MjMyMDU3OTg6Ok5vbmU6NTAwOjUzMzIwNTc5ODo3LDExMTExMTExMTExLDQwOzQ'
                  '0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0M'
                  'DoxNjo6OjUyMzIwNTc5ODoxNjA3NjU1ODMxOjo6MTU4OTE3MjAwMDo0MDI5Njk6MDoxYjZlMTU0MjNlY2ViNTE5ODNmMTk3ZTc5MGUwZmQ0MTk6ZGVmYXV'
                  'sdF80OjE%3D; userid=523205798; u_name=mx_523205798; escapename=mx_523205798; ticket=d13375290cc17754a181f3e0ec6cbfc9; '
                  'user_status=0; log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1607655799,1607656459; Hm_lpvt_78c58f01938'
                  'e4d85eaf619eae71b4ed1=1607656459; v=AsWSdIa0NpbvgxJK0dAwMZcE1Ar8gnn3wzRdaMcqgfwLXut8j9KJ5FOGbQZU',
        'Accept': '*/*',
        'Host': 'd.10jqka.com.cn',
        'Referer': 'http://t.10jqka.com.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep - alive'
    }

    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    json_object = ast.literal_eval(res.text[16:len(res.text) - 1])

    pt = PrettyTable(" 股票名　当前价格　涨跌幅度　振幅　换手率　成交额 昨收　今开".split())
    # pt.field_names()

    for item in json_object:
        for item1 in json_object[item]:
            price = ''
            up_and_down_range = ''
            # 判断涨停情况，进行不同的颜色标记
            if json_object[item][item1]['264648'] > '0':
                price = '\n'.join([Fore.RED + json_object[item][item1]['10'] + Fore.RESET])
                up_and_down_range = '\n'.join(
                    [Fore.RED + json_object[item][item1]['199112'] + "%(" + json_object[item][item1][
                        '264648'] + ")" + Fore.RESET])
            else:
                price = '\n'.join([Fore.BLUE + json_object[item][item1]['10'] + Fore.RESET])
                up_and_down_range = '\n'.join([Fore.BLUE + json_object[item][item1]['199112'] + "%(" +
                                               json_object[item][item1]['264648'] + ")" + Fore.RESET])
            pt.add_row([
                # 股票名
                json_object[item][item1]['name'] + "(" + item1 + ")",
                # 当前价格
                price,
                # 涨跌幅度
                up_and_down_range,
                # 振幅
                json_object[item][item1]['526792'],
                # 换手率
                json_object[item][item1]['1968584'],
                # 成交额
                json_object[item][item1]['19'],
                # 昨开
                json_object[item][item1]['6'],
                # 今开
                json_object[item][item1]['7'],
            ])
            pt.sortby = "涨跌幅度"
            pt.reversesort = True
    print(pt)


scheduler = BlockingScheduler()
# 定时任务，5秒一次
scheduler.add_job(id='shares', func=lottery, trigger='cron', hour='9-11,13-15', second='*/3')
time_hour = time.strftime('%H:%M', time.localtime())

if '15:00' <= time_hour:
    scheduler.shutdown()
else:
    scheduler.start()
