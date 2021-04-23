from configparser import MissingSectionHeaderError
from ctypes import Array
from logging import setLogRecordFactory
from re import X
from typing import NoReturn
from kivy import app

from kivymd.uix import screen
from uix.list import OneLineListItem
import kivy 
from kivymd.app import MDApp
from kivy.lang import Builder, builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget


class mainmenu(Screen):
    def hi (self,array=[]):
        for x in range(100):
            self.root.ids.list.add_widget(OneLineListItem(text = str(x)))
            
    
    pass

class MyApp(MDApp):
    
    def build(self):
        print(dir(app))
        #app.root.ids.grid.add_widget(MDLabel(text = "=asd"))
        #app.Widget.root.ids.list.add_widget(MDLabel(text = "=asd"))
        x = []
        
        mainmenu.hi(self,x)

        
    

    
   

    
    

        return super().build()

        

        

if __name__ == '__main__':
    MyApp().run()