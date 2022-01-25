# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.shell import inspect_response
from scrapy.utils.response import open_in_browser
import logging

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # countries = response.xpath('//td/a') # a list of selector objects
        # for country in countries:
        #     name = country.xpath('.//text()').get() # must start by .// when executing an xpath against a selector object
        #     link = country.xpath('.//@href').get() # must start by .// when executing an xpath against a selector object
        #     # send a request to each country link

        #     # absolute_url = f"https://www.worldometers.info{link}"
        #     # absolute_url = response.urljoin(link)
        yield response.follow(url="https://www.worldometers.info/world-population/china-population", callback=self.parse_country, meta={'country_name': 'China'})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }
