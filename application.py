import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChildApp(GridLayout):
    def __init__(self,**kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = 'Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Building Number'))
        self.s_buildingno = TextInput()
        self.add_widget(self.s_buildingno)

        self.add_widget(Label(text='Home Number'))
        self.s_homeno = TextInput()
        self.add_widget(self.s_homeno)

        self.press = Button(text = 'Submit')
        self.press.bind(on_press = self.submit)
        self.add_widget(self.press)

    def submit(self, instance):
        print("Visitor Name: "+self.s_name.text)
        print("Building number is: " + self.s_buildingno.text)
        print("Home number is: " + self.s_homeno.text)
        print("")


class ParentApp(App):
    def build(self):
        return ChildApp()

if __name__ == "__main__":
    ParentApp().run()