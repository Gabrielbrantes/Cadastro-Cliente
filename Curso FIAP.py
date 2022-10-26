import PySimpleGUI as sg

class PassGen:
    def __init__(self):
        #layout
        sg.theme('Purple')
        layout = [
            [sg.Text('Paciente', size=(12,1)), sg.Input(key='paciente',size=(25,1))],
            [sg.Text('Idade', size=(12,1)), sg.Input(key='idade',size=(25,1))],
            [sg.Output(size=(55,40))],
            [sg.Button('Conferir')]
          ]

        self.janela = sg.Window('Calculadora de exame', layout)
    
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WIN_CLOSED:
                break
            elif evento == "Calculadora de exame":
                idade_correta>= '45'
                paciente_correto = ' '
                paciente = values['paciente']
                idade = values['idade']
                if idade == idade_correta and paciente == paciente_correto:
                  sg.output()
                  print('Terá de fazer exame de prostata')
                else:
                  sg.output()
                  print('Não terá de fazer exame de prostata')
                  
                
gen = PassGen()
gen.Iniciar()


