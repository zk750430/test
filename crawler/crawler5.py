import time

import requests
import json
from prettytable import PrettyTable
from colorama import Fore
import re


class global_value():
    stations = []


# 传入的参数
param = {
    'leftTicketDTO.train_date': '2019-12-25',
    'leftTicketDTO.from_station': 'HZH',
    'leftTicketDTO.to_station': 'BBH',
    'purpose_codes': 'ADULT'
}

# 去掉可能会存在的一些不必要的验证
headers = {
    'Cookie': 'JSESSIONID=23E7E77D43D69D640A9594ED1BABF1F6; RAIL_EXPIRATION=1577380063481; RAIL_DEVICEID=jI-9_AxET9wIMmgInOuQxvuqUvVkpVdoiMS3y0CIfjmOy4x8aqYgeg5fjcukxLZsUa1XG3TcokPAKOzszM0uJVze_ajE1a3ZUH079_ggeXdfyejfZKNFIaXzkskTAXZeMAUAGOKh098AVThguiMJ7KJPQy28Mqg-; BIGipServerotn=955253258.50210.0000; BIGipServerpool_passport=216859146.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u868C%u57E0%2CBBH; _jc_save_fromDate=2019-12-25; _jc_save_toDate=2019-12-25; _jc_save_wfdc_flag=dc',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

}


def getHTMLText(url):
    try:
        res = requests.get(url, param, headers=headers, timeout=30)
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""


def getStatiosn():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9134'
    # 发送get请求，不判断证书
    response = requests.get(url, verify=False)
    # 　使用正则表达式提取所有的站点：汉字和大写代号
    stations = dict(re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text))
    # 转换成字典就是为了将汉字站点和字母代号分开且有一一对应关系：键－－>值
    global_value.stations = stations


# 根据站点的编码获取站点名
def get_name(telecode):
    stations = global_value.stations
    for station in stations:
        if (stations.get(station) == telecode):
            return station
        else:
            continue


if __name__ == "__main__":
    getStatiosn()
    time.sleep(3)

    # 爬取查询结果
    url1 = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
    text = getHTMLText(url1)
    # stations = dict(re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text))
    raw_trains = json.loads(text)['data']['result']
    pt = PrettyTable()
    pt._set_field_names("车次　车站　时间　经历时　一等座　二等座　软卧　硬卧 硬座　无座".split())
    for raw_train in raw_trains:
        # split切割之后得到的是一个列表
        data_list = raw_train.split("|")
        train_no = data_list[3]
        initial = train_no[0].lower()
        # print(train_no[0])
        # 判断是否是查询特定车次的信息
        from_station_code = data_list[6]
        to_station_code = data_list[7]
        from_station_name = ''
        to_station_name = ''
        start_time = data_list[8]
        arrive_time = data_list[9]
        time_duration = data_list[10]
        first_class_seat = data_list[31] or "--"
        second_class_seat = data_list[30] or "--"
        soft_sleep = data_list[23] or "--"
        hard_sleep = data_list[28] or "--"
        hard_seat = data_list[29] or "--"
        no_seat = data_list[33] or "--"
        pt.add_row([
            # 对特定文字添加颜色
            train_no,
            '\n'.join([Fore.GREEN + get_name(from_station_code) + Fore.RESET,
                       Fore.RED + get_name(to_station_code) + Fore.RESET]),
            '\n'.join([Fore.GREEN + start_time + Fore.RESET, Fore.RED + arrive_time + Fore.RESET]),
            time_duration,
            first_class_seat,
            second_class_seat,
            soft_sleep,
            hard_sleep,
            hard_seat,
            no_seat
        ])

    print(pt)
