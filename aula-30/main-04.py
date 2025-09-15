from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Tela de Login
class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text='Tela de Login'))

        self.usuario = TextInput(hint_text='Usuário', multiline=False)
        layout.add_widget(self.usuario)

        self.senha = TextInput(hint_text='Senha', password=True, multiline=False)
        layout.add_widget(self.senha)

        btn_entrar = Button(text='Entrar')
        btn_entrar.bind(on_press=self.entrar)
        layout.add_widget(btn_entrar)

        self.add_widget(layout)

    def entrar(self, instance):
        self.manager.current = 'boas_vindas'

# Tela de Boas-Vindas
class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super(TelaBoasVindas, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text='Bem-vindo!'))

        btn_voltar = Button(text='Voltar')
        btn_voltar.bind(on_press=self.voltar)
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'login'

# App principal
class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

if __name__ == '__main__':
    MeuApp().run()
