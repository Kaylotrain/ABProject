import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput;


class MyApp(App):

    def build(self):
        return LoginScreen()

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name:"))
        self.name = TextInputModified(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Last Name:"))
        self.Lname = TextInput(multiline=False)
        self.add_widget(self.Lname)
        self.add_widget(Label(text="Email:"))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)
        
class TextInputModified(TextInput):
    def __init__(self,**kwargs):
        super(TextInputModified,self).__init__(**kwargs)
        self.background_color = [1,0,0,1]
        self.padding = [50,50,50,50]

if __name__ == '__main__':
    MyApp().run()