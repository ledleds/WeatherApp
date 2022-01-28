import kivy
kivy.require('2.0.0') 

from kivy.uix.label import Label
from datetime import datetime as dt
from datetime import timedelta as td

class Time(Label):
    def __init__(self, *args):
      self.now = dt.now()
      
      self.current_time = Label(
        text = self.now.strftime('%-I:%M %p').lower(), 
        text_size= (800, 200),
        halign="left",
        pos_hint= {'x': .49, 'y': .7},
        size_hint= (None, None),
        font_size= 140)

      self.current_date = Label(
        text = self.now.strftime('%A %d %B %Y'), 
        text_size= (500, 200),
        halign="left",
        pos_hint= {'x': .31, 'y': .64},
        size_hint= (None, None),
        font_size= 30
      )

    def update_clock(self, *args):
      self.now = dt.now()
      self.current_time.text = self.now.strftime('%-I:%M %p').lower()

      # If it is midnight, update the date too.
      if self.now.hour == 0 and self.now.minute == 0 and self.now.second == 0:
        self.update_date()

    def update_date(self, *args):
      print('Updating date')
      self.current_date.text = self.now.strftime('%A %d %B %Y')

    def seconds_until_next_hour(self):
      delta = td(hours=1)
      next_hour = (self.now + delta).replace(microsecond=0, second=0, minute=2)

      return (next_hour - self.now).seconds
