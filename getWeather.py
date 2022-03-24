"""
    getWeather class
    usage: getWeather(place) -> returns tuple of current weather in named place 
        return string place + temp + conditions
"""

import requests, json

class Weather():
    def __init__(self, apikey):
        self.weatherService = "http://api.openweathermap.org/data/2.5/weather?"
        self.weatherApiKey = apikey
        self.result = ""

    def getWeather(self, place):
        url = self.weatherService + "appid=" + self.weatherApiKey + "&q=" + place + "&units=metric" + "&lang=ru"
        responceJson = requests.get(url)
        responce = responceJson.json()

        if responce["cod"] != "404":
            data = responce["main"]
            temp = str(data["temp"])
            weather = responce["weather"]
            weatherMain = weather[0]["main"]
            
            if weatherMain == "Rain" or weatherMain == "Drizzle":
                weatherEmoji = "🌧 "
            elif weatherMain == "Clear":
                weatherEmoji = "☀ "
            elif weatherMain == "Clouds":
                weatherEmoji = "☁ "
            elif weatherMain == "Thunderstorm":
                weatherEmoji = "⛈ "
            elif weatherMain == "Snow":
                weatherEmoji = "❄ "
            elif weatherMain == "Fog" or weatherMain == "Haze" or weatherMain == "Mist":
                weatherEmoji = "🌫 "
            else:
                weatherEmoji = "⛅ "

            self.result: str = "🏠 " + place + ": 🌡" + temp + "C, " + weatherEmoji + weather[0]["description"]
        else:
            self.result = "Город не найден"

        return self.result