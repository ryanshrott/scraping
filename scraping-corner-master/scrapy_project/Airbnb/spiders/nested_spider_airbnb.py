import scrapy
import get_info
from logzero import logger as lg
class AirbnbSpider(scrapy.Spider):
    name = "AirbnbSpider"

    def start_requests(self):
        cities = ['toronto']
        urls = [f'https://www.airbnb.com/s/{city}/homes/' for city in cities]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
           

    def parse(self, response):
        lg.info(response.url)

        # Getting hotels list
        hotel_links = response.css('div._8ssblpx ::attr(href)')

        # Oepening hotels pages
        for link in hotel_links:
            yield response.follow(url=link, callback=self.parse_hotel)
        
        # Get Next Page information
        next_page = response.css('a._za9j7e ::attr(href)').extract()
        if next_page is not None:
            if len(next_page)>0:
                next_page = next_page[0]
                url = "https://www.airbnb.com" + next_page + '&display_currency=USD'
                lg.info(url)
                yield scrapy.Request(url=url, callback=self.parse)     

    def parse_hotel(self, response):

        # Get price informations
        prices = get_info.get_prices(response)
        price_1, price_2, price_3, price_4, price_5 = prices
        lg.debug(prices)

        # Get title information
        title = get_info.get_title(response)
        lg.debug(title)

        # Get description information
        description = get_info.get_description(response)

        yield {
            "title":title,
            "description":description,
            "url": response.url
        }



    