# -*- coding: utf-8 -*-
import scrapy
import json


class HrSpider(scrapy.Spider):
    name = 'hr'

    def start_requests(self):
        urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1577261601515&countryId=1&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']
        headers = {
            'cookie': 'pgv_pvi=6409418752; pgv_pvid=3604204180; _ga=GA1.2.1296393966.1560133345; _gcl_au=1.1.871655896.1576132207',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        meta = {
            'dont_redirect': True,

            'handle_httpstatus_list': [302, 304]
        }

        for url in urls:
            yield scrapy.Request(url=url, headers=headers, meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302]

            }, callback=self.parse, )

    def parse(self, response):
        if response.status == 302:
            return
        text_list = json.loads(response.text)['Data']['Posts']
        for list in text_list:
            item = {}
            item["title"] = list['RecruitPostName']
            item["position"] = list['CategoryName']
            item["publish_date"] = list['LastUpdateTime']
            yield item
