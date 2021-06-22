from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


runTouchApp(Builder.load_string('''
BoxLayout:
    Button:
        text:'B1'
        size_hint_x: 0.5
    Button:
        text:'B2'
        size_hint_x:1
    Button
        text:'B3'
        size_hint_x:0.5
'''))

class MyList(BoxLayout):
    pass

if __name__=='__main__':
    runTouchApp(MyList())