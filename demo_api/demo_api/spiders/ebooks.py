# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
import json


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12&offset=12/']
    offset = 12
    def parse(self, response):
        resp = json.loads(response.body)
        ebooks = resp.get('works')
        if(len(ebooks) == 0) or response.status == 500:
            raise CloseSpider('Reached last page...')
        for ebook in ebooks:
            yield{
                'title' : ebook.get('title'), 
                'subject' : ebook.get('subject'), 
            }
        self.offset = self.offset * 2
        try:
            yield scrapy.Request(
                url=f'https://openlibrary.org/subjects/picture_books.json?limit=12&offset={self.offset}/',
                callback=self.parse
            )
        except Exception as e:
            print('End')
            
