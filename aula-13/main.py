from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from componentes import TelaLogin, TelaCadastro, TelaPrincipal
import json

class MeuApp(App):
    dados_usuarios = {}

    def build(self):
        Builder.load_file('interface.kv')
        self.carregar_dados()
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaCadastro(name='cadastro'))
        sm.add_widget(TelaPrincipal(name='principal'))
        return sm

    def carregar_dados(self):
        try:
            with open('usuarios.json', 'r') as f:
                self.dados_usuarios = json.load(f)
        except FileNotFoundError:
            self.dados_usuarios = {}

    def salvar_usuario(self, usuario, senha):
        self.dados_usuarios[usuario] = senha
        with open('usuarios.json', 'w') as f:
            json.dump(self.dados_usuarios, f)

    def validar_login(self, usuario, senha):
        return self.dados_usuarios.get(usuario) == senha

if __name__ == '__main__':
    MeuApp().run()