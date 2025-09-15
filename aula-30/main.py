from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaLogin(Screen):
    pass

class TelaBoasVindas(Screen):
    pass

class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

MeuApp().run()