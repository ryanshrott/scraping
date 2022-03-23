import scrapy
from ..items import SteamItem
import json
from urllib.parse import urlencode
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com']
    #start_urls = ['https://store.steampowered.com/search/?filter=topsellers/']

    payload = ""
    headers = {
            "Connection": "keep-alive",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
            "X-Prototype-Version": "1.7",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://store.steampowered.com/search/?filter=topsellers/",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": "browserid=2641930369710941690; sessionid=1d12726f27edc111922f86f2; timezoneOffset=-14400,0; _ga=GA1.2.594756377.1647808505; steamCountry=CA%7C624e00eec742d7493d8b44d3d1a0367d; _gid=GA1.2.2023452283.1647984245; app_impressions=252490@1_7_7_230_150_1|1506830@1_7_7_230_150_1|39210@1_7_7_230_150_1|386360@1_7_7_230_150_1|271590@1_7_7_230_150_1|1621690@1_7_7_230_150_1|1222670@1_7_7_230_150_1|1174180@1_7_7_230_150_1|359550@1_7_7_230_150_1|1085660@1_7_7_230_150_1|1599340@1_7_7_230_150_1|730@1_7_7_230_150_1|1172470@1_7_7_230_150_1|1245620@1_7_7_230_150_1"
        }

    def start_requests(self):

        url = "https://store.steampowered.com/search/results"

        querystring = {"query":"","start":0*25,"count": (0+1) * 25,"dynamic_data":"","sort_by":"_ASC","snr":"1_7_7_230_7","infinite":"1"}
        url = f"https://store.steampowered.com/search/results?{urlencode(querystring)}"
        yield scrapy.Request(
            url=url,
            method='GET',
            body=json.dumps(self.payload),
            headers=self.headers,
            callback=self.parse
        )
        
    def parse(self, response):
        print('PARSE')
        json_data = json.loads(response.body)
        html = json_data.get('results_html')
        selector = Selector(text=html)
        with open('data.html', 'w') as f:
            json.dump(html, f)
        games = selector.xpath("//a")
        for game in games:
            loader = ItemLoader(item=SteamItem(), selector=game, response=selector)
            loader.add_xpath('game_url', ".//@href")
            loader.add_xpath('image_url', ".//div[@class='col search_capsule']/img/@src")
            loader.add_xpath('game_item', ".//span[@class='title']/text()")
            loader.add_xpath('release_date', ".//div[@class='col search_released responsive_secondrow']/text()")
            loader.add_xpath('platforms', ".//span[contains(@class, 'platform_img') or @class='vr_supported']/@class")
            loader.add_xpath('reviews_summary', "///span[contains(@class,'search_review_summary')]/@data-tooltip-html")
            loader.add_xpath('discount_rate', ".//div[contains(@class, 'search_discount')]//span/text()")
            loader.add_xpath('original_price', './/div[contains(@class, "search_price_discount_combined")]')
            loader.add_xpath('discounted_price', "(.//div[contains(@class, 'search_price discounted')]/text())[2]")
            yield loader.load_item()

        for i in range(1,5):        
            querystring = {"query":"","start":i*25,"count": (i+1) * 25,"dynamic_data":"","sort_by":"_ASC","snr":"1_7_7_230_7","infinite":"1"}
            url = f"https://store.steampowered.com/search/results?{urlencode(querystring)}"
            yield scrapy.Request(
                url=url,
                method='GET',
                body=json.dumps(self.payload),
                headers=self.headers,
                callback=self.parse
            )