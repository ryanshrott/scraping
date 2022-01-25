# -*- coding: utf-8 -*-
import scrapy


class OpenlibraryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login'
    allowed_domains = ['openlibrary.org']
    start_urls = ['http://openlibrary.org/account/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, 
            formid='register',
            formdata ={'username': 'ryans664@gmail.com',
                    'password': 'test123',
                    'redirect' : '/',
                    'debug_token': '',
                    'login': 'Log in'},

            callback=self.after_login
        )

    def after_login(self, response):
        print('logged in')
