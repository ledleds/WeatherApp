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

def generate_widgets(data):
  currentTemperature = Label(
    text = f'{str(data[0].temp)}°', 
    pos_hint={'center_x':0.17,'center_y':0.22},
    font_size= 22,
    bold= True,
  )
  currentIcon = Image(
    source=f'./icons/{data[0].icon}.png', 
    pos_hint={'center_x':0.17,'center_y':0.385},
    size_hint_x= 0.24,
    allow_stretch= True,
  )

  # in 1hr
  secondHour = Label(
    text = convert_hour(data[1].hour), 
    pos_hint={'center_x':0.4,'center_y':0.41},
    font_size= 15,
  )
  secondTemperature = Label(
    text = f'{str(data[1].temp)}°', 
    pos_hint={'center_x':0.4,'center_y':0.22},
    font_size= 19,
    bold= True,
  )
  secondIcon = Image(
    source=f'./icons/{data[1].icon}.png', 
    pos_hint={'center_x':0.4,'center_y':0.31},
    size_hint_x= 0.09,
    allow_stretch= True,
  )

  # in 2hrs
  thirdHour = Label(
    text = convert_hour(data[2].hour), 
    pos_hint={'center_x':0.55,'center_y':0.41},
    font_size= 15,
  )
  thirdTemperature = Label(
    text = f'{str(data[2].temp)}°', 
    pos_hint={'center_x':0.55,'center_y':0.22},
    font_size= 19,
    bold= True,
  )
  thirdIcon = Image(
    source=f'./icons/{data[2].icon}.png', 
    pos_hint={'center_x':0.55,'center_y':0.31},
    size_hint_x= 0.09,
    allow_stretch= True,
  )

  # in 3hrs
  fourthHour = Label(
    text = convert_hour(data[3].hour), 
    pos_hint={'center_x':0.7,'center_y':0.41},
    font_size= 15,
  )
  fourthTemperature = Label(
    text = f'{str(data[3].temp)}°', 
    pos_hint={'center_x':0.7,'center_y':0.22},
    font_size= 19,
    bold= True,
  )
  fourthIcon = Image(
    source=f'./icons/{data[3].icon}.png', 
    pos_hint={'center_x':0.7,'center_y':0.31},
    size_hint_x= 0.09,
    allow_stretch= True,
  )

  # in 4hrs
  fifthHour = Label(
    text = convert_hour(data[4].hour), 
    pos_hint={'center_x':0.85,'center_y':0.41},
    font_size= 15,
  )
  fifthTemperature = Label(
    text = f'{str(data[4].temp)}°', 
    pos_hint={'center_x':0.85,'center_y':0.22},
    font_size= 19,
    bold= True,
  )
  fifthIcon = Image(
    source=f'./icons/{data[4].icon}.png', 
    pos_hint={'center_x':0.85,'center_y':0.31},
    size_hint_x= 0.09,
    allow_stretch= True,
  )

  return { 
    'currentTemperature': currentTemperature,
    'currentIcon': currentIcon,
    'secondTemperature': secondTemperature,
    'secondIcon': secondIcon,
    'secondHour': secondHour,
    'thirdTemperature': thirdTemperature,
    'thirdIcon': thirdIcon,
    'thirdHour': thirdHour,
    'fourthTemperature': fourthTemperature,
    'fourthIcon': fourthIcon,
    'fourthHour': fourthHour,
    'fifthTemperature': fifthTemperature,
    'fifthIcon': fifthIcon,
    'fifthHour': fifthHour,
}

# data example:
# {'feelsLike': 4, 'hour': 22, 'icon': '10n', 'temp': 5}
class Weather(Label):
    def __init__(self, *args):
      self.data = get_weather()
      self.widgets = generate_widgets(self.data)
      
    def update_weather(self, *args):
      self.data = get_weather()
      self.widgets = generate_widgets(self.data)

    def start(self):
      print('called start')
      self.update_weather()
      Clock.schedule_interval(self.update_weather, 1)
