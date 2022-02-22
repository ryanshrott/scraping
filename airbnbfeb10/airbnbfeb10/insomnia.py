import requests

url = "https://www.airbnb.ca/api/v3/StaysPdpSections"

querystring = {"operationName":"StaysPdpSections","locale":"en-CA","currency":"CAD","_cb":"10mvec716p5tv21aeaj5g12w88yb","variables":"{\"id\":\"U3RheUxpc3Rpbmc6NTA0MjAxMjE=\",\"pdpSectionsRequest\":{\"adults\":\"1\",\"bypassTargetings\":false,\"categoryTag\":null,\"causeId\":null,\"children\":null,\"disasterId\":null,\"discountedGuestFeeVersion\":null,\"displayExtensions\":null,\"federatedSearchId\":\"940e74ab-c1fe-492e-a5f4-87f8e205aad8\",\"forceBoostPriorityMessageType\":null,\"infants\":null,\"interactionType\":null,\"layouts\":[\"SIDEBAR\",\"SINGLE_COLUMN\"],\"pets\":0,\"pdpTypeOverride\":null,\"preview\":false,\"previousStateCheckIn\":null,\"previousStateCheckOut\":null,\"priceDropSource\":null,\"privateBooking\":false,\"promotionUuid\":null,\"relaxedAmenityIds\":null,\"searchId\":null,\"selectedCancellationPolicyId\":null,\"selectedRatePlanId\":null,\"staysBookingMigrationEnabled\":false,\"translateUgc\":null,\"useNewSectionWrapperApi\":false,\"sectionIds\":null,\"checkIn\":\"2022-03-08\",\"checkOut\":\"2022-03-09\"}}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"9f9b31d1ffc6fc68a2de67b8812732900d347f59256dc618df69c97c3521f10e\"}}"}

