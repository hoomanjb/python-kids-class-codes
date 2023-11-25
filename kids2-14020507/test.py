from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.app import App
from kivy.lang.builder import Builder
import requests


class MDFloatLayout(FloatLayout):
    pass

a = 700
b = 960

class main(App):
    def build(self):
        Window.size = (a, b)
        Window.clearcolor = (1, 1, 1, 1)
        response = requests.get(
            'https://api.openweathermap.org/data/2.5/weather?q=ramsar&appid=1dd799b5f02d6af897b2f0f1d06f543d')
        jsonResponse = response.json()
        city = jsonResponse['name']
        temperature = jsonResponse['main']['temp'] - 273

        style = Builder.load_string('''
MDFloatLayout:
    Image:
        source: 'C:/Users/Kian/Desktop/api/assets/7474511.png'
        size_hint: None, None
        size: 100, 100
        pos_hint: {'x':0, 'y':0.1}

        keep_ratio: False
''')

        print("city: " + city + "\n" + "Temperature: " + str(temperature))
        return style


main().run()

