import requests
import json
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def weathernews():
    loc_url = "http://api.ipstack.com/check?access_key="
    geo_req = requests.get(loc_url)
    geo_json = json.loads(geo_req.text)
    api_key = ""
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = geo_json['city']
    complete_url = url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    weather_details = {}
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        # weather_details.append(city_name)
        weather_details["Temperature"] = str(int(current_temperature)-273.15)
        weather_details["Pressure"] = current_pressure
        weather_details["Humidity"] = current_humidiy
        weather_details["Summary"] = weather_description

        for key, value in weather_details.items():
            speak(key)
            speak(value)
        speak('That is all for todays weather, have a good day!')
    else:
        speak('Unable to fetch todays weather')


if __name__ == '__main__':
    weathernews()
