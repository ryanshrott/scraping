from lxml import html
import httpx
import requests
from bs4 import BeautifulSoup
import json
  
import requests_html
session = requests_html.HTMLSession()
r = session.get("https://www.airbnb.ca/rooms/48058366")
r.html.render(sleep=5, timeout=8)


print(r.html.xpath("//h2[@class='_14i3z6h']"))
print(r.html.xpath("((//div[@data-plugin-in-point-id='DESCRIPTION_DEFAULT']//span)[1]//span)[1]/text()"))
print('*********************************************************************************************')

days = r.html.xpath("//div[@class='_ytfarf']//td//div//@data-testid")
availability = r.html.xpath("//div[@class='_ytfarf']//td//div//@data-is-day-blocked")

print(availability)
