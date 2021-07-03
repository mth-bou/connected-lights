import json
from decouple import config
import requests


def hotOrcold(temp):
    global hueColor

    hueColorChaud = [[10331, 199, 209], [2595, 199, 205], [13737, 198, 45]]
    hueColorDoux = [[2210, 152, 167], [4260, 152, 131], [11871, 152, 65]]
    hueColorFrais = [[20884, 241, 63], [34967, 241, 54], [37508, 241, 54]]
    hueColorFroid = [[42643, 203, 184], [42681, 203, 114], [44297, 203, 15]]

    if temp >= 25:
        print("Il fait chaud : ", temp)
        hueColor = hueColorChaud
    elif temp < 25 and temp > 17:
        print("Il fait doux : ", temp)
        hueColor = hueColorDoux
    elif temp <= 17 and temp > 10:
        print("Il fait frais : ", temp)
        hueColor = hueColorFrais
    elif temp <= 10:
        print("Il fait froid : ", temp)
        hueColor = hueColorFroid

    #setHueColors(hueColor)


def setHueColors(hueColor):
    # Set bridge_ip of Hue router in the .env file
    bridge_ip = config('BRIDGE_IP')
    # Set username ID in the .env file
    username = config('USERNAME_HUE')

    lights_url = "http://{}/api/{}/lights".format(bridge_ip, username)

    # print(lights_url)
    # print(light_state_url)

    r = requests.get(lights_url)
    i = 0
    for light in r.json():
        light_current_status = "{} - {} : {}".format(light,
                                                     r.json()[light]["name"].encode("utf-8"),
                                                     r.json()[light]["state"]["on"])

        print(light_current_status)
        light_number = light
        light_state_url = "{}/{}/state".format(lights_url, light_number)

        message = json.dumps({
            "on": True,
            "bri": hueColor[i][1],
            "hue": hueColor[i][0],
            "sat": hueColor[i][2]
        })
        action = requests.put(light_state_url, data=message)
        print(action.content)

        i += 1
