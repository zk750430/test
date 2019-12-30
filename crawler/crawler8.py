import requests
from bs4 import BeautifulSoup
import json
import redis

#
# url = 'https://hz-bj-rubbish.neocross.cn/rubbish/V1/app/transform/findByType'
# url1 = 'http://extshort.weixin.qq.com/mmtls/12667279'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.8(0x17000820) NetType/WIFI Language/zh_CN',
#     # 'Content-Type': 'application/json',
#     'User-Agent':'MicroMessenger Client',
#     'Content-Type': 'application/octet-stream',
#     'Accept': '*/*'
# }
# params = {
#     # "pageNum": 1,
#     # "pageSize": 100,
#     # "type": "4",
#     # "status": 1
# }
# res = requests.post(url, headers=headers, json=params, verify=False)
# res.encoding = res.apparent_encoding
# text_list = json.loads(res.text)['data']['records']
# text1 = {}
# for text in text_list:
#     text1['name'] = text['name']
#     print(text1)

url = 'https://xcx.www.gov.cn/ebus/gwymp/api/r/xcxrubbishsearch/getbytypeId?'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.8(0x17000820) NetType/WIFI Language/zh_CN',
    'Content-Type': 'application/json',
    'x-tif-did': '62KF5t6CC6',
    'x-yss-page': 'publicService/pages/refuseClassification/refuse_list/index',
    'x-tif-openid': 'ojyj-42UDoEmbUKUZzqPM9wXeXfM',
    'x-yss-city-code': '4400',
    'x-tif-sid': '2a432d58cfc7f5c989f2747ec9bce6cf80',
    'dgd-pre-release': '0'
}
# 可回收物
json1 = {
    "page": 1,
    "page_size": 1000,
    "type_id": "30"
}

# 有害垃圾
json2 = {
    "page": 1,
    "page_size": 1000,
    "type_id": "31"
}
# 厨余垃圾
json3 = {
    "page": 1,
    "page_size": 1000,
    "type_id": "32"
}
# 其他垃圾
json4 = {
    "page": 1,
    "page_size": 1000,
    "type_id": "33"
}

res = requests.post(url, headers=headers, json=json1, verify=False)
res.encoding = res.apparent_encoding
text_list = json.loads(res.text)['data']['list']
list = []
for text in text_list:
    name = text['example']
    list.append(name)
print(list)
r = redis.Redis(host='localhost', port=6379, password='123456',
                decode_responses=True)  # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.rpush("可回收物", ','.join(list))
