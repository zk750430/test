import requests
import re
from bs4 import BeautifulSoup
import json


def getHTMLText(url):
    headers = {
        'cookie': 'PHPSESSID=ifun99h16ulcal88mtqld8r233; NSC_wt_xa.tvo0769.dpn=ffffffffc3a0145d45525d5f4f58455e445a4a423660',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    try:
        print("111111")
        res = requests.get(url, headers=headers, verify=False)
        res.encoding = res.apparent_encoding
        res.raise_for_status()

        return res.text
    except Exception as e:
        print(e)
        return ""


if __name__ == "__main__":
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=0'
    text = getHTMLText(url)

    print(text)
