# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GreenlibrosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #info de producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    precio = scrapy.Field()
    
    #Variables fijas
    categoria = 'filosofia'
    comercio = 'Green Libros'