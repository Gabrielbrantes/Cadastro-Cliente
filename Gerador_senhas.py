import random
import PySimpleGUI as sg
import os

class PassGen:
    def __init__(self):
        #layout
        sg.theme('Purple')
        layout = [
            [sg.Text('Site/Software', size=(12,1)), sg.Input(key='site',size=(25,1))],
            [sg.Text('E-mail/Usuário', size=(12,1)), sg.Input(key='usuario',size=(25,1))],
            [sg.Text('Quantidade de caracteres'),sg.Combo(values=list(range(30)),key='total_chars', default_value=1, size=(5,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha')]
        ]
        #Declarar janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break

    def salvar_senha(self):
        pass
       
gen = PassGen()
gen.Iniciar()