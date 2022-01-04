import os
import kivy
kivy.require('2.0.0') 

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivymd.uix.screen import Screen

from weather import Weather
from weather import generate_widgets
from currentTime import Time

Config.set("graphics", "height", "480")
Config.set("graphics", "width", "800")

class WeatherApp(App):

    def build(self):
      screen = Screen()

      time = Time()
      # Add time to the screen
      screen.add_widget(time.current_time)
      screen.add_widget(time.current_date)
      Clock.schedule_interval(time.update_clock, 1)

      weather = Weather()
      # Update the weather every 30mins
      Clock.schedule_interval(weather.update_weather, 1800)

      weatherWidgets = generate_widgets(weather.data)

      # Add temp and icon for current weather
      screen.add_widget(weatherWidgets['currentTemperature'])
      screen.add_widget(weatherWidgets['currentIcon'])

      # Add temp and icon for weather in an hour
      screen.add_widget(weatherWidgets['secondTemperature'])
      screen.add_widget(weatherWidgets['secondIcon'])
      screen.add_widget(weatherWidgets['secondHour'])

      # Add temp and icon for weather in 2 hours
      screen.add_widget(weatherWidgets['thirdTemperature'])
      screen.add_widget(weatherWidgets['thirdIcon'])
      screen.add_widget(weatherWidgets['thirdHour'])

      # Add temp and icon for weather in 3 hours
      screen.add_widget(weatherWidgets['fourthTemperature'])
      screen.add_widget(weatherWidgets['fourthIcon'])
      screen.add_widget(weatherWidgets['fourthHour'])

      # Add temp and icon for weather in 4 hours
      screen.add_widget(weatherWidgets['fifthTemperature'])
      screen.add_widget(weatherWidgets['fifthIcon'])
      screen.add_widget(weatherWidgets['fifthHour'])

      return screen

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
