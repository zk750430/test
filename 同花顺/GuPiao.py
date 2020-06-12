import requests
import ast
from prettytable import PrettyTable
from colorama import Fore
from apscheduler.schedulers.blocking import BlockingScheduler




def lottery():
    # url地址通过抓包工具Charles获取
    url = 'http://d.10jqka.com.cn/multimarketreal/17,33/601360_600418_600598_600036_600030_600029_600814,000800_002142_002594_000425_000100_' \
          '000725_000063/1968584_13_19_3541450_526792_6_7_8_9_10_2034120_199112_264648?callback=multimarketreal&_=1591925863750'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'Cookie': 'historystock=002204; spversion=20130314; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1589859089,1589939884,1591925740; __'
                  'utma=156575163.511228193.1589859093.1589859093.1591925746.2; __utmc=156575163; __utmz=156575163.1591925746.2.2.utmcsr=download.10jqka.com.cn'
                  '|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=156575163.1.10.1591925746; log=; user=MDpteF81MjMyMDU3OTg6Ok5vbmU6NTAwOjUzMzIwNTc5ODo3LD'
                  'ExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDoxNjo6OjUyMz'
                  'IwNTc5ODoxNTkxOTI1ODUxOjo6MTU4OTE3MjAwMDo0MDA5NDk6MDoxMjljMmRiMTRlMjMyMWFlMjg2ZTFmMmMxNTEyYWU2MjE6ZGVmYXVsdF80OjE%3D; userid=523205798; u_name='
                  'mx_523205798; escapename=mx_523205798; ticket=c70d83f8d9120c5fd3cdd0bc738bdfbc; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1591925864; v=AjCUpLCqGt'
                  'ExW8bVOjecqONPAfWBeREVNndo2iqB_IBfJ94j0onkU4ZtOJF5',
        'Accept': '*/*',
        'Referer': 'http://t.10jqka.com.cn/newcircle/user/userPersonal/?from=finance&tab=zx',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'historystock=002204; spvers',
        'Connection': 'keep - alive'
    }

    res = requests.get(url, headers=headers, verify=False)
    res.encoding = res.apparent_encoding
    json_object = ast.literal_eval(res.text[16:len(res.text) - 1])

    pt = PrettyTable()
    pt._set_field_names(" 股票名　当前价格　涨跌幅度　振幅　换手率　成交额 昨收　今开".split())

    for item in json_object:
        for item1 in json_object[item]:
            price = ''
            up_and_down_range = ''
            # 判断涨停情况，进行不同的颜色标记
            if json_object[item][item1]['264648'] > '0':
                price = '\n'.join([Fore.RED + json_object[item][item1]['10'] + Fore.RESET])
                up_and_down_range = '\n'.join(
                    [Fore.RED + json_object[item][item1]['264648'] + "(" + json_object[item][item1][
                        '199112'] + "%)" + Fore.RESET])
            else:
                price = '\n'.join([Fore.BLUE + json_object[item][item1]['10'] + Fore.RESET])
                up_and_down_range = '\n'.join([Fore.BLUE + json_object[item][item1]['264648'] + "(" +
                                            json_object[item][item1]['199112'] + "%)" + Fore.RESET])
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
    print(pt)


# scheduler = BlockingScheduler()
# 定时任务，5秒一次
# scheduler.add_job(func=lottery, trigger='cron', second='*/5')
# scheduler.start()
if __name__ == "__main__":
    lottery()



