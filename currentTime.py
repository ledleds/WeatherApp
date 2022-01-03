import kivy
kivy.require('2.0.0') 

from kivy.uix.label import Label
from datetime import datetime as dt

class Time(Label):
    def __init__(self, *args):
      self.now = dt.now()
      
      self.current_time = Label(
        text = self.now.strftime('%-I:%M %p'), 
        text_size= (800, 200),
        halign="left",
        pos_hint= {'x': .49, 'y': .85},
        size_hint= (None, None),
        font_size= 100)

      self.current_date = Label(
        text = self.now.strftime('%A %d %B %Y'), 
        text_size= (250, 200),
        halign="left",
        pos_hint= {'x': .15, 'y': .82},
        size_hint= (None, None),
        font_size= 19
      )

    def update_clock(self, *args):
      self.now = dt.now()
      self.current_time.text = self.now.strftime('%-I:%M %p')

      # If it is midnight, update the date too.
      if self.now.hour == 0 and self.now.minute == 0 and self.now.second == 0 and self.now.microsecond == 0:
        self.update_date()

    def update_date(self, *args):
      print('Updating date')
      self.current_date.text = self.now.strftime('%A %d %B %Y')
