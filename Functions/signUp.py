import requests
import helper
import os

config=helper.read_config()

s=requests.Session()

def signUp(businessEmail,password):

    userSingUpdata = {
        "email": businessEmail,
        "password": password,
        "confirmPassword": password
    }

    if os.environ['env_variable'] == 'TEST':
        signupApi=config['TestApi']['signupapi']
    elif os.environ['env_variable'] == 'PRODUCTION':
        signupApi=config['ProductionApi']['signupapi']
    
    p = s.post(signupApi, json=userSingUpdata)
    signUpStatusCode = p.status_code
    
    return signUpStatusCode