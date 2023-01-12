import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from weatherScreen import WeatherScreen


class PanelBuilderApp(App):  # display the welcome screen
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcomeScreen'))
        sm.add_widget(WeatherScreen(name='weatherScreen'))
        return sm

class WelcomeScreen(Screen): 
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs) #init parent
        functionPage = FloatLayout()
        functionLabel = Label(text='Welcome to this app. Here you will choose what functions to use',
                              halign='center', valign='center', size_hint=(0.4,0.2), pos_hint={'top': 1, 'center_x': 0.5})
        functionPage.add_widget(functionLabel)
        weatherButton = Button(text= 'Click to see weather', on_press=self.callback)
        functionPage.add_widget(weatherButton)
        self.add_widget(functionPage)

    def callback(self, instance):
        print('The button has been pressed')
        self.manager.current = 'weatherScreen'

    def on_touch_move(self, touch):
      if touch.x > touch.ox: # this line checks if a right swipe has been detected
        self.manager.current = 'weatherScreen'

if __name__ == '__main__':
    PanelBuilderApp().run()
