# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']

    script = """
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(1))
        splash:set_viewport_full()
        return splash:html()
    end
    """

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js/', callback=self.parse, endpoint="execute",
                            args={'lua_source': self.script})

    def parse(self, response):
        currencies = response.xpath("//div[@class='quote']")
        for currency in currencies:
            yield {
                'quote': currency.xpath(".//span[1]/text()").get(),
                'author': currency.xpath(".//span[2]/small/text()").get(),
                'tags': currency.xpath(".//div[@class='tags']/a[@class='tag']//text()").getall()
            }
        next_page = response.xpath("//li[@class='next']/a/@href").get()

        if next_page:
            print('going to next page!')
            next_page_link = response.urljoin(next_page)
            print(next_page_link)
            yield SplashRequest(url=next_page_link, callback=self.parse, endpoint="execute",
                            args={'lua_source': self.script})
