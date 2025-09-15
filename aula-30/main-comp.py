#importação dos módulos
#Kivy - App para criar a aplicação, ScreenManager
#Kivy - ScreenManager para gerenciar multitelas e Screen para definir a tela
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

#Define a classe da tela de login

class TelaLogin(Screen):
# Função para validar credenciais e acessar a tela principal
    def validar_login(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if usuario == 'admin' and senha == '123':
            self.manager.current = 'boas_vindas'
        else:
            self.ids.resultado.text = 'Usuário ou senha incorretos.'

# Classe da tela de boas-vindas
class TelaBoasVindas(Screen):
    pass

# Classe principal da aplicação, metodo build
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

#inicia essa aplicação
MyApp().run()

