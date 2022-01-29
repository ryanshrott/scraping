# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.exceptions import CloseSpider
import time
class AirbnbSpider(scrapy.Spider):
    name = 'airbnb'
    allowed_domains = ['www.airbnb.ca']

    timestamp = int(time.time())
    cookies = {}
    def start_requests(self):
        print(self.city)
        yield scrapy.Request(url="https://www.airbnb.com/api/v2/place_activities/4430?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en&_format=for_spa_activity_pdp_web",
                    callback=self.parse_id)

    def parse_id(self, response):
        data = json.loads(response.body)
       # with open('sample.json', 'w') as file:
       #     file.write(json.dumps(data))

        rests = data.get('explore_tabs')[0].get('sections')[0].get('recommendation_items')
        if rests is None:
            raise CloseSpider('No rests avaialble in this city ')
        for r in rests:
            yield scrapy.Request(url=f"https://www.airbnb.com/api/v2/place_activities/{r.get('id')}?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en&_format=for_spa_activity_pdp_web",
                                 callback=self.parse)
        
        pagination_metadata = data.get('explore_tabs')[0].get('pagination_metadata')

        if pagination_metadata.get('has_next_page'):
            items_offset = pagination_metadata.get('items_offset')
            section_offset = pagination_metadata.get('section_offset')
            yield scrapy.Request(url=f"https://www.airbnb.com/api/v2/place_activities/4430?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en&_format=for_spa_activity_pdp_web&items_offset={items_offset}&section_offset{section_offset}",
                    callback=self.parse_id)

    def parse(self, response):
        restaurant = json.loads(response.body).get('place_activity')

        yield {
            'id' : restaurant.get('id'),
            'title' : restaurant.get('title'),
            'type' : restaurant.get('action_kicker'),
            'description' : restaurant.get('decription'),
            'place' : {
                'address' : restaurant.get('place').get('address'),
                'city' : restaurant.get('place').get('city'),
                'country' : restaurant.get('place').get('country'),
                'latitude' : restaurant.get('place').get('lat'),
                'longitude' : restaurant.get('place').get('lng'),
            },
            'phone_number': restaurant.get('place').get('phone'),
            'website': restaurant.get('place').get('website')}
