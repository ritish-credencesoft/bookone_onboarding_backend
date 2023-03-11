import requests
import os
import helper

config=helper.read_config()

s=requests.Session()

def addSubscription(propertyId,userId,header):

    suscriptionData = {
        "annualAmount": 0,
        "currency": "INR",
        "description": "",
        "discountAmount": 0,
        "id": userId,
        "imageUrl": "string",
        "monthlyAmount": 0,
        "name": "string",
        "organisationId": 1,
        "propertyId": propertyId,
        "specialNotes": "string",
        "subscriptionType": "MONTHLY"
    }

    if os.environ['env_variable'] == 'TEST':
        addSubscriptionApi=config['TestApi']['addsubscriptionapi'].replace('{propertyId}',str(propertyId))
    elif os.environ['env_variable'] == 'PRODUCTION':
        addSubscriptionApi=config['ProductionApi']['addsubscriptionapi'].replace('{propertyId}',str(propertyId))

    addSubscriptionApiRes = s.post( 
        addSubscriptionApi, headers=header, json=suscriptionData)
    subscriptionStatusCode = addSubscriptionApiRes.status_code

    if subscriptionStatusCode == 200:
        print('Subscription add api status code',subscriptionStatusCode)
    
    return subscriptionStatusCode
