from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text='Digite seu usuário e senha')
        self.usuario = TextInput(hint_text='Usuário', multiline=False)
        self.senha = TextInput(hint_text='Senha', password=True, multiline=False)
        self.botao = Button(text='Entrar', on_press=self.validar_login)
        self.resultado = Label(text='')

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.usuario)
        self.layout.add_widget(self.senha)
        self.layout.add_widget(self.botao)
        self.layout.add_widget(self.resultado)

        return self.layout

    def validar_login(self, instance):
        if self.usuario.text == 'admin' and self.senha.text == '123':
            self.resultado.text = 'Login bem-sucedido!'
        else:
            self.resultado.text = 'Usuário ou senha incorretos.'

LoginApp().run()