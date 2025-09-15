#Código que cria uma tela de login funcional usando Kivy com separação entre lógica (Python) e interface (KV). 

# Importa os componentes principais do Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Classe que representa o layout da tela de login
class LoginLayout(BoxLayout):
#função para verificar a usuário e senha
    def validar_login(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if usuario == 'admin' and senha == '123':
            self.ids.resultado.text = 'Login bem-sucedido!'
        else:
            self.ids.resultado.text = 'Usuário ou senha incorretos.'

# Classe principal da aplicação
class LoginApp(App):
    def build(self):
        return LoginLayout()

# Executa a aplicação
LoginApp().run()
