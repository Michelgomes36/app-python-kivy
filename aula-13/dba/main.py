from kivy.app import App
from kivy.lang import Builder
import sqlite3

class MeuApp(App):
    def build(self):
        self.conexao = sqlite3.connect('meu_banco.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS pessoas (nome TEXT)')
        self.conexao.commit()
        return Builder.load_file('interface.kv')

    def salvar_nome(self):
        nome = self.root.ids.nome_input.text
        if nome:
            self.cursor.execute('INSERT INTO pessoas (nome) VALUES (?)', (nome,))
            self.conexao.commit()
            self.root.ids.status.text = f'Nome "{nome}" salvo!'
            self.root.ids.nome_input.text = ''
        else:
            self.root.ids.status.text = 'Digite um nome válido.'

    def mostrar_nomes(self):
        self.cursor.execute('SELECT nome FROM pessoas')
        nomes = [linha[0] for linha in self.cursor.fetchall()]
        if nomes:
            self.root.ids.status.text = 'Nomes salvos:\n' + '\n'.join(nomes)
        else:
            self.root.ids.status.text = 'Nenhum nome salvo ainda.'

    def on_stop(self):
        self.conexao.close()

MeuApp().run()
