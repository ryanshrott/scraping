from urllib.parse import urlencode, parse_qsl


def query_listings(page, itemsPerGrid=50):
    query = {"operationNames":"ExploreSections","locale":"en-CA","currency":"CAD","_cb":"0p0h2v80gbppbv0agiauz17tjo9e",
    "variables":"{\"isInitialLoad\":true,\"hasLoggedIn\":true,\"cdnCacheSafe\":false,\"source\":\"EXPLORE\",\"exploreRequest\":{\"metadataOnly\":false,\"version\":\"1.8.3\",\"itemsPerGrid\":" + f"{itemsPerGrid}" +",\"flexibleTripLengths\":[\"weekend_trip\"],\"datePickerType\":\"calendar\",\"placeId\":\"ChIJpTvG15DL1IkRd8S0KlBVNTI\",\"refinementPaths\":[\"/homes\"],\"tabId\":\"home_tab\",\"checkin\":\"2022-04-12\",\"checkout\":\"2022-04-13\",\"source\":\"structured_search_input_header\",\"searchType\":\"autocomplete_click\",\"federatedSearchSessionId\":\"e0168175-d333-413f-b3b3-5d9bb36cd9cf\",\"itemsOffset\":" + f"{str(itemsPerGrid*page)}" +",\"sectionOffset\":3,\"query\":\"Toronto, ON\",\"cdnCacheSafe\":false,\"treatmentFlags\":[\"flex_destinations_june_2021_launch_web_treatment\",\"new_filter_bar_v2_fm_header\",\"merch_header_breakpoint_expansion_web\",\"flexible_dates_12_month_lead_time\",\"storefronts_nov23_2021_homepage_web_treatment\",\"web_remove_duplicated_params_fields\",\"flexible_dates_options_extend_one_three_seven_days\",\"super_date_flexibility\",\"micro_flex_improvements\",\"micro_flex_show_by_default\",\"search_input_placeholder_phrases\",\"pets_fee_treatment\"],\"screenSize\":\"large\",\"isInitialLoad\":true,\"hasLoggedIn\":true},\"removeDuplicatedParams\":true}","extensions":"{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"1cb8bde810f2d0469ed603796a970876815987bc4ff91f05bea3bf707e6f7aa2\"}}"}
    return query

querystring = query_listings(1)
url = f"https://www.airbnb.ca/api/v3/ExploreSections?{urlencode(querystring)}"