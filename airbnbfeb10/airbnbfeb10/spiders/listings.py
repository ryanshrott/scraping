import scrapy
import json
from urllib.parse import urlencode
from airbnbfeb10.items import ListingItem
import logging
import time 
from datetime import datetime
import base64
from urllib.parse import urlencode

class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['airbnb.ca']
    nPages = 3
    nItem = 0
    # logging 
    today_date = datetime.today()
    root_logger= logging.getLogger()
    root_logger.setLevel(logging.ERROR)
    handler = logging.FileHandler(f'C:\\Users\\Ryan\\projects\\airbnbfeb10\\airbnbfeb10\\log\\logging_{today_date.strftime("%y%m%d-%H%M%S")}.log', 'w', 'utf-8')
    handler.setFormatter(logging.Formatter('"%(asctime)s %(name)s:%(levelname)s:%(message)s"')) # or whatever
    root_logger.addHandler(handler)
    headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "DNT": "1",
            "Host": "www.airbnb.ca",
            "Pragma": "no-cache",
            "Referer": "https://www.airbnb.ca/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Sec-GPC": "1",
            "TE": "trailers",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
            "X-Airbnb-API-Key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
            "X-Airbnb-GraphQL-Platform": "web",
            "X-Airbnb-GraphQL-Platform-Client": "minimalist-niobe",
            "X-Airbnb-Supports-Airlock-V2": "true",
            "X-CSRF-Token": "null",
            "X-CSRF-Without-Token": "1",
            "X-KL-Ajax-Request": "Ajax_Request",
            "X-Niobe-Short-Circuited": "true"
        }
    
    @staticmethod
    def query_listings(page, itemsPerGrid=50):
        query = {"operationNames":"ExploreSections","locale":"en-CA","currency":"CAD","_cb":"0p0h2v80gbppbv0agiauz17tjo9e",
        "variables":"{\"isInitialLoad\":true,\"hasLoggedIn\":true,\"cdnCacheSafe\":false,\"source\":\"EXPLORE\",\"exploreRequest\":{\"metadataOnly\":false,\"version\":\"1.8.3\",\"itemsPerGrid\":" + f"{itemsPerGrid}" +",\"flexibleTripLengths\":[\"weekend_trip\"],\"datePickerType\":\"calendar\",\"placeId\":\"ChIJpTvG15DL1IkRd8S0KlBVNTI\",\"refinementPaths\":[\"/homes\"],\"tabId\":\"home_tab\",\"checkin\":\"2022-04-12\",\"checkout\":\"2022-04-13\",\"source\":\"structured_search_input_header\",\"searchType\":\"autocomplete_click\",\"federatedSearchSessionId\":\"e0168175-d333-413f-b3b3-5d9bb36cd9cf\",\"itemsOffset\":" + f"{str(itemsPerGrid*page)}" +",\"sectionOffset\":3,\"query\":\"Toronto, ON\",\"cdnCacheSafe\":false,\"treatmentFlags\":[\"flex_destinations_june_2021_launch_web_treatment\",\"new_filter_bar_v2_fm_header\",\"merch_header_breakpoint_expansion_web\",\"flexible_dates_12_month_lead_time\",\"storefronts_nov23_2021_homepage_web_treatment\",\"web_remove_duplicated_params_fields\",\"flexible_dates_options_extend_one_three_seven_days\",\"super_date_flexibility\",\"micro_flex_improvements\",\"micro_flex_show_by_default\",\"search_input_placeholder_phrases\",\"pets_fee_treatment\"],\"screenSize\":\"large\",\"isInitialLoad\":true,\"hasLoggedIn\":true},\"removeDuplicatedParams\":true}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"1cb8bde810f2d0469ed603796a970876815987bc4ff91f05bea3bf707e6f7aa2\"}}"}
        return query
    
    def start_requests(self):
        for page in range(1, self.nPages+1):
            querystring = ListingsSpider.query_listings(page)
            url = f"https://www.airbnb.ca/api/v3/ExploreSections?{urlencode(querystring)}"

            yield scrapy.Request(
                url=url,
                method='GET',
                headers=self.headers,
                callback=self.parse_listings,
            )
    
    def parse_listings(self, response):
        print('PARSE')
        json_data = json.loads(response.body)
        print(type(json_data))
        def get_query(encoded):
            return {"operationName":"StaysPdpSections","locale":"en-CA","currency":"CAD","_cb":"10mvec716p5tv21aeaj5g12w88yb",
                            "variables":'{\"id\":' + f'"{str(encoded)}\"' + ",\"pdpSectionsRequest\":{\"adults\":\"1\",\"bypassTargetings\":false,\"categoryTag\":null,\"causeId\":null,\"children\":null,\"disasterId\":null,\"discountedGuestFeeVersion\":null,\"displayExtensions\":null,\"federatedSearchId\":\"940e74ab-c1fe-492e-a5f4-87f8e205aad8\",\"forceBoostPriorityMessageType\":null,\"infants\":null,\"interactionType\":null,\"layouts\":[\"SIDEBAR\",\"SINGLE_COLUMN\"],\"pets\":0,\"pdpTypeOverride\":null,\"preview\":false,\"previousStateCheckIn\":null,\"previousStateCheckOut\":null,\"priceDropSource\":null,\"privateBooking\":false,\"promotionUuid\":null,\"relaxedAmenityIds\":null,\"searchId\":null,\"selectedCancellationPolicyId\":null,\"selectedRatePlanId\":null,\"staysBookingMigrationEnabled\":false,\"translateUgc\":null,\"useNewSectionWrapperApi\":false,\"sectionIds\":null,\"checkIn\":\"2022-03-08\",\"checkOut\":\"2022-03-09\"}}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"9f9b31d1ffc6fc68a2de67b8812732900d347f59256dc618df69c97c3521f10e\"}}"}
        with open('listings.json', 'w') as f:
            json.dump(json_data, f)
        try:
            sections = json_data.get('data').get('presentation').get('explore').get('sections').get('sections')
        except Exception as e:
            print(e)
        for section in sections:
            if section['sectionComponentType'] == 'EXPLORE_SECTION_WRAPPER' and 'PAGINATED' in section['sectionId']:
                for item in section['section']['child']['section']['items']:

                    listingInfo = item['listing'] 
                    listing = ListingItem(index=self.nItem, 
                                        timeStamp=datetime.now().strftime("%y%m%d-%H%M%S"),
                                        listingId=listingInfo['id'],
                                        url=f"https://www.airbnb.ca/rooms/{listingInfo['id']}",
                                        price=item.get('pricingQuote').get('price').get('total').get('amountFormatted')
                                            )
                    self.nItem += 1
                    print(listing['listingId'], listing['url'], listing['price'])
                    coded_string = 'StayListing:' + listing['listingId']
                    message_bytes = coded_string.encode('ascii')
                    encoded = base64.b64encode(message_bytes).decode('utf-8')
            
                    querystring = get_query(encoded) 
                    url_details = f"https://www.airbnb.ca/api/v3/StaysPdpSections?{urlencode(querystring)}"
                    yield scrapy.Request(
                        url=url_details,
                        method='GET',
                        headers=self.headers,
                        callback=self.parse_details,
                        meta= {'listing': listing}
                    )

    def parse_details(self, response):
        print('DETAILS')
        listing = response.request.meta['listing']
        id = listing['listingId']
        json_data = json.loads(response.body)
        #print(json_data)
        #print(type(json_data))
        with open('details.json', 'w') as f:
            json.dump(json_data, f)
        
        loggingContext = json_data['data']['presentation']['stayProductDetailPage']['sections']['metadata']['loggingContext']['eventDataLogging']
        lat = loggingContext['listingLat']
        lng = loggingContext['listingLng']
        listing['location'] = (lat, lng)
        listing['isSuperHost'] = loggingContext['isSuperhost']
        listing['numPictures'] = loggingContext['pictureCount']

        (listing['accuracyRating'], listing['checkinRating'], listing['cleanlinessRating'], 
        listing['communicationRating'], listing['locationRating'], listing['valueRating'], 
        listing['guestSatisfactionOverall'], listing['visibleReviewCount']) = (loggingContext['accuracyRating'], loggingContext['checkinRating'], loggingContext['cleanlinessRating'],
        loggingContext['communicationRating'], loggingContext['locationRating'], loggingContext['valueRating'],
        loggingContext['guestSatisfactionOverall'], loggingContext['visibleReviewCount'] )

        listing['hostContactInfo'] = f"https://www.airbnb.ca/contact_host/{id}/send_message"

        # listing description
        data = json_data['data']['presentation']['stayProductDetailPage']['sections']['sections']
        listing['descriptions'] = []
        listing['amenities'] = {}
        for d in data:
            if(d['sectionComponentType'] == 'PDP_DESCRIPTION_MODAL'):
                for x in d['section']['items']:
                    listing['descriptions'].append(x['html']['htmlText'])
            if(d['sectionComponentType'] == 'AMENITIES_DEFAULT'):
                for x in d['section']['seeAllAmenitiesGroups']:
                    listing['amenities'][x['title']] = [y['title'] for y in x['amenities']]
            if(d['sectionComponentType'] == 'PHOTO_TOUR_SCROLLABLE'):
                listing['title'] = d['section']['shareSave']['sharingConfig']['title']
                listing['propertyType'] = d['section']['shareSave']['sharingConfig']['propertyType']
                listing['personCapacity'] = d['section']['shareSave']['sharingConfig']['personCapacity']
            if(d['sectionComponentType'] == 'HOST_PROFILE_DEFAULT'):
                listing['hostName'] = d['section']['title']
                if(len(d['section']['hostTags']) > 0):
                    listing['hostNumReviews'] = d['section']['hostTags'][0]['title']
                for x in d['section']['hostFeatures']:
                    if(x['title'] ==  "Policy number"):
                        listing['policyNumber'] = x['subtitle']
                    if(x['title'] ==  "Languages"):
                        listing['languages'] = x['subtitle']
                    if(x['title'] ==  "Response rate"):
                        listing['responseRate'] = x['subtitle']
                    if(x['title'] ==  "Response time"):
                        listing['responseTime'] = x['subtitle']
                listing['hostJoinDate'] = d['section']['hostBasicInfos'][0]['title']
                listing['hostId'] = d['section']['hostAvatar']['userId']
            if(d['sectionComponentType'] == 'OVERVIEW_DEFAULT'):
                numItems = len(d['section']['detailItems'][1:])
                if(numItems > 0):
                    listing['numberOfBedrooms'] = d['section']['detailItems'][1]['title']
                if(numItems > 1):
                    if(listing['numberOfBedrooms'] == "Studio"):
                        listing['numberOfBathrooms'] = d['section']['detailItems'][2]['title']
                    else:
                        listing['numberOfBeds'] = d['section']['detailItems'][2]['title']
                if(numItems > 2):
                    listing['numberOfBathrooms'] = d['section']['detailItems'][3]['title'] 

     #   print('Description: ', listing['descriptions'])  
     #   print('*********************************************************************************************')
      #  print('Amenities: ', listing['amenities'])
      #  print('*********************************************************************************************')
        url_avail = "https://www.airbnb.ca/api/v3/PdpAvailabilityCalendar"
        querystring = {"operationName":"PdpAvailabilityCalendar","locale":"en-CA","currency":"CAD","_cb":"1so46um0i1hlnn1ide7l016vtvhu","variables":
            "{\"request\":{\"count\":12,\"listingId\":" + f'\"{id}\"' + ",\"month\":2,\"year\":2022}}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"8f08e03c7bd16fcad3c92a3592c19a8b559a0d0855a84028d1163d4733ed9ade\"}}"}
        url_avail = f"https://www.airbnb.ca/api/v3/StaysPdpSections?{urlencode(querystring)}"

        yield scrapy.Request(url=url_avail,
                            method='GET',
                            headers=self.headers,
                            callback=self.parse_availability,
                            meta={'listing': listing})

    def parse_availability(self, response):
        print('parse_availability IN')
        listing = response.request.meta['listing']
        json_data = json.loads(response.body)
        with open('avail.json', 'w') as f:
            json.dump(json_data, f)

        availability = {}
        for month in json_data.get('data').get('merlin').get('pdpAvailabilityCalendar').get('calendarMonths'):
            for day in month.get('days'):
                availability[day.get('calendarDate')] = day.get('available')
        print('parse_availability OUT')
        #listing['occupancyTable'] = availability
        yield listing
