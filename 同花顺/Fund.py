import requests
import ast
from prettytable import PrettyTable
from colorama import Fore
from apscheduler.schedulers.blocking import BlockingScheduler
import time


def lottery():
    # url地址通过抓包工具Charles获取
    url = 'http://qd.10jqka.com.cn/quote.php?cate=real&type=fund&return=json&callback=jQuery18306106009431502835_1609997351119&code=159949&_=1609997352038'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Cookie': 'spversion=20130314; historystock=HK9633%7C*%7C300033; log=; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1607655799,16076564'
                  '59,1609382869,1609997278; user=MDpteF81MjMyMDU3OTg6Ok5vbmU6NTAwOjUzMzIwNTc5ODo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0'
                  'MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoxNjo6OjUyMzIwNTc'
                  '5ODoxNjA5OTk3MzI5Ojo6MTU4OTE3MjAwMDo0MDE0NzE6MDoxYzFiNmYwMTA5NjljMjg3OTY2NDlmMzdmNmRlMDRkMGU6ZGVmYXVsdF80OjE%3D; userid='
                  '523205798; u_name=mx_523205798; escapename=mx_523205798; ticket=60269a56de08d9ab11794e6c7322ee1a; user_status=0; Hm_lpvt_'
                  '78c58f01938e4d85eaf619eae71b4ed1=1609997335; v=A9TDxFWtd3FylOM9go3RUn5DpRlFLfgAOlGMW261YN_iWXoPlj3Ip4phXO29',
        'Accept': '*/*',
        'Referer': 'http://fund.10jqka.com.cn/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep - alive'
    }

    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    json_object = ast.literal_eval(res.text[41:len(res.text) - 1])

    pt = PrettyTable(" 基金代码 基金名称 最新报价 涨跌幅度 昨收 今开 最高 最低 换手率".split())
    pt.title="自选基金"
    pt.align["基金代码"]='c'
    pt.align["基金名称"] = 'c'
    # pt._set_field_names(" 基金代码 基金名称 最新报价 涨跌幅度 昨收 今开 最高 最低 换手率".split())

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
                pt.sortby = "涨跌幅度"
                # pt.reversesort = True
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
