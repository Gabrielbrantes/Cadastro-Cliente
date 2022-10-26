import random
import PySimpleGUI as sg 
import os

class PassGen:
    def __init__(self):
        #Layout
        sg.theme('Purple')
        layout = [
            [sg.Text('Site/Programa', size=(12,1)), sg.Input(key='site', size=(25,1))],
            [sg.Text('Email/Usuário', size=(12,1)), sg.Input(key='usuario', size=(25,1))],
            [sg.Text('Quantidade de Caracteres'), sg.Combo(values=list(range(31)), key='total_chars', default_value=1, size=(5,1))],
            [sg.Output(size=(32,5))],
            [sg.Button('Gerar Senha')]
        ]
        #Janela
        self.janela = sg.Window('Gerador de Senha', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break

    def salvar_senha(self):
        pass

gen = PassGen()
gen.Iniciar()