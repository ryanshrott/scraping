# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver 
from shutil import which 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware

class ListingSpider(scrapy.Spider):
    name = 'listing'
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    @staticmethod
    def init_driver():
        chrome_options = webdriver.ChromeOptions(); 
        chrome_path = which("chromedriver")
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('disable-infobars')
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.get("https://www.airbnb.ca/s/Toronto--ON/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto%2C%20ON&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&checkin=2022-02-03&checkout=2022-02-04&adults=5&source=structured_search_input_header&search_type=filter_change&ne_lat=43.71490168362106&ne_lng=-79.38440082661077&sw_lat=43.58555929640049&sw_lng=-79.46489213275458&zoom=13&search_by_map=true")
        time.sleep(1) 

        return driver

    @staticmethod
    def get_links(driver, page):
        print(f"On page number {page}")
        link_elements = driver.find_elements_by_xpath("//div[@class='c1o3pz3i dir dir-ltr']/a")

        for link in link_elements:
            href = link.get_attribute('href')
            print(href)
            yield scrapy.Request(href)

        try:
            privacy_btn = driver.find_element_by_xpath("//button[@data-testid='accept-btn']")
            privacy_btn.click()
            time.sleep(3) 
        except Exception as e:
            pass

        try:
            next_button = driver.find_element_by_xpath("//a[@aria-label='Next']")
            next_button.click()
            time.sleep(3) 
            ListingSpider.get_links(driver, page+1)
        except Exception as e:
            print('Done!')
            driver.close()
            return 

    def start_requests(self):
        print('Start requests')

        chrome_options = webdriver.ChromeOptions(); 
        chrome_path = which("chromedriver")
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('disable-infobars')
        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.get("https://www.airbnb.ca/s/Toronto--ON/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto%2C%20ON&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&checkin=2022-02-03&checkout=2022-02-04&adults=5&source=structured_search_input_header&search_type=filter_change&ne_lat=43.71490168362106&ne_lng=-79.38440082661077&sw_lat=43.58555929640049&sw_lng=-79.46489213275458&zoom=13&search_by_map=true")
        time.sleep(1)         
        ListingSpider.get_links(driver, 0)
        link_elements = driver.find_elements_by_xpath("//div[@class='c1o3pz3i dir dir-ltr']/a")

        for link in link_elements:
            href = link.get_attribute('href')
            print(href)
            yield scrapy.Request(href, dont_filter=True, headers={'User-Agent': self.user_agent}, meta = {'dont_redirect': True,'handle_httpstatus_list': [301, 302, 403] })

        try:
            privacy_btn = driver.find_element_by_xpath("//button[@data-testid='accept-btn']")
            privacy_btn.click()
            time.sleep(3) 
        except Exception as e:
            pass

    def parse(self, response):
        yield {
            'name' : response.xpath('//h1/text()').get()
        }