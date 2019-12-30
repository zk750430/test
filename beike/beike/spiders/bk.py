# -*- coding: utf-8 -*-
import scrapy
from ..items import BeikeItem


class BkSpider(scrapy.Spider):
    name = 'bk'

    # allowed_domains = ['nj.zu.ke.com']
    def start_requests(self):
        start_urls = ['https://nj.zu.ke.com/ditiezufang/li110460690s100021183/rt200600000002/']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
            'Content-Type': 'text/html; charset=UTF-8',
            'Cookie': 'lianjia_uuid=2c065f4e-386d-44f6-ada5-cdc6a8232837; sajssdk_2015_cross_new_user=1; select_city=320100; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216f55c138f7515-0f1ec966ed3b9d-36624209-3686400-16f55c138f8939%22%2C%22%24device_id%22%3A%2216f55c138f7515-0f1ec966ed3b9d-36624209-3686400-16f55c138f8939%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDxD930EMKh0nsg607aJ6-X00000rPpy-C00000FKUhv0.THvkVQOZ0A3qmh7GuZNCUvd-gLKM0ZnquH7-myfsPWnsnj0snjRvP6Kd5RRdPHRdnH6YPWb3rjN7wWfYP1b4nWmdP10%22%2C%22%24latest_referrer_host%22%3A%22sp0.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22wyhangzhou%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; Qs_lvt_200116=1577691736; Qs_pv_200116=3234650526796246000; digv_extends=%7B%22utmTrackId%22%3A%2280420087%22%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiN2U1M2FlMmU2MGU4OWUwMDA5MTEzODNiZmUyYTNlYTA0Y2M1NWZlMmJlMDFmOThkMDkxMTI2MTdkZDkwY2FlZmRiM2M5OGJhMDE2ZTFiOGE5NGQ1MzlhYjBiYTFjNDg0M2JkMjM1NjI3ODMxMTMyZjg2MDIzZWIwMmE3ZmMwNDNiYmZmNDc3MmJmYjUxN2IwZjg3ZTliMTljNDkzOWQ0NzQ4MmJhYWE5MDQ1YjcyNmZjZWFkYjkyYmE0NzQwNThiNTRmZDY0MTViZDlmNGNjY2U1YjdhMWI0YjQ1OGYyOWUxYWVlODNjZTQ3NjAxN2RlYTY3N2M2NjRjMmU5YjAzZTJmZDNkMmE1MDUyYjE2NTJmOGVkN2YzYTM1YzcwZTg4YWUyOTEwNjUxZTY2ZTcxNTkzZjRhZTFkZTYyMjM3ZDgwNjFkNGU1MjJiZDcwN2Y0ZmM4N2M0NDJiNjE3YmFiOVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJjNGU1NGQyZVwifSIsInIiOiJodHRwczovL25qLnp1LmtlLmNvbS9kaXRpZXp1ZmFuZy9saTExMDQ2MDY5MHMxMDAwMjExODMvcnQyMDA2MDAwMDAwMDIvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; Hm_lvt_4e5bdf78b2b9fcb88736fc67709f2806=1577691740; Hm_lpvt_4e5bdf78b2b9fcb88736fc67709f2806=1577691767; lianjia_ssid=55ab3fae-78e7-417b-a63b-0c09494ea504',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
        for url in start_urls:
            yield scrapy.Request(url=url, headers=headers, meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302]
            }, callback=self.parse, )

    def parse(self, response):
        res_list = response.xpath("//div[@class='content__list--item--main']")
        # print(res_list)
        for res in res_list:
            item = BeikeItem()
            href = res.xpath("./p[@class='content__list--item--title twoline']/a/@href").extract_first()
            price = res.xpath("./span[@class='content__list--item-price']/em/text()").extract_first()
            if int(price) <= 1100:
                url_path = 'https://nj.zu.ke.com/zufang'
                item['href'] = url_path + href
                item['price'] = price
                print(item)
            else:
                continue
        pass
