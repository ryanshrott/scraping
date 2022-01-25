# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest


class ListingsSpider(scrapy.Spider):
    name = 'listings'

    url = 'https://www.airbnb.ca/s/Toronto--ON/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto%2C%20ON&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&checkin=2022-02-01&checkout=2022-02-04&adults=2&source=structured_search_input_header&search_type=user_map_move&ne_lat=43.68366776846674&ne_lng=-79.37296721824504&sw_lat=43.65022358872021&sw_lng=-79.39357060679293&zoom=15&search_by_map=true'
    
    def start_requests(self):
        yield SeleniumRequest(
            url= self.url,
            wait_time=3,
            callback=self.parse
        )

    def parse(self, response):
        print('PARSING')
        listings = response.xpath("//div[@class='_gig1e7']")

        for listing in listings:
            yield {
                'name' : listing.xpath(".//meta[@itemprop='name']/@content").get(),
            }

        next_page = response.xpath("//a[@aria-label='Next']/@href").get()
        if next_page:
            print(next_page)
            absolute_url = f"{self.url}/{next_page}"
            print(absolute_url)
            yield SeleniumRequest(
                url=absolute_url,
                wait_time=3,
                callback=self.parse
            )
