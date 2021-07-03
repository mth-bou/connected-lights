import requests
from decouple import config

# set API_KEY_WEATHERMAP in .env file
api_key_weathermap = config('API_KEY_WEATHERMAP')
# set API_KEY_IPSTACK in .env file
api_key_ipstack = config('API_KEY_IPSTACK')


def getAllWeatherApi():
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=' + api_key_weathermap)
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


def getPrevisionalWeatherWithLocation():
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=' + getLocationWithIpStackApi() + '&appid=' + api_key_weathermap + '&units=metric')
    meteo = res.json()
    return meteo


def getCurrentWeatherWithLocation():
    res = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + getLocationWithIpStackApi() + '&appid=' + api_key_weathermap + '&units=metric')
    meteo = res.json()
    return meteo