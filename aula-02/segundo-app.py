# Importa a classe base da aplicação Kivy
from kivy.app import App
# Importa o layout em grade (GridLayout)
from kivy.uix.gridlayout import GridLayout
# Importa os componentes visuais: rótulo e campo de texto
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# Define a classe principal da aplicação
class Meu2App(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=20)
        layout.add_widget(Label(text='Usuario:'))
        layout.add_widget(TextInput())
        layout.add_widget(Label(text='Senha:'))
        layout.add_widget(TextInput(password=True))
        return layout
# Executa a aplicação
Meu2App().run()