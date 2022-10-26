from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk 
import datetime as dt

#Fazer com que a Janela não  seja redimencionavel, de tamanho fixo (Ver isso Depois!!!! ): Dica do meu amor! (Outra dica formulário responsivo!)


lista_brindes = ["Bolsinha", "Bolsinha Quadrada", "Estojo", "Estojão", "Estojo Box", "Kit Dente", "Porta Moeda", "Mini-Lousa", "Cachepô", ]

janela = tk.Tk()


janela.title('Formulário de Pedidos')

label_descricao = tk.Label(text="Nome Cliente")
label_descricao.grid(row=1, column=0, padx= 10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx= 10, pady=10, sticky='nswe', columnspan=4)

label_tipo_unidade = tk.Label(text="Selecione o Brinde")
label_tipo_unidade.grid(row=3, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_brindes)
combobox_selecionar_tipo.grid(row=3, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)

#Quantidade dos Brindes

label_quant = tk.Label(text="Quantidade de Brindes")
label_quant.grid(row=4, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

label_quant = tk.Entry()
label_quant.grid(row=4, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)

#Tema dos Brindes

label_tema = tk.Label(text="Tema do Brinde")
label_tema.grid(row=5, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

entry_tema = tk.Entry()
entry_tema.grid(row=5, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)

# Cor 1 e 2 

label_cor = tk.Label(text="Cor 1")
label_cor.grid(row=6, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

entry_cor = tk.Entry()
entry_cor.grid(row=6, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)

label_cor = tk.Label(text="Cor 2")
label_cor.grid(row=7, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

entry_cor = tk.Entry()
entry_cor.grid(row=7, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)

#----------------------------------------------------------------------------

label_descricao = tk.Label(text="Descrição")
label_descricao.grid(row=8, column=0, padx= 10, pady=10, sticky='nswe', columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=9, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

#Nome da Criança

label_nome_crianca = tk.Label(text="Nome da Criança")
label_nome_crianca.grid(row=10, column=0, padx= 10, pady=10, sticky='nswe', columnspan=2)

entry_nome_crianca = tk.Entry()
entry_nome_crianca.grid(row=10, column=2, padx= 10, pady=10, sticky='nswe', columnspan=2)


botao_imprimir = tk.Button(text="Imprimir")
botao_imprimir.grid(row=12, column=0, padx= 10, pady=10, sticky='nswe', columnspan=4)


janela.mainloop()
