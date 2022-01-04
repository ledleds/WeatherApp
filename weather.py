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
      
    def update_weather(self, *args):
      self.data = get_weather()

    def start(self):
      print('called start')
      self.update_weather()
      Clock.schedule_interval(self.update_weather, 1)
