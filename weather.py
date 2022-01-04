import os
import kivy
kivy.require('2.0.0') 
import requests

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock

from datetime import datetime as dt

class WeatherDataPerHour:
    def __init__(self, data):
      # should call convert_hour in here instead of in each label
      self.hour = dt.fromtimestamp(data["dt"]).hour
      self.icon = data["weather"][0]["icon"]
      self.temp = round(data["temp"])
      self.feelsLike = round(data["feels_like"])

def get_weather():
  weather = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=51.554780&lon=-0.040490&exclude=minutely,alerts,daily&units=metric&appid={os.environ['WEATHER_API_KEY']}").json()

  formattedWeatherNow = WeatherDataPerHour(weather["current"])
  nextHour = WeatherDataPerHour(weather["hourly"][1]);
  secondHour = WeatherDataPerHour(weather["hourly"][2])
  thirdHour = WeatherDataPerHour(weather["hourly"][3])
  fourthHour = WeatherDataPerHour(weather["hourly"][4])

  return [formattedWeatherNow, nextHour, secondHour, thirdHour, fourthHour]

def convert_hour(hour):
  if hour > 12:
    return f'{hour - 12} pm'

  if hour == 0:
    return '12 am'

  return f'{hour} am'

# data example:
# {'feelsLike': 4, 'hour': 22, 'icon': '10n', 'temp': 5}
class Weather(Label):
    def __init__(self, *args):
      self.data = get_weather()

      self.currentTemperature = Label(
        text = f'{str(self.data[0].temp)}°', 
        pos_hint={'center_x':0.17,'center_y':0.22},
        font_size= 22,
        bold= True,
      )
      self.currentIcon = Image(
        source=f'./icons/{self.data[0].icon}.png', 
        pos_hint={'center_x':0.17,'center_y':0.385},
        size_hint_x= 0.20,
        allow_stretch= True,
      )

      # in 1hr
      self.secondHour = Label(
        text = convert_hour(self.data[1].hour), 
        pos_hint={'center_x':0.4,'center_y':0.41},
        font_size= 15,
      )
      self.secondTemperature = Label(
        text = f'{str(self.data[1].temp)}°', 
        pos_hint={'center_x':0.4,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      self.secondIcon = Image(
        source=f'./icons/{self.data[1].icon}.png', 
        pos_hint={'center_x':0.4,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True,
      )

      # in 2hrs
      self.thirdHour = Label(
        text = convert_hour(self.data[2].hour), 
        pos_hint={'center_x':0.55,'center_y':0.41},
        font_size= 15,
      )
      self.thirdTemperature = Label(
        text = f'{str(self.data[2].temp)}°', 
        pos_hint={'center_x':0.55,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      self.thirdIcon = Image(
        source=f'./icons/{self.data[2].icon}.png', 
        pos_hint={'center_x':0.55,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True,
      )

      # in 3hrs
      self.fourthHour = Label(
        text = convert_hour(self.data[3].hour), 
        pos_hint={'center_x':0.7,'center_y':0.41},
        font_size= 15,
      )
      self.fourthTemperature = Label(
        text = f'{str(self.data[3].temp)}°', 
        pos_hint={'center_x':0.7,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      self.fourthIcon = Image(
        source=f'./icons/{self.data[3].icon}.png', 
        pos_hint={'center_x':0.7,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True,
      )

      # in 4hrs
      self.fifthHour = Label(
        text = convert_hour(self.data[4].hour), 
        pos_hint={'center_x':0.85,'center_y':0.41},
        font_size= 15,
      )
      self.fifthTemperature = Label(
        text = f'{str(self.data[4].temp)}°', 
        pos_hint={'center_x':0.85,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      self.fifthIcon = Image(
        source=f'./icons/{self.data[4].icon}.png', 
        pos_hint={'center_x':0.85,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True,
      )
      
    def update_weather(self, *args):
      print('Updating weather')
      self.data = get_weather()

      self.currentTemperature.text = f'{str(self.data[0].temp)}°'
      self.currentIcon.source = f'./icons/{self.data[0].icon}.png'

      self.secondTemperature.text = f'{str(self.data[1].temp)}°'
      self.secondIcon.source = f'./icons/{self.data[1].icon}.png'
      self.secondHour.text = convert_hour(self.data[1].hour)

      self.thirdTemperature.text = f'{str(self.data[2].temp)}°'
      self.thirdIcon.source = f'./icons/{self.data[2].icon}.png'
      self.thirdHour.text = convert_hour(self.data[2].hour)

      self.fourthTemperature.text = f'{str(self.data[3].temp)}°'
      self.fourthIcon.source = f'./icons/{self.data[3].icon}.png'
      self.fourthHour.text = convert_hour(self.data[3].hour)

      self.fifthTemperature.text = f'{str(self.data[4].temp)}°'
      self.fifthIcon.source = f'./icons/{self.data[4].icon}.png'
      self.fifthHour.text = convert_hour(self.data[4].hour)
