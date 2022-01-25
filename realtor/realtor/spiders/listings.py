# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['realtor.ca']
    start_urls = ['http://www.realtor.ca']

    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def start_requests(self):
        yield scrapy.Request(url='https://www.realtor.ca/map#ZoomLevel=13&Center=43.686631%2C-79.339824&LatitudeMax=43.75741&LongitudeMax=-79.25894&LatitudeMin=43.61577&LongitudeMin=-79.42071&view=list&Sort=6-D&PGeoIds=g20_dpz8de7m&GeoName=East%20York%2C%20Toronto%2C%20ON&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD',
                             headers={'User-Agent': self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='cardCon']"), callback='parse', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse(self, response):
        print('PARSE')
        yield {
            'Address': response.xpath("//div[@class='listingCardAddress']/text()").get()
        }
