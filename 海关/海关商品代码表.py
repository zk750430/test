import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import urllib3


def lottery():
    # url地址通过抓包工具Charles获取
    print("=================")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    url = 'http://gss.customs.gov.cn/CLSouter2020/KeyGoods/GetQueryKeyGoods'
    # 设置headers，特别是User-Agent和Cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Cookie': '__RequestVerificationToken_L0NMU291dGVyMjAyMA2=h2b_KfoVafsOZiYgDV1OLeHnTH0RGzmZDIdBaVut_Xm_yGcQhxff8p7OZQIFiTUHrgYaL3YPWLQK7F09lzyBAnN9FxrwOx_IZ7iHSuJtXSA1',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://gss.customs.gov.cn/clsouter2020/Home/KeyGoodsSearch',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content_Length': '181',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://gss.customs.gov.cn'
    }
    data = {
        '__RequestVerificationToken': 'SXyTIl5nWi44NoFV7ol1IdbPvJyvUr4nF51BvFb2VFCuRGpOBLyINPKC8YfZAV7TGgAbOma7NFvWux0i3BAI1maWT2ZutkUY_sn17IVuRM01',
        'page': '1', 'pageSize': '5000', 'Code_Ts': '', 'G_Name': '', 'Key_Word': ''}
    res = requests.post(url, data, headers=headers, verify=False)
    res.encoding = res.apparent_encoding


urllib3.disable_warnings()

if __name__ == "__main__":
    lottery()
