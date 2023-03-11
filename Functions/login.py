import json
import requests
import helper
import os

config=helper.read_config()

s=requests.Session()

def login(email, password):

    loginPayload = {
        'username': email,
        'password': password
    }

    if os.environ['env_variable'] == 'TEST':
        loginApi=config['TestApi']['loginapi']
    elif os.environ['env_variable'] == 'PRODUCTION':
        loginApi=config['ProductionApi']['loginapi']

    res = s.post(
        loginApi, json=loginPayload)
    s.headers.update({'authorization': json.loads(res.content)['token']})

    token = res.content
    tokenData = json.loads(token)
    loginData = {
        'token': tokenData['token'],
        'userId': tokenData['userId'],
        'status-code': res.status_code
    }
    if res.status_code == 200:
        print('Login api status code ', res.status_code)


    return loginData