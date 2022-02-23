# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ListingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # indexing 
    index = scrapy.Field()
    timeStamp = scrapy.Field()
    listingId = scrapy.Field()

    # url
    url = scrapy.Field()

    # general info 
    title = scrapy.Field()
    propertyType = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    hood = scrapy.Field()
    descriptions = scrapy.Field()
    amenities = scrapy.Field()
    personCapacity = scrapy.Field()
    numberOfBedrooms = scrapy.Field()
    numberOfBeds = scrapy.Field()
    numberOfBathrooms = scrapy.Field()
    numPictures = scrapy.Field()

    # host info
    hostName = scrapy.Field()
    hostId = scrapy.Field()
    hostContactInfo = scrapy.Field()
    isSuperHost = scrapy.Field()
    hostNumReviews = scrapy.Field()
    policyNumber = scrapy.Field()
    languages = scrapy.Field()
    responseRate = scrapy.Field()
    responseTime = scrapy.Field()
    hostJoinDate = scrapy.Field()

    # occupancy
    occupancyTable = scrapy.Field()
    isAvailableTonight = scrapy.Field()
    futureOccupanyRate = scrapy.Field()

    # ratings
    accuracyRating = scrapy.Field()
    checkinRating = scrapy.Field()
    cleanlinessRating = scrapy.Field()
    communicationRating = scrapy.Field()
    locationRating = scrapy.Field()
    valueRating = scrapy.Field()
    guestSatisfactionOverall = scrapy.Field()
    visibleReviewCount = scrapy.Field()



