# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SqtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    MovieName = scrapy.Field()
    Zip320 = scrapy.Field()
    Zip128 = scrapy.Field()
    TimeStamp = scrapy.Field()
    pass
