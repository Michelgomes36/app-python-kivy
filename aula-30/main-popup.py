from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.usuario = TextInput(hint_text='Usuário', multiline=False)
        self.senha = TextInput(hint_text='Senha', password=True, multiline=False)

        btn_entrar = Button(text='Entrar')
        btn_entrar.bind(on_press=self.validar_login)

        layout.add_widget(self.usuario)
        layout.add_widget(self.senha)
        layout.add_widget(btn_entrar)

        self.add_widget(layout)

    def validar_login(self, instance):
        if self.usuario.text == 'admin' and self.senha.text == '123':
            self.manager.current = 'boas_vindas'
        else:
            self.mostrar_popup('Usuário ou senha incorretos.')

    def mostrar_popup(self, mensagem):
        conteudo = BoxLayout(orientation='vertical', padding=10, spacing=10)
        conteudo.add_widget(Label(text=mensagem))
        btn_fechar = Button(text='Fechar', size_hint=(1, 0.3))
        conteudo.add_widget(btn_fechar)

        popup = Popup(title='Erro de Login',
                      content=conteudo,
                      size_hint=(0.7, 0.4),
                      auto_dismiss=False)
        btn_fechar.bind(on_press=popup.dismiss)
        popup.open()

class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        layout.add_widget(Label(text='Bem-vindo!'))
        self.add_widget(layout)

class MeunovoApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

MeunovoApp().run()

