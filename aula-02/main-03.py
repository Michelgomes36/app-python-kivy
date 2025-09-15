from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LoginLayout(BoxLayout):
    def validar_login(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if usuario == 'admin' and senha == '123':
            self.ids.resultado.text = 'Login bem-sucedido!'
        else:
            self.ids.resultado.text = 'Usuário ou senha incorretos.'

class LoginApp(App):
    def build(self):
        return LoginLayout()

LoginApp().run()