from tkinter import *

#Importação do tkinter e definição do paddle para a interface gráfica
class Gui ():
    """classe da interface gráfica
    """
    x_pad = 5
    t_pad = 3
    width_entry = 30

#Para criar uma janela 
#PYSQL será o nome fantasia da aplicação

window = Tk()
window.wm_title("PYSQL versão 1.0")

#definição das variaveis que recebem os dados inseridos pelo user

txtNome_StringVar()
txtSobrenome_StringVar()
txtEmail_StringVar()
txtCPF_StringVar()

# Criando os objetos que farão parte das janelas

lblnome = Label(window, text="Nome")
lblSobrenome = Label(window, text="Sobrenome")
lblEmail = Label(window, text="Email")
lblCPF = Label(window, text="CPF")
entNome = Entry(window, textvariable=txtNome, width=width_entry)

entSObrenome = Entry(window, textvariable=txtSobrenome, width=width_entry)
entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
entCPF = Entry(window, textvariable=txtCPF, width=width_entry)

listClientes = Listbox(window, width=100)
scrollClientes = scrollbar (window)
btnViewAll = Button(window, text="Ver Todos")
btnBuscar = Button(window, text="Buscar")
btnInserir = Button(window, text="Inserir")
btnUpdate = Button(window, text="Atualizar Selecionados")
btnDell = Button(window, text="Deletar Selecionados")
btnClose = Button(window, text="Fechar")

# associando os objetos criados ao Grid da Janela

lblnome.grid(row=0, column=0)
lblSobrenome.grid(row=1, column=0)
lblEmail.grid(row=2, column=0)
lblCPF.grid(row=3, column=0)
entNome.grid(row=0, column=1, padx=50, pady=50)
entSobrenome.grid(row=1, column=1)
entEmail.grid(row=2, column=1)
entCPF.grid(row=3, column=1)
listClientes.grid(row=0, column=2, rowspan=10)
scrollClientes.grid(row=0, column=6, rowspan=10)
btnViewAll.grid(row=4, column=0)
btnBuscar.grid(row=5, column=0, columnspan=2)
btnInserir.grid(row=6, column=0, columnspan=2)
btnUpdate.grid(row=7, column=0, columnspan=2)
btnDel.grid(row=8, column=0, columnspan=2)
btnClose.grid(row=9, column=0, columnspan=2)

#União do Scrollbar com a Listbox

listClientes.configure(yscrollcommand=scrollClientes.set)
ScrollClientes.configure(command=listClientes.yview)

for chield in window.winfo_children():
    widget_class = child.__class__.__name__
    if widget_class == "Button":
        child.grid_configure(sticky='We', padx=_pad, pady=y_pad)
    elif widget_class == "listbox":
        child.grid_configure(padx=0, pady=0, sticky='NS')
    elif widget_class == "Scrollvar":
        child.grid_configure(padx=0, pady=0, sticky='NS')
    else:
        child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()

