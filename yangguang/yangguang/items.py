# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    publish_date = scrapy.Field()
    content = scrapy.Field()
    content_img = scrapy.Field()
