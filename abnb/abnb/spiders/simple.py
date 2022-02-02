# -*- coding: utf-8 -*-
from distutils.util import execute
import scrapy
from scrapy_splash import SplashRequest


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['airbnb.ca']

    script = '''function main(splash, args)
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return {
                html = splash:html(),
            }
            end'''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

    def start_requests(self):
        yield SplashRequest(
            url='https://www.airbnb.ca/rooms/48058366/',
            callback=self.parse,
            args={"lua_source": self.script},
            headers = self.headers,
            endpoint='execute'
       )

    def parse(self, response):
        with open('page.html', 'wb') as html_file:
            html_file.write(response.body)
        yield { 
            'title': response.xpath("//h2[@class='_14i3z6h']/text()").get()}