headers = {
    "cookie": "bev=1644501377_NmE3ZDcwN2U4YjVi; _aat=0%7C41661hs5NucrAsfvROXi255Teed27zrKoKON8fLjH3w5GlwuHJhgodCaR16zRuNt; abb_fa2=%7B%22user_id%22%3A%2260%7C1%7CL1lPultHbtDMRdFrINuT%2FMk7kwNhqhClUk4q%2Fd19W92FfMm%2BAnQpNiY%3D%22%7D; _airbed_session_id=491c3bc938577ed8955a91e711408659; _csrf_token=V4%24.airbnb.ca%24bpzSB3wPQHE%24TgT-tubi-fJjF21SelKp7JIyB9cGuVC09_kXjvyeXRM%3D; flags=0; roles=0; OptanonConsent=0_179751%3A1%2C0_183217%3A1%2C0_183345%3A1%2C0_183219%3A1%2C0_183240%3A1%2C0_200002%3A1%2C0_179747%3A1%2C0_179756%3A1%2C0_183241%3A1%2C0_200003%3A1%2C0_200007%3A1%2C0_200004%3A1%2C0_200005%3A1%2C0_179739%3A1%2C0_179743%3A1%2C0_185813%3A1%2C0_183096%3A1%2C0_179755%3A1%2C0_185808%3A1%2C0_179740%3A1%2C0_179744%3A1%2C0_185814%3A1%2C0_183097%3A1%2C0_183344%3A1%2C0_185809%3A1%2C0_179748%3A1%2C0_179752%3A1%2C0_179741%3A1%2C0_183098%3A1%2C0_179745%3A1%2C0_183346%3A1%2C0_185811%3A1%2C0_179737%3A1%2C0_179757%3A1%2C0_179749%3A1%2C0_179753%3A1%2C0_185831%3A1%2C0_183099%3A1%2C0_179738%3A1%2C0_179742%3A1%2C0_183095%3A1%2C0_179754%3A1%2C0_179750%3A1%2C0_200008%3A1%2C0_200009%3A1%2C0_200010%3A1%2C0_200006%3A1%2C0_200011%3A1%2C0_200012%3A1; OptanonAlertBoxClosed=2022-02-12T15%3A39%3A33.750Z; cdn_exp_44f412bd466ffe35b=control; cdn_exp_15383cd1580337cf3=treatment; cdn_exp_90bbb75bab0d2037e=treatment; cdn_exp_dcefc80b9923f2e83=treatment; cfrmfctr=DESKTOP; frmfctr=wide; _abck=C77BE1F7B78379A2185496EEDA7F5DF8~0~YAAQD8aISEJnp69+AQAANnsI8AdxI5A79s190bPNhfFpS0D2MC4BC9gWMFC/r7Y/12AnaKs8zzkpCw+vEdoEjQnLmXYh7QozFruoDmdxbIUjEMae85b76c7RDJfH37tBjkZ6v6nxr/BESl0n1zd2fZsRzgmo2kha6Zhkf/DUmkqWhN0Cu8JGAPt4bxjn3cuFHP4VFKxDAxTX4NF7yMBIQTUkJG8mCw58n6ALLfU5bO6uuE362gcXd+7cjGKTuijdxzYFgFmONb+CtkGuZogBZoUd/jNzSLh4xkDipfqYhE4m9mQzFAXOGohPQCvA04xXDKnIDLR9/pi9qXESn0h6fe3GMfoTThAd7wELdefSX6f+qcv55Ab4PIufxYUFSiZHUn3G3oxm4i44eW6dqAjBA/dpqZU0tVg=~-1~-1~-1; bm_sz=C1922A9BB33B15D174751A13530380DE~YAAQD8aISENnp69+AQAANnsI8A45W8sa+bfryPq9EiErii41z/4HhV0ZWDYEDqabpjaab3fVwgrDC66cBsh59sFGKVJtBMkovYc3tAQgZZ+SusAusUNjhhX50cml+vKoSTywfZMLhb33crstNPOpexsMmLEFqz54FVzU4vj19c3BoS8u+//7FEZuJt0ASaHWXrRKMKF7c63VX2qt6QZ5zEiYl47gNIpD6IqlYcQ1yv47HiiCkry2I9DVBdp5OOexANvNoUKJtYeAMk/vufGHN85gThOENXpeOQdW4FOH09xuZA==~4339508~3687729; previousTab=%7B%22id%22%3A%22aee1e3ce-47aa-4f6e-9b9b-2d1137cd1030%22%2C%22url%22%3A%22https%3A%2F%2Fwww.airbnb.ca%2Frooms%2F50420121%3Fcheck_in%3D2022-03-08%26check_out%3D2022-03-09%26federated_search_id%3D940e74ab-c1fe-492e-a5f4-87f8e205aad8%26source_impression_id%3Dp3_1644691066_P8p%252FJXerTr8bUu6c%22%7D; AMP_TOKEN=%24NOT_FOUND; jitney_client_session_id=daf9490c-313a-4563-993d-b843f4c648e2; jitney_client_session_created_at=1644704594; _gid=GA1.2.66999108.1644704595; _gat=1; _gcl_au=1.1.1688292422.1644704596; _ga_2P6Q8PGG16=GS1.1.1644704596.4.0.1644704596.60; _uetsid=ff2ed3c08c1911ec9878f377d950a650; _uetvid=ff2f2f508c1911ecbdd1c153c7aafc34; cbkp=3; _pt=1--WyI0MTBiZmY2ZWM4OGNlZTNlZDVjZDNlNmVmNzlkOWIzNDIyYmM0MDhlIl0%3D--a31ffdeeee304547a57078badfc3db76a734b81f; tzo=-300; jitney_client_session_updated_at=1644704600; _user_attributes=%7B%22curr%22%3A%22CAD%22%2C%22guest_exchange%22%3A1.27238%2C%22device_profiling_session_id%22%3A%221644528814--df68d8398c1a2b5f12c6d8a7%22%2C%22giftcard_profiling_session_id%22%3A%221644704595-438786010-e911296f2ba7dc1886d26afc%22%2C%22reservation_profiling_session_id%22%3A%221644704595-438786010-5486329739f3599a7a413977%22%2C%22id%22%3A438786010%2C%22hash_user_id%22%3A%22410bff6ec88cee3ed5cd3e6ef79d9b3422bc408e%22%2C%22eid%22%3A%22ZWQOAFmIX9xrcAFUswTKIw%3D%3D%22%2C%22num_h%22%3A0%2C%22num_trip_notif%22%3A0%2C%22name%22%3A%22Ryan%22%2C%22num_action%22%3A0%2C%22is_admin%22%3Afalse%2C%22can_access_photography%22%3Afalse%2C%22travel_credit_status%22%3Anull%2C%22referrals_info%22%3A%7B%22receiver_max_savings%22%3Anull%2C%22receiver_savings_percent%22%3Anull%2C%22receiver_signup%22%3Anull%2C%22referrer_guest%22%3A%22%2425+CAD%22%2C%22terms_and_conditions_link%22%3A%22%2Fhelp%2Farticle%2F2269%22%2C%22wechat_link%22%3Anull%2C%22offer_discount_type%22%3Anull%7D%7D; _ga=GA1.2.344962597.1644704595",
    "authority": "www.airbnb.ca",
    "x-airbnb-api-key": "d306zoyjsyarp7ifhu67rjxn52tv0t20",
    "x-niobe-short-circuited": "true",
    "dpr": "1.5",
    "device-memory": "8",
    "x-airbnb-graphql-platform-client": "minimalist-niobe",
    "sec-ch-ua-mobile": "?0",
    "x-csrf-without-token": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "viewport-width": "1356",
    "content-type": "application/json",
    "x-airbnb-supports-airlock-v2": "true",
    "ect": "4g",
    "x-airbnb-graphql-platform": "web",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.airbnb.ca/rooms/50420121?check_in=2022-03-08&check_out=2022-03-09&federated_search_id=940e74ab-c1fe-492e-a5f4-87f8e205aad8&source_impression_id=p3_1644691066_P8p%2FJXerTr8bUu6c",
    "accept-language": "en-US,en;q=0.9"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)