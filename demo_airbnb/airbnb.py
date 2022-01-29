import requests
from bs4 import BeautifulSoup
import json
  
headers = 	{
	'accept':'*/*',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
	}

#you could parameterise the search to get more results: areas, pages, dates etc
url = 'https://www.airbnb.ca/s/Mayrhofen--Austria/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=april&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Mayrhofen%2C%20Austria&place_id=ChIJbzLYLzjdd0cRDtGuTzM_vt4&source=structured_search_input_header&search_type=filter_change&checkin=2022-01-05&checkout=2022-01-12'

resp = requests.get(url,headers=headers)

soup = BeautifulSoup(resp.text,'html.parser')

data_state = soup.find('script',{'id':"data-deferred-state"})
json_data = json.loads(data_state.text)

for section in json_data['niobeMinimalClientData'][0][1]['data']['presentation']['explore']['sections']['sections']:
    try:
        for item in section['section']['child']['section']['items']:
            listing = item['listing'] #all listing details here
            price = item['pricingQuote'] #all price details here

            print(f"https://www.airbnb.ca/rooms/{listing['id']} price: {price['price']['total']['amountFormatted']}")

    except KeyError:
        pass #not every section has listings