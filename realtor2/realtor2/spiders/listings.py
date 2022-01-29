# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest

class ListingsSpider(CrawlSpider):
    name = 'listings'
    allowed_domains = ['realtor.ca']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
	    url = args.url
        assert(splash:go(url))
        assert(splash:wait(3))
        return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url='https://www.realtor.ca',
                             headers={'User-Agent': self.user_agent}, callback=self.parse_item, endpoint="execute", args={'lua_source': self.script})

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='listingCard card']//a[@class='blockLink listingDetailsLink']"), callback='parse_item', follow=True, process_request='set_user_agent'),
    )
    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield {
            'Address': response.xpath("//div[@id='listingPrice']/text()").get()
        }
