import requests

apiKey = "a3ca8c897af429d70420956cab71c08f"
res = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format("toronto", apiKey))
if res.status_code == 200:
    data = res.json()
    weather_icon = "http://openweathermap.org/img/wn/{}@2x.png".format(
        data["weather"][0]["icon"])
    weather_des = data["weather"][0]["description"]
    temp = str(round(data["main"]["temp"] - 273.15)) + "°C"
    feels_temp = str(round(data["main"]["feels_like"] - 273.15)) + "°C"
    humidity = str(data["main"]["humidity"]) + "%"
    pressure = str(data["main"]["pressure"]) + " hPa"
    city = data["name"]
    country = data["sys"]["country"]
    time = data["dt"]
    message = {
        "channel": "ok",
        "attachments": [
            {
                "color": "#",
                "title": "Weather in {}, {}:".format(city, country),
                "fields": [
                    {
                        "title": "Temperature:",
                        "value": "It is {} and feels like {}.".format(temp, feels_temp),
                        "short": True
                    },
                    {
                        "title": "Description:",
                        "value": weather_des,
                        "short": True
                    },
                    {
                        "title": "Humidity:",
                        "value": humidity,
                        "short": True
                    },
                    {
                        "title": "Atmospheric Pressure:",
                        "value": pressure,
                        "short": True
                    }
                ],
                "thumb_url": weather_icon,
                "footer": "OpenWeather.org",
                "footer_icon": "https://openweathermap.org/themes/openweathermap/assets/vendor/owm/img/icons/logo_32x32.png",
                "ts": time,
            }
        ]
    }
    print(message)
