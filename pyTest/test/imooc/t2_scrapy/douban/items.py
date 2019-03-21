# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#  这里定义数据结构
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 这里定义每一个item的定义.
    movieId=scrapy.Field()
    movieName=scrapy.Field()
    movieLink=scrapy.Field()
    pass
