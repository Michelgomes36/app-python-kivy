from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class TelaLogin(Screen):
    def validar(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if App.get_running_app().validar_login(usuario, senha):
            self.manager.current = 'principal'
        else:
            self.mostrar_popup('Usuário ou senha incorretos.')

    def mostrar_popup(self, mensagem):
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=mensagem))
        btn = Button(text='Fechar', size_hint=(1, 0.3))
        box.add_widget(btn)
        popup = Popup(title='Erro de Login', content=box, size_hint=(0.6, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()

class TelaCadastro(Screen):
    def salvar(self):
        usuario = self.ids.novo_usuario.text
        senha = self.ids.nova_senha.text
        if usuario and senha:
            App.get_running_app().salvar_usuario(usuario, senha)
            self.manager.current = 'login'
        else:
            self.mostrar_popup('Preencha todos os campos.')

    def mostrar_popup(self, mensagem):
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=mensagem))
        btn = Button(text='Fechar', size_hint=(1, 0.3))
        box.add_widget(btn)
        popup = Popup(title='Cadastro', content=box, size_hint=(0.6, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()

class TelaPrincipal(Screen):
    pass

