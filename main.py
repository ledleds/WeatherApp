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
      # Update the weather every 30mins
      Clock.schedule_interval(weather.update_weather, 1800)

      # ///////////////////////////////
      # TEMPORARY, move these somewhere better!
      currentTemperature = Label(
        text = f'{str(weather.data[0].temp)}°', 
        pos_hint={'center_x':0.17,'center_y':0.22},
        font_size= 22,
        bold= True,
      )
      currentIcon = Image(
        source=f'./icons/{weather.data[0].icon}.png', 
        pos_hint={'center_x':0.17,'center_y':0.385},
        size_hint_x= 0.24,
        allow_stretch= True
      )

      # in 1hr
      secondHour = Label(
        text = convert_hour(weather.data[1].hour), 
        pos_hint={'center_x':0.4,'center_y':0.41},
        font_size= 15,
      )
      secondTemperature = Label(
        text = f'{str(weather.data[1].temp)}°', 
        pos_hint={'center_x':0.4,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      secondIcon = Image(
        source=f'./icons/{weather.data[1].icon}.png', 
        pos_hint={'center_x':0.4,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 2hrs
      thirdHour = Label(
        text = convert_hour(weather.data[2].hour), 
        pos_hint={'center_x':0.55,'center_y':0.41},
        font_size= 15,
      )
      thirdTemperature = Label(
        text = f'{str(weather.data[2].temp)}°', 
        pos_hint={'center_x':0.55,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      thirdIcon = Image(
        source=f'./icons/{weather.data[2].icon}.png', 
        pos_hint={'center_x':0.55,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 3hrs
      fourthHour = Label(
        text = convert_hour(weather.data[3].hour), 
        pos_hint={'center_x':0.7,'center_y':0.41},
        font_size= 15,
      )
      fourthTemperature = Label(
        text = f'{str(weather.data[3].temp)}°', 
        pos_hint={'center_x':0.7,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      fourthIcon = Image(
        source=f'./icons/{weather.data[3].icon}.png', 
        pos_hint={'center_x':0.7,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True
      )

      # in 4hrs
      fifthHour = Label(
        text = convert_hour(weather.data[4].hour), 
        pos_hint={'center_x':0.85,'center_y':0.41},
        font_size= 15,
      )
      fifthTemperature = Label(
        text = f'{str(weather.data[4].temp)}°', 
        pos_hint={'center_x':0.85,'center_y':0.22},
        font_size= 19,
        bold= True,
      )
      fifthIcon = Image(
        source=f'./icons/{weather.data[4].icon}.png', 
        pos_hint={'center_x':0.85,'center_y':0.31},
        size_hint_x= 0.09,
        allow_stretch= True
      )
      # ///////////////////////////////

      # Add temp and icon for current weather
      screen.add_widget(currentTemperature)
      screen.add_widget(currentIcon)

      # Add temp and icon for weather in an hour
      screen.add_widget(secondTemperature)
      screen.add_widget(secondIcon)
      screen.add_widget(secondHour)

      # Add temp and icon for weather in 2 hours
      screen.add_widget(thirdTemperature)
      screen.add_widget(thirdIcon)
      screen.add_widget(thirdHour)

      # Add temp and icon for weather in 3 hours
      screen.add_widget(fourthTemperature)
      screen.add_widget(fourthIcon)
      screen.add_widget(fourthHour)

      # Add temp and icon for weather in 4 hours
      screen.add_widget(fifthTemperature)
      screen.add_widget(fifthIcon)
      screen.add_widget(fifthHour)

      return screen

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
