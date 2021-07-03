from api import getAllWeatherApi, getCurrentWeatherWithLocation, getPrevisionalWeatherWithLocation
from utils import hotOrcold
from threading import Timer


def getPrevisionalTemp(date):
    data = getPrevisionalWeatherWithLocation()
    list = data['list']
    for elem in list:
        if date:
            temp_min = elem['main']['temp_min']
            temp_max = elem['main']['temp_max']
            temp = (temp_max + temp_min) / 2

    return temp


# Tranches horaires de 3h donc 8ème élément du tableau = 24h
def getPrevisionalWeatherDate():
    data = getPrevisionalWeatherWithLocation()
    list = data['list']
    days = []
    for elem in list:
        day = elem['dt_txt']
        days.append(day)

    return days[8]


def getCurrentTemp():
    data = getCurrentWeatherWithLocation()
    temp = data['main']['temp']
    return temp


# Function called every 15min to reload right colors with the new temperature
def update():
    set_timer()
    temp = getCurrentTemp()
    hotOrcold(temp)


def set_timer():
    t = Timer(5, update).start()


if __name__ == '__main__':
    # day = getPrevisionalWeatherDate()
    # temp = getPrevisionalTemp(day)

    # First occurence before timer's occurences
    temp = getCurrentTemp()
    hotOrcold(temp)
    set_timer()
