import kivy
kivy.require('2.0.0') 

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.uix.ScreenManager import ScreenManager
from kivy.uix.label import Label

from weather import Weather
from currentTime import Time

Config.set("graphics", "height", "480")
Config.set("graphics", "width", "800")


class WeatherApp(App):

    def build(self):
      sm = ScreenManager()


      screen = Screen(name="Main")
      sm.add_widget(screen)

      secondScreen = Screen(name="secondary")
      sm.add_widget(secondScreen)

      time = Time()
      # Add time to the screen
      screen.add_widget(time.current_time)
      screen.add_widget(time.current_date)
      Clock.schedule_interval(time.update_clock, 1)

      weather = Weather()
      # Schedule one new update at the next hour
      secondsUntilNextHour = time.seconds_until_next_hour()
      Clock.schedule_once(weather.update_weather, secondsUntilNextHour + 5)
      # Update the weather every 10mins
      Clock.schedule_interval(weather.update_weather, 600)

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

      if (weather.error == True):
        screen.add_widget(
          Label(
            text = "Weather Error", 
            text_size= (500, 200),
            halign="left",
            pos_hint= {'x': .27, 'y': .99},
            size_hint= (None, None),
            font_size= 30,
            color= (1, 0, 0)
          )
        )

      sm.current = 'Main'
      return screen

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
