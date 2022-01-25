# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import splash_request

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['web.archive.org']

    script = '''
    function main(splash, args)
        splash.private_mode_enabled = false
        url = args.url
        assert(splash:go(url))
        assert(splash:wait(0.1))
        rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
        rur_tab[5]:mouse_click()
        assert(splash:wait(0.1))
        splash:set_viewport_full()
        return splash:html()
        end
    '''

    def start_requests(self):
        yield SplashRequest(url='https://web.archive.org/web/20200116052415/https://www.livecoin.net/en/', callback=self.parse, endpoint="execute",
         args={'lua_source': self.script})


    def parse(self, response):
        print(response.body)
