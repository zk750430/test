# -*- coding: utf-8 -*-
import scrapy
from ..items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=']

    def start_requests(self):
        urls = [
            'http://wz.sun0769.com/index.php/question/report?page='
        ]

        headers = {
            # 'cookie': 'pgv_pvi=6409418752; pgv_pvid=3604204180; _ga=GA1.2.1296393966.1560133345; _gcl_au=1.1.871655896.1576132207',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            # 'Host': 'wz.sun0769.com',
            # 'Referer': 'http://wz.sun0769.com/index.php/question/report?page=30',
            'Upgrade-Insecure-Requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        # cookies ='pgv_pvi=6409418752; pgv_pvid=3604204180; _ga=GA1.2.1296393966.1560133345; _gcl_au=1.1.871655896.1576132207',
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse, )

    def parse(self, response):
        # 分组

        tr_list = response.xpath("//table[@class='newsHead clearfix']/table[2]/tr")
        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath("./td[3]a[1]/@title").extract_first()
            item["publish_data"] = tr.xpath("./td[6]/text()").extract_first()
            item["publish_name"] = tr.xpath("./td[5]/text()").extract_first()
            item["publish_state"] = tr.xpath("./td[4]/span[@class='qgrn']/text()").extract_first()
            yield item
