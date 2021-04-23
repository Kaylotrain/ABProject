from configparser import MissingSectionHeaderError
import kivy 
from kivymd.app import MDApp
from kivy.lang import Builder, builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen 


screen_helper= """ 
ScreenManager 
    MenuScreen: 
    
    

<MenuScreen>
    name: 'menu'

    BoxLayout:
        orientation:'vertical'

        
        MDToolbar:
            title: 'APP'
            md_bg_color: .1, .1, .1, 1
            specific_text_color: 1, 1, 1, 1

        MDBottomNavigation:
            panel_color: 1, 1, 1, 1

            MDBottomNavigationItem:

                name: 'screen 1'
                text: 'Calendario'
                icon: 'calendar'
                
                ScrollView:
                    MDList:

                        OneLineListItem:
                            text: "1"
                        OneLineListItem:
                            text: "2"
                        OneLineListItem:
                            text: "3"
                        OneLineListItem:
                            text: "4"
                        OneLineListItem:
                            text: "5"
                        OneLineListItem:
                            text: "6"
                        OneLineListItem:
                            text: "7"
                        OneLineListItem:
                            text: "8"
                            
                
                
                
            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'registrar'
                icon: 'database-plus'
                
                height: "240dp"
                ScrollView:
                    MDGridLayout:
                        cols: 4
                        adaptive_height: True
                        padding: dp(20), dp(20)
                        spacing: dp(20)
                        SmartTileWithLabel:
                            source: "main-header.jpg"
                            text: "hola"
                            size_hint_y: None
                            height: "120dp"
                        SmartTileWithLabel:
                            source: "main-header.jpg"
                            text: "hola"
                            size_hint_y: None
                            height: "120dp"
                        SmartTileWithLabel:
                            source: "main-header.jpg"
                            text: "hola"
                            size_hint_y: None
                            height: "120dp"
                        SmartTileWithLabel:
                            source: "main-header.jpg"
                            text: "hola"
                            size_hint_y: None
                            height: "120dp"

                        
    
"""
class MenuScreen(Screen):
    pass
class MyApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    MyApp().run()