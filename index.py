import time
import json
import os
from Functions.signUp import signUp
from Functions.login import login
from Functions.updateUser import updateUser
from Functions.addProperty import addProperty
from Functions.addSubscription import addSubscription
from Functions.addRoom import addRoom
from Functions.roomInfo import roomInformation
from Functions.roomPlan import addRoomPlan
from Functions.availabilityAndUpdatePlan import addAvailabilityAndUpdatePlan
from Functions.yearlyGenerate import yearlyGenerateApi
from Functions.pointOfSale import pointOfSaleApi
from Functions.businessService import businessServiceApi


os.environ['env_variable'] = 'TEST'
# os.environ['env_variable']='PRODUCTION'


class DriverClass:

    def __init__(self) -> None:
        pass

    def driverFucntion(self):

        print('ONBOARDING STARTS FOR PROPERTY -- >', businessEmail)
        print()

        # 1-SIGN UP API
        signUpStatusCode = signUp(businessEmail, password)
        time.sleep(2)

        if signUpStatusCode == 200 or signUpStatusCode == 226:
            print('SignUp api status code ', signUpStatusCode)

            data = login(businessEmail, password)

            userId = data['userId']
            t = data['token']
            apiToken = f'Bearer {t}'
            loginStatusCode = data['status-code']

        time.sleep(2)

        if loginStatusCode == 200:
            # 2-UPDATE USER API
            updateUserApiStatusCode = updateUser(userId, businessType, businessEmail, password,
                                                 businessName, mobileNumber, city, suburb, streetName, country, state, postcode)

        time.sleep(1)

        header = {
            'USER_ID': str(userId),
            'Authorization': apiToken,
            'APP_ID': 'BOOKONE_WEB_APP'
        }

        if updateUserApiStatusCode == 200:
            # ADD PROPERTY API
            addPropertyApi = addProperty(header, userId, businessName, businessShortName, businessEmail, mobileNumber, managerContactNumber, seoName, country,
                                         postcode, streetName, suburb, city, state, googlePlaceId, longitude, latitude, businessType)
            propertyId = addPropertyApi['propertyId']
            print(propertyId)
            addPropertyStatusCode = addPropertyApi['status']

        time.sleep(1)

        if addPropertyStatusCode == 200:
            # ADD SUBSCRIPTION API
            subscriptionStatusCode = addSubscription(
                propertyId, userId, header)

        time.sleep(1)

        if subscriptionStatusCode == 200:
            # ADD ROOM API
            addRoomApiStatusCode = addRoom(propertyId, header, roomType)

        time.sleep(1)

        if addRoomApiStatusCode == 201:
            allRoomIdList = roomInformation(propertyId, header)

            # ADD ROOM PLAN API
            time.sleep(1)
            addPlan = addRoomPlan(allRoomIdList, propertyId, header, roomPlan)

        if addPlan == 201:
            # AVAILABILITY AND UPDATE PLAN
            availbilityAndUpdatePlanApi = addAvailabilityAndUpdatePlan(
                allRoomIdList, propertyId, header, roomPlan)

            availabilityStatusCode = availbilityAndUpdatePlanApi['availabilityByDateRangeStatusCode']
            addOrUpdatePlanStatusCode = availbilityAndUpdatePlanApi['addOrUpdatePlanStatusCode']

        time.sleep(2)

        if availabilityStatusCode == 200 and addOrUpdatePlanStatusCode == 200:
            # GENERATE YEARLY RATES
            yearlyGenerateStatusCode = yearlyGenerateApi(propertyId, header, businessShortName, businessEmail, mobileNumber,
                                                         country, postcode, streetName, suburb, city, state, googlePlaceId, longitude, latitude, businessType)

        time.sleep(2)

        if yearlyGenerateStatusCode == 200:
            # POINT OF SALE
            posStatusCode = pointOfSaleApi(propertyId, header)

        time.sleep(1)

        if posStatusCode == 200:
            # ADD BUSINESS SERVICE
            addBusinessServiceStatusCode = businessServiceApi(
                propertyId, header)
            time.sleep(1)
            if addBusinessServiceStatusCode == 200:
                print('Property onboard successful')

        print('-----------------------------------------------------')

f = open(r'Data/test2.json')
jsonData = json.load(f)

for x in jsonData:
    # JSON READ
    businessName = x['BusinessName']
    businessShortName = ''
    password = 'Pass@1234'
    businessShortNameSplit = businessName.split()
    for i in businessShortNameSplit:
        businessShortName = businessShortName+i[0].upper()

    seoFriendlyName = businessName.split()
    seoName = '-'.join(seoFriendlyName).replace(',','')

    try:
        businessUrl = x['BusinessUrl']
    except:
        businessUrl = ''
    city = x['city']
    country = x['country']
    postcode = x['postcode']
    state = x['state']
    streetName = x['streetName']
    suburb = x['subUrb']
    businessType = x['BusinessType']
    collectedBy = x['dataCollectedBy']
    businessEmail = x['email']
    managerContactNumber = x['managerContactNo'].strip()
    mobileNumber = x['mobile'].strip()
    try:
        businessSource = x['source']
    except:
        businessSource = ''
    try:
        businessStatus = x['status']
    except:
        businessStatus = ''
    try:
        roomType = x['Room Type']
    except:
        roomType = ''
    try:
        roomPlan = x['Room Plan']
    except:
        roomPlan = ''
    try:
        longitude = x['Longitude']
    except:
        longitude = ''
    try:
        latitude = x['Latitude']
    except:
        latitude = ''
    try:
        googlePlaceId = x['Google place id']
    except:
        googlePlaceId = ''
    try:
        website = x['website']
    except:
        website = ''
    status = x['status']
    source = x['source']
    try:
        images = x['images']
    except:
        images = []

    obj = DriverClass()
    obj.driverFucntion()

    time.sleep(3)
