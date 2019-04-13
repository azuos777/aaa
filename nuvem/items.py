# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProdutoItem(scrapy.Item):
    # define the fields for your item here like:
    linkprod = scrapy.Field()
    valorame = scrapy.Field()
    pass