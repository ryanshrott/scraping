# -*- coding: utf-8 -*-
import scrapy


class BestSellersSpider(scrapy.Spider):
    name = 'best_sellers'
    allowed_domains = ['glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']


    def parse(self, response):
        glasses = response.xpath("//div[@id='product-lists']/div")
        for glass in glasses:
            yield {
                'name': glass.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'url': glass.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': glass.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                'price': glass.xpath(".//div[@class='p-price']//span/text()").get()
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        print('pagination')
        print(next_page)
        if next_page:
            print('going to next page!')
            yield scrapy.Request(url=next_page, callback=self.parse)
