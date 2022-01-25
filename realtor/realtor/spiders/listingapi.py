import requests

s = requests.Session()
home_url = 'https://www.realtor.ca/map#ZoomLevel=13&Center=43.686631%2C-79.339824&LatitudeMax=43.75741&LongitudeMax=-79.25894&LatitudeMin=43.61577&LongitudeMin=-79.42071&view=list&Sort=6-D&PGeoIds=g20_dpz8de7m&GeoName=East%20York%2C%20Toronto%2C%20ON&PropertyTypeGroupID=1&PropertySearchTypeId=1&TransactionTypeId=2&Currency=CAD'
step = s.get(home_url)
print(step)

url = 'https://api2.realtor.ca/Listing.svc/PropertySearch_Post'

headers = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
    'origin':'https://www.realtor.ca',
    'referer':'https://www.realtor.ca/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

output = []
for page in range(1,5):

    payload = {
        'ZoomLevel':'13',
        'LatitudeMax':'43.75741',
        'LongitudeMax':'-79.25894',
        'LatitudeMin':'43.61577',
        'LongitudeMin':'-79.42071',
        'Sort':'6-D',
        'PropertyTypeGroupID':'1',
        'PropertySearchTypeId':'1',
        'TransactionTypeId':'2',
        'Currency':'CAD',
        'RecordsPerPage':'100',
        'ApplicationId':'1',
        'CultureId':'1',
        'Version':'7.0',
        'CurrentPage': str(page)
        }

    post = s.post(url,headers=headers,data=payload).json()
    results = len(post['Results'])
    print(f'Scraping page: {page}, results: {results}')

    for i, listing in enumerate(post['Results']):
        print(0, listing['Id'],listing['Property']['Price'])