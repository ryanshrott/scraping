import scrapy
import base64
import json
from urllib.parse import urlencode

class DetailsSpider(scrapy.Spider):
    name = 'details'
    allowed_domains = ['airbnb.ca']

    def start_requests(self):
        url = "https://www.airbnb.ca/api/v3/StaysPdpSections"
        coded_string = 'StayListing:52780274'
        message_bytes = coded_string.encode('ascii')
        encoded = base64.b64encode(message_bytes).decode('utf-8')
        querystringDynamic = {"operationName":"StaysPdpSections","locale":"en-CA","currency":"CAD","_cb":"10mvec716p5tv21aeaj5g12w88yb",
                "variables":'{\"id\":' + f'"{str(encoded)}\"' + ",\"pdpSectionsRequest\":{\"adults\":\"1\",\"bypassTargetings\":false,\"categoryTag\":null,\"causeId\":null,\"children\":null,\"disasterId\":null,\"discountedGuestFeeVersion\":null,\"displayExtensions\":null,\"federatedSearchId\":\"940e74ab-c1fe-492e-a5f4-87f8e205aad8\",\"forceBoostPriorityMessageType\":null,\"infants\":null,\"interactionType\":null,\"layouts\":[\"SIDEBAR\",\"SINGLE_COLUMN\"],\"pets\":0,\"pdpTypeOverride\":null,\"preview\":false,\"previousStateCheckIn\":null,\"previousStateCheckOut\":null,\"priceDropSource\":null,\"privateBooking\":false,\"promotionUuid\":null,\"relaxedAmenityIds\":null,\"searchId\":null,\"selectedCancellationPolicyId\":null,\"selectedRatePlanId\":null,\"staysBookingMigrationEnabled\":false,\"translateUgc\":null,\"useNewSectionWrapperApi\":false,\"sectionIds\":null,\"checkIn\":\"2022-03-08\",\"checkOut\":\"2022-03-09\"}}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"9f9b31d1ffc6fc68a2de67b8812732900d347f59256dc618df69c97c3521f10e\"}}"}
        url = f"https://www.airbnb.ca/api/v3/StaysPdpSections?{urlencode(querystringDynamic)}"
        print(querystringDynamic['variables'][:50])

        headersWorking = {
                "cookie": "bev=1644501377_NmE3ZDcwN2U4YjVi; _aat=0%7C41661hs5NucrAsfvROXi255Teed27zrKoKON8fLjH3w5GlwuHJhgodCaR16zRuNt; abb_fa2=%7B%22user_id%22%3A%2260%7C1%7CL1lPultHbtDMRdFrINuT%2FMk7kwNhqhClUk4q%2Fd19W92FfMm%2BAnQpNiY%3D%22%7D; _airbed_session_id=491c3bc938577ed8955a91e711408659; _abck=C77BE1F7B78379A2185496EEDA7F5DF8~0~YAAQDcaISCSQItl+AQAAN1KR7gc5rSP3xBzu+oWnIwAFMKLckvWqMuek7PRkV6lVoRQ00EIX+hcp/wjIQenXxPE2TqkXEBFQIIKCW4w+1XPj+FwSNkQ8xskwtZQCGfnleudCoNRyFdFxQp4QdPBejrwL+IGiRjli+q3eJpOXHXq7KvXJadkfKq1klDjWM7LcAq9W2GHlXr/MsBS9pG97wANu9UOFp3ZIfIDppNC2Z7KlDoGeE6ve/bTSD2zxgPJqTKO7ciXY1CCETL9bf2cIfeDu2PvhppRll3vB2zpCTPVRfX5r5MzzKipjZ+/9iOR9qkqUrQi6MQaoFySi/K/85eFrE60CWb0M3euBn29zgBDwOTbEaJ4m0QXbDIDfectz7SewSs/agXMoDWtGD6VqUss2vzhTzOY=~-1~-1~-1; bm_sz=B47447B3E4C5B3F44E7F59246C467B76~YAAQDcaISCWQItl+AQAAN1KR7g5PYlSi+Gr6rdkg2W1VWGkENewfodb80Li9DG8Ip4RgNBHJjT9msSfi0iOaGS2D+J8hyNwylMYCPYXTk1TqfH9OpeWIopwJ1Gn6yQbZeuILsjwy/qj888TlIx/Q7zZkFhb4VqKX/Y2SZsOYQWe8o8iqB99sj6VwwPFvnuEQ7ALu6M9jtaV123d1AjBLJKJDcgdfBkfWX4j5x0l5tab/bAUg5HLVtLf8OwH+Odh6BPU6mT4Utpm9nu4jZ9jA/Wd6YQFck+hf8cUOfaImwHvQSQ==~4604483~3290936; _csrf_token=V4%24.airbnb.ca%24bpzSB3wPQHE%24TgT-tubi-fJjF21SelKp7JIyB9cGuVC09_kXjvyeXRM%3D; flags=0; roles=0; OptanonConsent=0_179751%3A1%2C0_183217%3A1%2C0_183345%3A1%2C0_183219%3A1%2C0_183240%3A1%2C0_200002%3A1%2C0_179747%3A1%2C0_179756%3A1%2C0_183241%3A1%2C0_200003%3A1%2C0_200007%3A1%2C0_200004%3A1%2C0_200005%3A1%2C0_179739%3A1%2C0_179743%3A1%2C0_185813%3A1%2C0_183096%3A1%2C0_179755%3A1%2C0_185808%3A1%2C0_179740%3A1%2C0_179744%3A1%2C0_185814%3A1%2C0_183097%3A1%2C0_183344%3A1%2C0_185809%3A1%2C0_179748%3A1%2C0_179752%3A1%2C0_179741%3A1%2C0_183098%3A1%2C0_179745%3A1%2C0_183346%3A1%2C0_185811%3A1%2C0_179737%3A1%2C0_179757%3A1%2C0_179749%3A1%2C0_179753%3A1%2C0_185831%3A1%2C0_183099%3A1%2C0_179738%3A1%2C0_179742%3A1%2C0_183095%3A1%2C0_179754%3A1%2C0_179750%3A1%2C0_200008%3A1%2C0_200009%3A1%2C0_200010%3A1%2C0_200006%3A1%2C0_200011%3A1%2C0_200012%3A1; OptanonAlertBoxClosed=2022-02-12T15%3A39%3A33.750Z; cdn_exp_44f412bd466ffe35b=control; cdn_exp_15383cd1580337cf3=treatment; cdn_exp_90bbb75bab0d2037e=treatment; cdn_exp_dcefc80b9923f2e83=treatment; jitney_client_session_id=94842ed1-df0d-402f-9b9d-65b7dcc369f0; jitney_client_session_created_at=1644687124; cfrmfctr=MOBILE; cbkp=1; _ga_2P6Q8PGG16=GS1.1.1644687126.3.1.1644691205.57; previousTab=%7B%22id%22%3A%22245c9730-945d-4f7a-aef1-82bef3f9b08f%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.ca%2Frooms%2F47452643%3Fsource_impression_id%3Dp3_1644691201_eOOkAbdjZmaQUMgX%22%7D; _user_attributes=%7B%22curr%22%3A%22CAD%22%2C%22guest_exchange%22%3A1.27238%2C%22device_profiling_session_id%22%3A%221644528814--df68d8398c1a2b5f12c6d8a7%22%2C%22giftcard_profiling_session_id%22%3A%221644690943-438786010-ef62fa21060380ae398ac36e%22%2C%22reservation_profiling_session_id%22%3A%221644690943-438786010-671a2d2e1d1c10580e62ee37%22%2C%22id%22%3A438786010%2C%22hash_user_id%22%3A%22410bff6ec88cee3ed5cd3e6ef79d9b3422bc408e%22%2C%22eid%22%3A%22ZWQOAFmIX9xrcAFUswTKIw%3D%3D%22%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22Ryan%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3Anull%2C%22receiver_savings_percent%22%3Anull%2C%22receiver_signup%22%3Anull%2C%22referrer_guest%22%3A%22%2425+CAD%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3Anull%2C%22offer_discount_type%22%3Anull%7D%7D; frmfctr=compact; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.2096187383.1644691214; _gid=GA1.2.1252868348.1644691214; _gat=1; jitney_client_session_updated_at=1644691213",
                "authority": "www.airbnb.ca",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                "x-csrf-token": "V4$.airbnb.ca$bpzSB3wPQHE$TgT-tubi-fJjF21SelKp7JIyB9cGuVC09_kXjvyeXRM=",
                "x-airbnb-api-key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
                "x-niobe-short-circuited": "true",
                "dpr": "1.5",
                "sec-ch-ua-platform": '"Windows"',
                "device-memory": "8",
                "x-airbnb-graphql-platform-client": "minimalist-niobe",
                "sec-ch-ua-mobile": "?0",
                "x-csrf-without-token": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
                "viewport-width": "716",
                "content-type": "application/json",
                "x-airbnb-supports-airlock-v2": "true",
                "ect": "4g",
                "x-airbnb-graphql-platform": "web",
                "accept": "*/*",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.airbnb.ca/rooms/47452643?source_impression_id=p3_1644691201_eOOkAbdjZmaQUMgX",
                "accept-language": "en-US,en;q=0.9",
                'Accept-Encoding': 'gzip, deflate, br', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'DNT': '1', 'Host': 'www.airbnb.ca', 'Pragma': 'no-cache', 'Sec-GPC': '1', 'TE': 'trailers', 'X-KL-Ajax-Request': 'Ajax_Request'
            }
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
        yield scrapy.Request(
            url=url,
            method='GET',
            headers=headers,
            callback=self.parse_details
        )

    def parse_details(self, response):
        print('PARSE')
        json_data = json.loads(response.body)
        print(json_data)
        print(type(json_data))
        with open('details.json', 'w') as f:
            json.dump(json_data, f)



    