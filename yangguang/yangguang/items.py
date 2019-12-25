# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    title = scrapy.Field()
    publish_data = scrapy.Field()
    publish_name = scrapy.Field()
    publish_state = scrapy.Field()
