#Esse código cria uma interface simples com três botões usando o Kivy.

# Importa a classe base da aplicação Kivy
from kivy.app import App
# Importa o botão e o layout em caixa (BoxLayout)
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Define a classe principal da aplicação
class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        layout.add_widget(Button(text='Login'))
        layout.add_widget(Button(text='Cadastrar'))
        layout.add_widget(Button(text='Sair'))
        return layout

# Executa a aplicação
MeuApp().run()
