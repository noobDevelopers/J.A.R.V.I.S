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

    city_name="Bangalore"
    api_key = "yourapikey"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    x = response.json()
    speak('Todays weather')
    weather_details={}
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]  
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        #weather_details.append(city_name)
        weather_details["Temperature"]=int(int(current_temperature)-273.15)
        weather_details["Pressure"]=current_pressure
        weather_details["Humidity"]=current_humidiy
        weather_details["Summary"] = weather_description
        
        for key,value in weather_details.items():
            speak(key)
            speak(value)
        speak('These were the top headlines, Have a nice day Sir!!..')
    else:
        speak('Unable to fetch todays weather')
    
if __name__ == '__main__':
    speak_news()