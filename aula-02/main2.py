from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class MeuApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=20)
        layout.add_widget(Label(text='Usuário:'))
        layout.add_widget(TextInput())
        layout.add_widget(Label(text='Senha:'))
        layout.add_widget(TextInput(password=True))
        return layout

MeuApp().run()