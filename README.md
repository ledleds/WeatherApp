# WeatherApp

A weather app built using Python and Kivy to be displayed on a 5inch Raspberry Pi Display.

<img width="500" alt="Screenshot 2022-01-07 at 7 28 47 pm" src="https://user-images.githubusercontent.com/22013969/148596751-9dc46b0b-c5ac-4890-8a35-5c5f6b41a640.png">

## Running

### Install Dependencies

This is a Python Project, so make sure you have that installed.

Follow the instructions on Kivy [here](https://kivy.org/doc/stable/gettingstarted/installation.html) to install Kivy Version 2.0.0.

You will also need KivyMD, docks for installing that are [here](https://kivymd.readthedocs.io/en/0.104.0/getting-started.html).

### Secrets

You'll need to create an account on [Open Weather Map](https://api.openweathermap.org) and generate an API key to be replaced in the request on line 22 of weather.py.

### Now, run it

`python main.py`

## Things to add

- Sunset time
- Feels like time
- Rain volume (only when raining)
  - Decipher between light and heavy rain
- Humidity

Next Level:

- Multiscreens
- Weekly weather view
- Calendar overview
