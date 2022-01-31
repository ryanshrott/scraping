import scrapy


class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    allowed_domains = ['api2.realtor.ca']

    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
    }
    api = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

    payload = "ZoomLevel=11&LatitudeMax=43.98268&LongitudeMax=-78.96028&LatitudeMin=43.43223&LongitudeMin=-79.79249&Sort=6-D&PropertySearchTypeId=1&TransactionTypeId=2&PropertyTypeGroupID=1&Currency=CAD&CurrentPage=1&ApplicationId=1&CultureId=1&Version=7.0&RecordsPerPage=200"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "DNT": "1",
        "Host": "api2.realtor.ca",
        "Origin": "https://www.realtor.ca",
        "Pragma": "no-cache",
        "Referer": "https://www.realtor.ca/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "TE": "trailers",
        'User-Agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Mobile Safari/537.36",
    }
    
    def start_requests(self):
        yield scrapy.Request(url=self.api,
                             callback=self.parse,
                             method='POST',
                             headers=self.headers,
                             body=self.payload)

    def parse(self, response):
        print('PARSE')
        results = response.json().get('Results')
        print('results')
        for r in results:
            yield {
                'Id': r.get('Id'),
                'Price': r.get('Property').get('Price')
            }