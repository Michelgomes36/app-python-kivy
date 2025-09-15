from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class TelaLogin(Screen):
    def validar_login(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if usuario == 'admin' and senha == '123':
            self.manager.current = 'boas_vindas'
        else:
            self.ids.resultado.text = 'Usuário ou senha incorretos.'


class TelaBoasVindas(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

MyApp().run()