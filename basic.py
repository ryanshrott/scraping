# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['basic.com']
    start_urls = ['http://basic.com/']

    def parse(self, response):
        pass
