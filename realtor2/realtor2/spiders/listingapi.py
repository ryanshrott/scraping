# -*- coding: utf-8 -*-
import scrapy
import json


class ListingapiSpider(scrapy.Spider):
    name = 'listingapi'
    allowed_domains = ['realtor.ca']
    start_urls = ['https://www.realtor.ca/map#ZoomLevel=13&Center=43.686631%2C-79.339824&LatitudeMax=43.75741&LongitudeMax=-79.25894&LatitudeMin=43.61577&LongitudeMin=-79.42071&view=list&Sort=6-D&PGeoIds=g20_dpz8de7m&GeoName=East%20York%2C%20Toronto%2C%20ON&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD']

    headers = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'origin':'https://www.realtor.ca',
    'referer':'https://www.realtor.ca/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    payload = {
        'ZoomLevel':'13',
        'LatitudeMax':'43.75741',
        'LongitudeMax':'-79.25894',
        'LatitudeMin':'43.61577',
        'LongitudeMin':'-79.42071',
        'Sort':'6-D',
        'PropertyTypeGroupID':'1',
        'PropertySearchTypeId':'1',
        'TransactionTypeId':'2',
        'Currency':'CAD',
        'RecordsPerPage':'100',
        'ApplicationId':'1',
        'CultureId':'1',
        'Version':'7.0',
        'CurrentPage': '1'
        }

    def parse(self, response):
        resp = json.loads(response.body)
        results = resp.get('Results')
        for r in results:
            yield {
                'MlsNumber' : r.get('MlsNumber')
            }
        current_page = int(resp.get('CurrentPage'))
        if current_page < 5:
            next_page = int(current_page) + 1
            self.payload['CurrentPage'] = str(next_page)
            yield scrapy.Request(
                url=f'https://api2.realtor.ca/Listing.svc/PropertySearch_Post',
                body=json.dumps(self.payload), 
                headers=self.headers,
                callback=self.parse
            )
            
