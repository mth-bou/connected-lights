import requests
from decouple import config


api_key_weithermap = config('API_KEY_WEITHERMAP')
api_key_ipstack = config('API_KEY_IPSTACK')


def getAllWeitherApi():
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=' + api_key_weithermap)
    if res.status_code == 200:
        print(res.json())


def getLocationWithIpStackApi():
    res = requests.get('https://api.ipify.org?format=json')
    json = res.json()
    ip = json['ip']

    res = requests.get('http://api.ipstack.com/' + ip + '?access_key=' + api_key_ipstack)
    localisation = res.json()
    ville = localisation['city']
    return ville


def getWeitherWithLocation():
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + getLocationWithIpStackApi() + '&appid=' + api_key_weithermap + '&units=metric')
    meteo = res.json()
    print(meteo)


