import requests
import re
from bs4 import BeautifulSoup
import json


def getHTMLText(url):
    params = {
        'timestamp': '1577261601515',
        'countryId': '1',
        'cityId': '',
        'bgIds': '',
        'productId': '',
        'categoryId': '',
        'parentCategoryId': '',
        'attrId': '',
        'keyword': '',
        'pageIndex': '1',
        'pageSize': '10',
        'language': 'zh - cn',
        'area': 'cn'
    }
    headers = {
        'Cookie': 'JSESSIONID=23E7E77D43D69D640A9594ED1BABF1F6; RAIL_EXPIRATION=1577380063481; RAIL_DEVICEID=jI-9_AxET9wIMmgInOuQxvuqUvVkpVdoiMS3y0CIfjmOy4x8aqYgeg5fjcukxLZsUa1XG3TcokPAKOzszM0uJVze_ajE1a3ZUH079_ggeXdfyejfZKNFIaXzkskTAXZeMAUAGOKh098AVThguiMJ7KJPQy28Mqg-; BIGipServerotn=955253258.50210.0000; BIGipServerpool_passport=216859146.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toStation=%u868C%u57E0%2CBBH; _jc_save_fromDate=2019-12-25; _jc_save_toDate=2019-12-25; _jc_save_wfdc_flag=dc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        print("111111")
        res = requests.get(url, headers=headers, verify=False)

        return res.text
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1577261601515&countryId=1&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
    text = json.loads(getHTMLText(url))['Data']['Posts']

    print(text)
