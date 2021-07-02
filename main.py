from api import getAllWeatherApi, getWeatherWithLocation
from utils import hotOrcold


def getTemp(date):
    data = getWeatherWithLocation()
    list = data['list']
    for elem in list:
        if date:
            temp_min = elem['main']['temp_min']
            temp_max = elem['main']['temp_max']
            temp = (temp_max + temp_min) / 2

    return temp


# Tranches horaires de 3h donc 8ème élément du tableau = 24h
def getPrevisionalWeatherDate():
    data = getWeatherWithLocation()
    list = data['list']
    days = []
    for elem in list:
        day = elem['dt_txt']
        days.append(day)

    return days[8]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day = getPrevisionalWeatherDate()
    temp = getTemp(day)
    hotOrcold(temp)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
