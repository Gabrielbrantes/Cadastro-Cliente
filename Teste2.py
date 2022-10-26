import PySimpleGUI as sg
import os

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('login',layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "login":
        senha_correta = 'Daniel.1703'
        usuario_correto = 'gabriel.brantes_2013@hotmail.com'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha ou usuário incorreto')


            