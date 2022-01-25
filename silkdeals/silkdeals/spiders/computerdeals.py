# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ComputerdealsSpider(scrapy.Spider):
    name = 'computerdeals'

    def remove_characters(self, value):
        try:
            return value.strip('\\xao')
        except Exception as e:
            return ''

    def start_requests(self):
        yield SeleniumRequest(
            url='https://slickdeals.net/computer-deals',
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        products = response.xpath("//ul[@class='dealTiles categoryGridDeals blueprint']/li")

        for product in products:
            yield {
                'name' : product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/text()").get(),
                'link' : product.xpath(".//a[@class='itemTitle bp-p-dealLink bp-c-link']/@href").get(),
                'price' : product.xpath("normalize-space((.//button[contains(@class, 'itemStore')] | //a[contains(@class, 'itemStore')])/text())").get(),
                'store_name' : self.remove_characters(product.xpath("normalize-space(.//button[contains(@class,'itemStore')]/text())").get()),
            }

        next_page = response.xpath("//a[@data-role='next-page']/@href").get()
        if next_page:
            print(next_page)
            absolute_url = f"https://slickdeals.net{next_page}"
            print(absolute_url)
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )

