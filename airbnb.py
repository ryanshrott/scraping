# -*- coding: utf-8 -*-
import scrapy


class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.ca']
    start_urls = ['http://www.airbnb.ca/']

    def parse(self, response):
        pass
