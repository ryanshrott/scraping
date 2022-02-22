import base64
coded_string = 'StayListing:50420121'

message_bytes = coded_string.encode('ascii')
encoded = base64.b64encode(message_bytes).decode('utf-8')

print(encoded)

out = '"{\"id\":\"U3RheUxpc3Rpbmc6NTA0MjAxMjE=\"'
out2 = '"{\"id\":' + f'"{str(encoded)}\"'

print(out)
print(out2)
 
querystring = '"{\"id\":' + f'"{str(encoded)}\"' + ",\"pdpSectionsRequest"


good = "{\"id\":\"U3RheUxpc3Rpbmc6NTA0MjAxMjE=\",\"pdpSectionsRequest\":{\"adults\":\"1\",\"bypassTargetings\":false,\"categoryTag\":null,\"causeId\":null,\"children\":null,\"disasterId\":null,\"discountedGuestFeeVersion\":null,\"displayExtensions\":null,\"federatedSearchId\":\"940e74ab-c1fe-492e-a5f4-87f8e205aad8\",\"forceBoostPriorityMessageType\":null,\"infants\":null,\"interactionType\":null,\"layouts\":[\"SIDEBAR\",\"SINGLE_COLUMN\"],\"pets\":0,\"pdpTypeOverride\":null,\"preview\":false,\"previousStateCheckIn\":null,\"previousStateCheckOut\":null,\"priceDropSource\":null,\"privateBooking\":false,\"promotionUuid\":null,\"relaxedAmenityIds\":null,\"searchId\":null,\"selectedCancellationPolicyId\":null,\"selectedRatePlanId\":null,\"staysBookingMigrationEnabled\":false,\"translateUgc\":null,\"useNewSectionWrapperApi\":false,\"sectionIds\":null,\"checkIn\":\"2022-03-08\",\"checkOut\":\"2022-03-09\"}}"

print(good)
print('------------------------')
print(querystring)