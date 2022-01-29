        # -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver 
from shutil import which 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
        
#chrome_options.add_argument("--headless")
chrome_path = which("chromedriver")

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.realtor.ca")
time.sleep(1) 
search_inp  = driver.find_element_by_xpath("//input[@id='homeSearchTxt']")

search_inp.send_keys("Toronto")


search_btn = driver.find_element_by_id('homeSearchBtn')
search_btn.click()

list_btn = driver.find_element_by_xpath("(//div[@class='toggleSwitchInnerCon'])[2]/a[2]")
list_btn.click()

link_elements = driver.find_elements_by_xpath("//*[@id='listInnerCon']//div[1]/a")

links = []

for link in link_elements:
    href = link.get_attribute('href')
    print(href)
    links.append(href)
driver.close()