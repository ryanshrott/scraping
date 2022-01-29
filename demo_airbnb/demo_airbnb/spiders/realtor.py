# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.exceptions import CloseSpider


class RealtorSpider(scrapy.Spider):
    
    name = 'realtor'
    allowed_domains = ['api2.realtor.ca']

    api = "https://api2.realtor.ca/Listing.svc/PropertySearch_Post"

    payload = "ZoomLevel=11&LatitudeMax=43.99454&LongitudeMax=-79.05332&LatitudeMin=43.42026&LongitudeMin=-79.69945&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD&CurrentPage=1&ApplicationId=1&CultureId=1&Version=7.0&RecordsPerPage=100"

    headers = {
    'cookie': "gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=JLYUNoQeQ8aK7XCukUKVyLTR4GEAAAAAQUIPAAAAAAD5E9h/kC3MKXYFk8j751oC; visid_incap_2269415=SnrfkV/xRM2/zMAwUwhS+8xj4GEAAAAAQkIPAAAAAACALOWhAWPmyCDb18oF6pHY12yEiWlUbIgr; nlbi_2269415=Vq3lX/59Tg3xXSVkkG5lugAAAAB+8mCpAlS1F5Timw4irGua; _gid=GA1.2.1583316853.1643415717; ASP.NET_SessionId=ov1iizcd3npobsilupzii5ep; nlbi_2271082=uYrYPyycJwjJZMEUcbDG1QAAAABYkXBfZhGO2s/HVfvOZarc; _gac_UA-12908513-11=1.1643468700.Cj0KCQiA6NOPBhCPARIsAHAy2zAmFT3_yol1CanQDHoHW_z8aJ6HgaY2f7iilRt6yGvssuzmDbbh8FoaAkpxEALw_wcB; reese84=3:R9V1thF3zfU1XzAsrmuqqw==:nB+hlWUK8YKFcNBilS0QI9rZ84RqPlXW5EuYuziGW1hsBJZ/ITopxflcaYX9mPK+3pw6lZfiiTtWMBNPd7RghkgEw94K+41ZrfCQ22umvM7EvU3pY7NUzr55xlEoUvSlcKTV59bEja1wW6MGEODWcQStcnPLWf0qBJEH/F970O+KNHadiiteNgbm+WF2QRe7F/iDFNKn2rWNK9UOGQTEq+vUTkizNBP6wle3Rz59JMZ4Dak5atrxULvJR9ha2X7blFXW4rZLe0YLrEJTnTgvlogCy2IppekNtui09pq9T5JBH7Ohrv4I8bJXUJYGIn1vTxuDhVkB3dEQxIMSsjk0aUWqFgSEfqJFjAlbDd98CBMjCjMcZOnjGrtHQ6cHExIhJ4qZY1PWiKw6wlM1dzt+YbJed3Bp7Z39OVx0p5prRjfFGii4GeryVuxm7FvT1joN:kT2/H9VmAKXNkl0oPylL7igZEL4qyfJtYQEBlh/+R+Y=; nlbi_2271082_2147483646=wqCqB+Pz10CU9ix2cbDG1QAAAABou7Z3m9/gbU6T/e0I3d/e; incap_ses_303_2269415=A7WPfSd/+nVF8RqgDHk0BFGI9WEAAAAA0cDdAY+/cAogsUDNlpNB3g==; incap_ses_303_2271082=6bfXOzBGFl4dbh6gDHk0BJqM9WEAAAAAFnnt12UHDTHyZc6pWTy9/g==; _ga=GA1.2.2104488426.1642095581; _ga_Y07J3B53QP=GS1.1.1643482261.23.1.1643482312.9; _4c_=%7B%22_4c_s_%22%3A%22bZNbi9swEIX%2FStDzOtFlbMt5K1koC4WWQuljUKxxLJJYRlbibkP%2Be0fOjV2qF0tnjj5bmuMzG1vs2FIUoEBLJUAW5Qvb4fvAlmcWnE2PE1uypkKocm6zMhc8A5Q800VtMoPGcBpNJYG9sD8Tq9KlyLXgeXF5Yba7Myw25riPd1vONWgAobQim%2BvjzZc%2BRoDWUGqpH17iX5XkvRMN%2B289jA%2FUtZDzEtQH66SQte5v1jOrvUViimouYE6HbAaix78kZYpzmvfB22Md1%2FG9T8YRN7PB7qhg8eRqXI%2FOxjYRpJBPtUW3beMk51WS%2B0ALOefXkVcFhwJAU2l0nfXjZ85N%2FczZBD8OmFirNvgDzl5x2EXfz6qSqp4ayH5PO9MxAjYYwuRuY%2ByH5WIxjuM8oNlHH%2Ba1WZBpcDGd6yneNIrDU84m%2BZvptkezne4rLf12i3b21qWkmP2ApP0I%2FuS6Olm%2Bd9EE50lc%2BWMXQ8KtTGdsQv3EwVnsojN7H1b%2BcMDgarOf3viokA%2B71PE%2BWJp%2F%2FbL%2B9faarlFwSFGRxZxiI3mVU%2B7Y5R5ElRcURaUKoE5GYuoCplsnx%2BmRIuSbhkshMlXYJgNVyoyaIjPatwGQlSmVfGSb%2FhMQQirIb0ihr8TL5R8%3D%22%7D; nlbi_2269415_2147483646=vLKqe7aBHXbR7iJwkG5lugAAAAAfxG3k5G38kDfkdhEpIeqz; reese84=3:WNwfhq2pDdC2bnkoSu5l4g==:5R34KYRfQaNh8p4Fx++uMiyBLhcNZQioajjrBaGGzcV0+BLy8tw9eccrJ7uh6mgkd2VtsP0o/z5XPxZBgdHdmHQpSEqRidZdsCsb07dOfdWHYS9C/ea6OweTK7MBma94pgzjl8BNIXtEMrsYcGA8SN8tkYQVfuwtxucqUU/eBOebuiEs2VEy2PmtenE2kWbuGE7fPtBY3KxGcCbPSbF/vaxiAClQFePrkRx6UM4TQpnRyNAzex9M7Tn1/pmmHWNvD4k+NNaMbFKV5Lm0ClP2tM+oNdrCueBRnOHGZfVI9jwkVP2C0go96e/y7ZP8YtrHwbzV0BpXtJQGtEAxQNgn982izdpRKg36pdbqpL7TxXfQdwnMtxQeBpISBXQgvIjNEe++x+Iia1dKzUqVsSyVMHdYb7FAbz826ipJIJiRlE4hroe4tzVVcLk2RbENV3Kf:/Ig9b61HCIagqhuUpGHbiaKQdS6MOtMWMQ00aHXDNnI=; _gali=lnkNextResultsPage",
    'authority': "api2.realtor.ca",
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
    'accept': "*/*",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'sec-ch-ua-mobile': "?1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
    'sec-ch-ua-platform': '"Android"',
    'origin': "https://www.realtor.ca",
    'sec-fetch-site': "same-site",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://www.realtor.ca/",
    'accept-language': "en-US,en;q=0.9"
    }

    def modify_payload(self, page_number):
        self.payload = f'ZoomLevel=11&LatitudeMax=43.99454&LongitudeMax=-79.05332&LatitudeMin=43.42026&LongitudeMin=-79.69945&Sort=6-D&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD&CurrentPage={page_number}&ApplicationId=1&CultureId=1&Version=7.0&RecordsPerPage=100'


    def start_requests(self):

        yield scrapy.Request(url=self.api,
                             callback=self.parse,
                             method='POST',
                             headers=self.headers,
                             body=self.payload)

    def parse(self, response):
        print('PARSE')
        data = json.loads(response.body)
        results = data.get('Results')
        print('results')
        for r in results:
            yield {
                'Id': r.get('Id'),
                'Price': r.get('Property').get('Price')
            }
        pagination = data.get('Paging')
        current_page = pagination.get('CurrentPage')
        next_page = int(current_page) + 1
        total_pages = pagination.get('TotalPages')
        print(next_page, total_pages)
        if(next_page < total_pages):
            self.modify_payload(next_page)
            yield scrapy.Request(url=self.api,
                                 callback=self.parse,
                                 method='POST',
                                 headers=self.headers,
                                 body=self.payload)


if __name__ == '__main__':
    import os
    from scrapy.cmdline import execute

    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    SPIDER_NAME = RealtorSpider.name
    try:
        execute(
            [
                'scrapy',
                'crawl',
                SPIDER_NAME,
                '-s',
                'FEED_EXPORT_ENCODING=utf-8',
            ]
        )
    except SystemExit:
        pass
