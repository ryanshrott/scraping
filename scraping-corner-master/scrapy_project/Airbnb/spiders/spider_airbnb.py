import scrapy

import logzero
import logging
from logzero import logger as lg
logzero.loglevel(logging.DEBUG) # To display content information


def prepare_request(city, checkin=None, checkout=None, price_min=None, price_max=None, currency='USD'):
    """ Given a city and eventual dates, and eventual prices, returns the airbnb url to scrap
        Both dates must be strings formatted 'YYYY-MM-DD'
    """
    url = f'https://www.airbnb.com/s/{city}/homes/?' 
    if checkin and checkout:
        url += f'&checkin={checkin}&checkout={checkout}'
    if price_min and price_max:
        url+= f'&price_min={price_min}&price_max={price_max}&display_currency={currency}'
    return url

class AirbnbSpider(scrapy.Spider):
    name = "AirbnbSpider"

    def __init__(self, *args, **kwargs):
    
        # Web pages to parse
        self.start_urls = [
            prepare_request('toronto', '2021-03-01', '2021-03-08', price_min=0, price_max=100)
        ]

        # Parse max_page
        self.max_page = 15

        # Scrapping compteur
        self.page = 0
        self.object = 0


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):

        # Number of main page scrapped
        self.page += 1
        lg.warn('Parse page ({})'.format(self.page))

        # Loading all add on the webpage
        annonces = response.css('div._8ssblpx')

        # Iteratint on each of them to yield adds in a JSON file
        for annonce in annonces:

            titre = annonce.css('a ::attr(aria-label)').extract_first()
            lien = annonce.css('::attr(href)').extract_first()
            img_url = annonce.css('img ::attr(src)').extract_first()
            type_of_room = annonce.css('div._b14dlit ::text').extract_first()

            additionnal_info = annonce.css('div._kqh46o ::text').extract()
            additionnal_info = [i for i in additionnal_info if i not in [' · ']]

            rating = annonce.css('span._10fy1f8 ::text').extract_first()
            nb_comment = annonce.css('span._a7a5sx ::text').extract()
            
            night_price = annonce.css('span._1p7iugi ::text').extract()
            full_price = annonce.css('span._7nl8mr ::text').extract()

            superhost = annonce.css('div._ufoy4t::text').extract()
            superhost = 'SUPERHOST' in superhost
            
            lg.debug(titre)
            yield {
                'titre':titre,
                'lien':lien,
                'img_url':img_url,
                'type_of_room':type_of_room,
                'additionnal_info':additionnal_info,
                'rating':rating,
                'nb_comment':nb_comment,
                'night_price':night_price,
                'full_price':full_price,
                'superhost':superhost
                }
     
        next_page = response.css('a._za9j7e ::attr(href)').extract()
        lg.warn(len(next_page))
        
        if next_page is not None:
            if len(next_page)>0:
                next_page = next_page[0]
                url = "https://www.airbnb.com" + next_page + '&display_currency=USD'
                yield scrapy.Request(url=url, callback=self.parse)
        else:
            lg.error('No next page')
        
