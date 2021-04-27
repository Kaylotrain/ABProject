from logging import addLevelName
from typing import Text
from PIL.Image import NONE
from kivy.core import window
from kivy.core.image import Image
from kivymd.uix import textfield
from kivymd.uix.behaviors import backgroundcolor_behavior
from uix.imagelist import SmartTileWithLabel
from uix.button import MDFlatButton, MDFloatingLabel, MDRaisedButton
from uix.list import ImageLeftWidget, OneLineListItem
from kivymd.app import MDApp
from kivy.lang.builder import Builder, delayed_call_fn
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix import screen
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import TwoLineAvatarListItem
from kivy.uix.button import Button
Window.size = (500,800)






def iserror(func, *args, **kw):
    try:
        func(*args, **kw)
        return False
    except Exception:
        return True
class product ():
    name = ""
    price = None
    image = ""
    object = None 
    id = None
    image = ""
    def __init__(self,name,price,id,image):
        self.name = name
        self.price = int(price)
        self.id = id
        self.image = image
        self.object=(SmartTileWithLabel(size_hint_y= None,height= 240,size_hint_x = None,width = Window.size[0]/3,text = name +"\n" + price,source = image,on_press = self.press))
        
    def press(self,obj):
        AddScreen.ac(self)
class AddScreen(Screen):
    products = []
    index = 0
    dele = False
    def add_item(self,name,price,image):
        if(price.isnumeric() == False or price == "" or name == ""):
            MDApp.get_running_app().root.get_screen("add").ids.item_name.text = ""
            MDApp.get_running_app().root.get_screen("add").ids.item_price.text = ""

            return
        self.products.append(product(name,price,AddScreen.index,image))
        MDApp.get_running_app().root.get_screen("menu").ids.grid.add_widget(self.products[AddScreen.index].object)
        MDApp.get_running_app().root.get_screen("add").ids.item_name.text = ""
        MDApp.get_running_app().root.get_screen("add").ids.item_price.text = ""
        AddScreen.index = AddScreen.index + 1
    def ac(object):
        if(AddScreen.dele):
            MDApp.get_running_app().root.get_screen("menu").ids.grid.remove_widget(object.object)
            AddScreen.index = AddScreen.index - 1
            AddScreen.products.pop(object.id)
            i = 0
            for x in AddScreen.products:
                print(i)
                x.id = i
                i += 1 
                
        else:
            print(object.id)
    def deletee(self):
        if(AddScreen.dele == True):
            AddScreen.dele = False
        else:
            AddScreen.dele = True
        
class MenuScreen(Screen):
    def addlist(app):
        ##app.root.ids.list.add_widget(OneLineListItem(text="asdasd"))
        pass
        

sm = ScreenManager()
sm.add_widget(MenuScreen(name ='menu'))


class MyApp(MDApp):  
    def build(self):
        kv = Builder.load_file("app.kv")
        return kv
    def on_start(self):
        self.root.get_screen("menu").ids.list.add_widget(OneLineListItem(text="asdasd"))
        pass
        

if __name__ == '__main__':
    MyApp().run()