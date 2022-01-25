# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        resp = json.loads(response.body)
        quotes = resp.get('Results')
        for quote in quotes:
            yield {
                'author' : quote.get('Id'),
            }
        current_page = resp.get('CurrentPage')
        if current_page < 5:
            next_page = int(resp.get('page')) + 1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={next_page}',
                callback=self.parse
            )
            
