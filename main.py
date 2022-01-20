import kivy
kivy.require('2.0.0') 

from kivy.app import App
from kivy.config import Config
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.button import Button
# from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

from weather import Weather
from currentTime import Time

Config.set("graphics", "height", "480")
Config.set("graphics", "width", "800")

# Move into kv file!
Builder.load_string("""
<SecondWindow>:
    BoxLayout:
        Button:
            text: 'Back to main'
            on_press: root.manager.current = 'mainScreen'
""")

class MainWindow(Screen):
    def build(self, sm):
      screen = Screen()

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

      # https://stackoverflow.com/questions/19491286/kivy-changing-screens-in-screen-manager-with-an-on-press-event
      # myButton = Button(text="Go to screen 2")
      # myButton.bind(on_press = self.changer
      # screen.add_widget(myButton)

      screen.add_widget(ScreenButton(toScreen = 'secondScreen', screenmanager=sm))

      return screen

# This doesn't work!
# class ScreenButton(Button):
#     def __init__(self, toScreen):
#       self.to_screen = toScreen
#       self.screenmanager = ObjectProperty()
      
#     def on_press(self, *args):
#         print('on_press was called with:', *args)
#         super(ScreenButton, self).on_press(*args)
#         self.screenmanager.current = self.to_screen

class ScreenButton(Button):
    def __init__(self, toScreen, screenmanager):
      super().__init__()
      self.toScreen = toScreen

    screenmanager = ObjectProperty()
    def on_press(self, *args):
        print('on_press was called')
        super(ScreenButton, self).on_press(*args)
        self.screenmanager.current = self.toScreen

class SecondWindow(Screen):
    pass

class WeatherApp(App):
    def build(self):
      screenManager = ScreenManager()

      screenManager.add_widget(MainWindow(name='mainScreen').build(screenManager))
      screenManager.add_widget(SecondWindow(name='secondScreen'))
      # screen = Screen(name='Main')
      # screenManager.current = 'Main'

      return screenManager

WeatherApp().run()

if __name__ == '__main__':
  WeatherApp().run()
