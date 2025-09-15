#importação dos módulos
#Kivy - App para criar a aplicação, ScreenManager
#Kivy - ScreenManager para gerenciar multitelas e Screen para definir a tela
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

#Define as duas telas utilizadas no aplicativo
class TelaLogin(Screen):
    pass

class TelaBoasVindas(Screen):
    pass

#Classe de criação da aplicação, metodo build
class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaBoasVindas(name='boas_vindas'))
        return sm

#inicia essa aplicação
MeuApp().run()