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
      Clock.schedule_interval(weather.update_weather, 10)

      # Add temp and icon for current weather
      screen.add_widget(weather.currentTemperature)
      screen.add_widget(weather.currentIcon)

      # Add temp and icon for weather in an hour
      screen.add_widget(weather.secondTemperature)
      screen.add_widget(weather.secondIcon)
      screen.add_widget(weather.secondHour)

      # Add temp and icon for weather in 2 hours
      screen.add_widget(weather.thirdTemperature)
      screen.add_widget(weather.thirdIcon)
      screen.add_widget(weather.thirdHour)

      # Add temp and icon for weather in 3 hours
      screen.add_widget(weather.fourthTemperature)
      screen.add_widget(weather.fourthIcon)
      screen.add_widget(weather.fourthHour)

      # Add temp and icon for weather in 4 hours
      screen.add_widget(weather.fifthTemperature)
      screen.add_widget(weather.fifthIcon)
      screen.add_widget(weather.fifthHour)

      return screen

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
