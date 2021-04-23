from configparser import MissingSectionHeaderError
from kivymd.app import MDApp
from kivy.lang import Builder, builder
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.core.window import Window

Window.size = (720,1280)

screen_helper = """
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

                    
            

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'inventario'
            icon: 'plus-box-multiple'
            ScrollView:
                MDGridLayout:
                    cols: 1
                    adaptive_height: True
                    padding: dp(20), dp(20)
                    spacing: dp(4)
                   
                    MDTextField:
                        hint_text: "nombre del producto"
                    MDTextField:
                        hint_text: "precio base"
                    MDGridLayout:
                        cols: 2
                        adaptive_height: True
                        padding: dp(20), dp(20)
                        spacing: dp(20)
                        MDIconButton:
                            icon: "camera"
                            user_font_size: "130sp"
                        MDIconButton:
                            icon: "check-circle"
                            user_font_size: "130sp"
                            """

class Test(MDApp):

    
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


Test().run()
