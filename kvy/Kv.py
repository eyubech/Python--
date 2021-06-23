
import kivy
from kivy.app import App
kivy.require('1.9.0')

from kivy.uix.image import Image


# creating the App class
class MyApp(App):

    # defining build()

    def build(self):
        return Image(source='1.jpg')



# run the App
MyApp().run()