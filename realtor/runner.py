import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from realtor.spiders.listings2 import Listings2Spider


process = CrawlerProcess(settings=get_project_settings())
process.crawl(Listings2Spider)
process.start()