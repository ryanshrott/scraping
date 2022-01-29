        # -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver 
from shutil import which 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
        
#chrome_options.add_argument("--headless")

def init_driver():
    chrome_path = which("chromedriver")

    chrome_options = webdriver.ChromeOptions(); 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.airbnb.ca/s/Toronto--ON/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto%2C%20ON&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&checkin=2022-02-03&checkout=2022-02-04&adults=5&source=structured_search_input_header&search_type=filter_change&ne_lat=43.71490168362106&ne_lng=-79.38440082661077&sw_lat=43.58555929640049&sw_lng=-79.46489213275458&zoom=13&search_by_map=true")
    time.sleep(1) 

    return driver

def get_links(driver, links, page):
    print(f"On page number {page}")
    link_elements = driver.find_elements_by_xpath("//div[@class='c1o3pz3i dir dir-ltr']/a")

    for link in link_elements:
        href = link.get_attribute('href')
        print(href)
        links.append(href)

    try:
        privacy_btn = driver.find_element_by_xpath("//button[@data-testid='accept-btn']")
        privacy_btn.click()
        time.sleep(1) 
    except Exception as e:
        pass

    try:
        next_button = driver.find_element_by_xpath("//a[@aria-label='Next']")
        next_button.click()
        time.sleep(2) 
        get_links(driver, links, page+1)
    except Exception as e:
        print('Done!')
        print(len(links))
        driver.close()
        return links


driver = init_driver()

links = get_links(driver, [], 0)

print(links)



