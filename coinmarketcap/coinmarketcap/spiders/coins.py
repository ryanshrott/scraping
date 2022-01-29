# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CoinsSpider(CrawlSpider):
    name = 'coins'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20190101085451/https://coinmarketcap.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='currency-name-container link-secondary']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'name' : response.xpath("normalize-space((//h1[@class='details-panel-item--name']/text())[2])").get(),
            'rank': response.xpath("//span[@class='label label-success']/text()").get(),
            'price(usd)': response.xpath("//span[@class='h2 text-semi-bold details-panel-item--price__value']/text()").get(),

        }
