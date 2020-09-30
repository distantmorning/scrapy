# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Test1Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    reply = scrapy.Field()
    link = scrapy.Field()
    pass

class chItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()