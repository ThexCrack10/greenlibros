# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from greenlibros.items import GreenlibrosItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 

class FilosofiaSpider(CrawlSpider):
	name = 'filosofia'
	allowed_domains = ['www.greenlibros.com']
	start_urls = ['http://www.greenlibros.com/categorias/filosofia',]
	rules = (
		# Para cada item
		Rule(SgmLinkExtractor(allow = (), restrict_xpaths = ('//*[@id="amshopby-page-container"]/div[3]/div[1]/div[2]/div/ol/li[6]/a'))),
		Rule(SgmLinkExtractor(allow =(), restrict_xpaths = ('//*[@id="amshopby-page-container"]/div[3]/div[1]/div[2]/div/ol/li[6]/a')),
							callback = 'parse_item', follow = False)
	)

	def parse_item(self, response):
		ml_item = GreenlibrosItem()
		#info de productos
		ml_item['titulo'] = response.xpath('//*[@id="product_addtocart_form"]/div[3]/div[1]/h1').extract()
		ml_item['modelo'] = response.xpath('//*[@id="product_addtocart_form"]/div[3]/div[1]/h5[2]/b').extract()
		ml_item['marca'] = response.xpath('//*[@id="product-attribute-specs-table"]/tbody/tr[3]/td').extract()
		ml_item['precio'] = response.xpath('//*[@id="product-price-237415"]/span').extract()
		ml_item['categoria'] = 'filosofia'
		ml_item['comercio'] = 'Green Libros'
		yield ml_item
		 

