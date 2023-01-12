import kivy
kivy.require('2.0.0') 

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from weather import Weather
from currentTime import Time

Config.set("graphics", "height", "480")
Config.set("graphics", "width", "800")


class WeatherScreen(Screen):

    def __init__(self, **kwargs):
        super(WeatherScreen, self).__init__(**kwargs) #init parent
        weatherPage = FloatLayout()

        time = Time()
        # Add time to the screen
        weatherPage.add_widget(time.current_time)
        weatherPage.add_widget(time.current_date)
        Clock.schedule_interval(time.update_clock, 1)

        weather = Weather()
        # Schedule one new update at the next hour
        secondsUntilNextHour = time.seconds_until_next_hour()
        Clock.schedule_once(weather.update_weather, secondsUntilNextHour + 5)
        # Update the weather every 10mins
        Clock.schedule_interval(weather.update_weather, 600)

        # Add temp and icon for current weather
        weatherPage.add_widget(weather.currentTemperature)
        weatherPage.add_widget(weather.currentIcon)

        # Add temp and icon for weather in an hour
        weatherPage.add_widget(weather.secondTemperature)
        weatherPage.add_widget(weather.secondIcon)
        weatherPage.add_widget(weather.secondHour)

        # Add temp and icon for weather in 2 hours
        weatherPage.add_widget(weather.thirdTemperature)
        weatherPage.add_widget(weather.thirdIcon)
        weatherPage.add_widget(weather.thirdHour)

        # Add temp and icon for weather in 3 hours
        weatherPage.add_widget(weather.fourthTemperature)
        weatherPage.add_widget(weather.fourthIcon)
        weatherPage.add_widget(weather.fourthHour)

        # Add temp and icon for weather in 4 hours
        weatherPage.add_widget(weather.fifthTemperature)
        weatherPage.add_widget(weather.fifthIcon)
        weatherPage.add_widget(weather.fifthHour)

        if (weather.error == True):
          weatherPage.add_widget(
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

        self.add_widget(weatherPage)

    def callback(self, instance):
        print('The button has been pressed')
        self.manager.current = 'welcomeScreen'

    def on_touch_move(self, touch):
      if touch.x < touch.ox: # this line checks if a left swipe has been detected
        self.manager.current = 'welcomeScreen' # calls the method in the main app that changes the screen


# WeatherApp().run()

# if __name__ == '__main__':
#   WeatherApp().run()
