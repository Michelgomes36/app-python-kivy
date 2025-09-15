from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text='Login'))
        layout.add_widget(Button(text='Cadastrar'))
        layout.add_widget(Button(text='Sair'))
        return layout

MeuApp().run()