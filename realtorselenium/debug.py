from realtorselenium.spiders import listing
spider = listing.ListingSpider()

spider.start_requests()

spider.parse()