# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['onlistings.trreb.ca']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def start_requests(self):
        yield scrapy.Request(url='https://onlistings.trreb.ca/searchlistings#search/32fe9868d978cbbbf4877efd/listing/TREB-E5439036',
                            dont_filter=True, headers={'User-Agent': self.user_agent}, meta = {'dont_redirect': True,'handle_httpstatus_list': [301, 302] })

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='listings']//li"), callback='parse', follow=True, process_request='set_user_agent'),
    )

    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse(self, response):
        print('PARSE')
        yield {
            'Address': response.xpath("//span[@class='listing-details']//span/strong").get()
        }
