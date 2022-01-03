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
      self.hour = dt.fromtimestamp(data["dt"]).hour
      self.icon = data["weather"][0]["icon"]
      self.temp = round(data["temp"])
      self.feelsLike = round(data["feels_like"])

def get_weather():
  print('Getting weather!')

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
      # now
      self.currentTemperature = Label(
        text = f'{str(self.data[0].temp)}°', 
        pos_hint={'center_x':0.15,'center_y':0.42},
        font_size= 19,
        bold= True,
      )
      self.currentIcon = Image(
        source=f'./icons/{self.data[0].icon}.png', 
        pos_hint={'center_x':0.15,'center_y':0.56},
        size_hint_x= 0.17,
        allow_stretch= True
      )
      self.currentHour = Label(
        text = 'Now', 
        pos_hint={'center_x':0.1,'center_y':0.57}
      )

      # in 1hr
      self.secondHour = Label(
        text = convert_hour(self.data[1].hour), 
        pos_hint={'center_x':0.35,'center_y':0.61},
        font_size= 15,
      )
      self.secondTemperature = Label(
        text = f'{str(self.data[1].temp)}°', 
        pos_hint={'center_x':0.35,'center_y':0.42},
        font_size= 19,
        bold= True,
      )
      self.secondIcon = Image(
        source=f'./icons/{self.data[1].icon}.png', 
        pos_hint={'center_x':0.35,'center_y':0.51},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 2hrs
      self.thirdHour = Label(
        text = convert_hour(self.data[2].hour), 
        pos_hint={'center_x':0.5,'center_y':0.61},
        font_size= 15,
      )
      self.thirdTemperature = Label(
        text = f'{str(self.data[2].temp)}°', 
        pos_hint={'center_x':0.5,'center_y':0.42},
        font_size= 19,
        bold= True,
      )
      self.thirdIcon = Image(
        source=f'./icons/{self.data[2].icon}.png', 
        pos_hint={'center_x':0.5,'center_y':0.51},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 3hrs
      self.fourthHour = Label(
        text = convert_hour(self.data[3].hour), 
        pos_hint={'center_x':0.65,'center_y':0.61},
        font_size= 15,
      )
      self.fourthTemperature = Label(
        text = f'{str(self.data[3].temp)}°', 
        pos_hint={'center_x':0.65,'center_y':0.42},
        font_size= 19,
        bold= True,
      )
      self.fourthIcon = Image(
        source=f'./icons/{self.data[3].icon}.png', 
        pos_hint={'center_x':0.65,'center_y':0.51},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 4hrs
      self.fifthHour = Label(
        text = convert_hour(self.data[4].hour), 
        pos_hint={'center_x':0.8,'center_y':0.61},
        font_size= 15,
      )
      self.fifthTemperature = Label(
        text = f'{str(self.data[4].temp)}°', 
        pos_hint={'center_x':0.8,'center_y':0.42},
        font_size= 19,
        bold= True,
      )
      self.fifthIcon = Image(
        source=f'./icons/{self.data[4].icon}.png', 
        pos_hint={'center_x':0.8,'center_y':0.51},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      
    def update_weather(self, *args):
      print('OMG Updating weather')
      self.data = get_weather()

    def start(self):
      print('called start')
      self.update_weather()
      Clock.schedule_interval(self.update_weather, 1)
