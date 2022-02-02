from lxml import html
import httpx
import requests
from bs4 import BeautifulSoup
import json
import requests_html


headers = 	{
	'accept':'*/*',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
	}

#you could parameterise the search to get more results: areas, pages, dates etc
url = 'https://www.airbnb.ca/s/Toronto/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-02-16&checkout=2022-02-17&adults=2&federated_search_session_id=3cae07b5-d881-4d36-b987-b0750724d96b&pagination_search=true&items_offset=0&section_offset=3'

def get_url(page):
    url = f'https://www.airbnb.ca/s/Toronto/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Toronto&place_id=ChIJpTvG15DL1IkRd8S0KlBVNTI&source=structured_search_input_header&search_type=autocomplete_click&checkin=2022-02-16&checkout=2022-02-17&adults=2&federated_search_session_id=3cae07b5-d881-4d36-b987-b0750724d96b&pagination_search=true&items_offset={2*page}&section_offset=3'
    return url


i=0
pages = 3
for j in range(pages):
    print(f'page : {j+1}')
    resp = requests.get(get_url(j),headers=headers)

    soup = BeautifulSoup(resp.text,'html.parser')

    data_state = soup.find('script',{'id':"data-deferred-state"})
    json_data = json.loads(data_state.text)
    session = requests_html.HTMLSession()
    for section in json_data['niobeMinimalClientData'][0][1]['data']['presentation']['explore']['sections']['sections']:
        try:
            for item in section['section']['child']['section']['items']:
                listing = item['listing'] #all listing details here
                price = item['pricingQuote'] #all price details here

                print(f"https://www.airbnb.ca/rooms/{listing['id']} price: {price['price']['total']['amountFormatted']}")

                r = session.get(f"https://www.airbnb.ca/rooms/{listing['id']}")
                r.html.render(sleep=5, timeout=8)
                print(r.html.xpath("//h2[@class='_14i3z6h']/text()"))
                print(r.html.xpath("((//div[@data-plugin-in-point-id='DESCRIPTION_DEFAULT']//span)[1]//span)[1]/text()"))
                print('*********************************************************************************************')
                days = r.html.xpath("//div[@class='_ytfarf']//td//div")
                print(days)
                i = i + 1
                print(i)

        except KeyError:
            pass #not every section has listings
    session.close()


print(f'Scraped {i} listings')