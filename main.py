import os
import kivy
kivy.require('2.0.0') 

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivymd.uix.screen import Screen

from weather import Weather
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
      # Schedule one new update at the next hour
      secondsUntilNextHour = time.seconds_until_next_hour()
      Clock.schedule_once(weather.update_weather, secondsUntilNextHour)
      # Update the weather every 20mins
      Clock.schedule_interval(weather.update_weather, 1200)

      # Add temp and icon for current weather
      screen.add_widget(weather.widgets['currentTemperature'])
      screen.add_widget(weather.widgets['currentIcon'])

      # Add temp and icon for weather in an hour
      screen.add_widget(weather.widgets['secondTemperature'])
      screen.add_widget(weather.widgets['secondIcon'])
      screen.add_widget(weather.widgets['secondHour'])

      # Add temp and icon for weather in 2 hours
      screen.add_widget(weather.widgets['thirdTemperature'])
      screen.add_widget(weather.widgets['thirdIcon'])
      screen.add_widget(weather.widgets['thirdHour'])

      # Add temp and icon for weather in 3 hours
      screen.add_widget(weather.widgets['fourthTemperature'])
      screen.add_widget(weather.widgets['fourthIcon'])
      screen.add_widget(weather.widgets['fourthHour'])

      # Add temp and icon for weather in 4 hours
      screen.add_widget(weather.widgets['fifthTemperature'])
      screen.add_widget(weather.widgets['fifthIcon'])
      screen.add_widget(weather.widgets['fifthHour'])

      return screen

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
