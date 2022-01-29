import scrapy

class nestedSpider(scrapy.Spider):
    name = "nestedSpider"

    def start_requests(self):
        urls = [url_city_1, url_city_2]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
           

    def parse(self, response):
        
        # Gettting the hotels list
        hotel_links = response.css('hotel_selector')

        # Oepening hotels pages
        for hotel in hotel_links:
            yield response.follow(url=hotel, callback=self.parse_hotel)
        
        # Get Next Page information
        next_page = response.css('next_page_selector').extract()
        yield scrapy.Request(url=next_page, callback=self.parse)     


    def parse_hotel(self, response):

        # Get price informations
        info_1 = response.css('info_1_selector')
        info_2 = response.css('info_2_selector')
        # ...
        
        yield {
            "info_1":info_1,
            "info_2":info_2
        }



       