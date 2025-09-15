from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Tela de Login
class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text='Login'))

        self.usuario = TextInput(hint_text='Usuário', multiline=False)
        self.senha = TextInput(hint_text='Senha', password=True, multiline=False)
        btn_entrar = Button(text='Entrar')
        btn_entrar.bind(on_press=self.entrar)

        btn_cadastrar = Button(text='Ir para Cadastro')
        btn_cadastrar.bind(on_press=self.ir_para_cadastro)

        layout.add_widget(self.usuario)
        layout.add_widget(self.senha)
        layout.add_widget(btn_entrar)
        layout.add_widget(btn_cadastrar)

        self.add_widget(layout)

    def entrar(self, instance):
        self.manager.current = 'principal'

    def ir_para_cadastro(self, instance):
        self.manager.current = 'cadastro'

# Tela de Cadastro
class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text='Cadastro'))

        self.nome = TextInput(hint_text='Nome completo', multiline=False)
        self.email = TextInput(hint_text='E-mail', multiline=False)
        self.senha = TextInput(hint_text='Senha', password=True, multiline=False)

        btn_salvar = Button(text='Salvar Cadastro')
        btn_salvar.bind(on_press=self.salvar)

        btn_voltar = Button(text='Voltar para Login')
        btn_voltar.bind(on_press=self.voltar)

        layout.add_widget(self.nome)
        layout.add_widget(self.email)
        layout.add_widget(self.senha)
        layout.add_widget(btn_salvar)
        layout.add_widget(btn_voltar)

        self.add_widget(layout)

    def salvar(self, instance):
        print(f"Cadastro salvo: {self.nome.text}, {self.email.text}")
        self.manager.current = 'login'

    def voltar(self, instance):
        self.manager.current = 'login'

# Tela Principal
class TelaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text='Bem-vindo à Tela Principal!'))

        btn_sair = Button(text='Sair')
        btn_sair.bind(on_press=self.sair)

        layout.add_widget(btn_sair)
        self.add_widget(layout)

    def sair(self, instance):
        self.manager.current = 'login'

# App principal
class MeuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaCadastro(name='cadastro'))
        sm.add_widget(TelaPrincipal(name='principal'))
        return sm

MeuApp().run()
