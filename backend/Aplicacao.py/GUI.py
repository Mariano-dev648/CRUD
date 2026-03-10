from tkinter import *

#Importação do tkinter e definição do paddle para a interface gráfica
class Gui ():
    """classe da interface gráfica
    """
    x_pad = 5
    y_pad = 3
    Width_entry = 30

#Para criar uma janela 
#PYSQL será o nome fantasia da aplicação

window = Tk()
window.wm_title("PYSQL versão 1.0")

#definição das variaveis que recebem os dados inseridos pelo user

txtNome = StringVar()
txtSobrenome = StringVar()
txtEmail = StringVar()
txtCPF = StringVar()

# Criando os objetos que farão parte das janelas

lblnome = Label(window, text="Nome")
lblSobrenome = Label(window, text="Sobrenome")
lblEmail = Label(window, text="Email")
lblCPF = Label(window, text="CPF")
entNome = Entry(window, textvariable=txtNome, width=Gui.Width_entry)

entSobrenome = Entry(window, textvariable=txtSobrenome, width=Gui.Width_entry)
entEmail = Entry(window, textvariable=txtEmail, width=Gui.Width_entry)
entCPF = Entry(window, textvariable=txtCPF, width=Gui.Width_entry)

listClientes = Listbox(window, width=100)
scrollClientes = Scrollbar (window)
btnViewALL = Button(window, text="Ver Todos")
btnBuscar = Button(window, text="Buscar")
btnInserir = Button(window, text="Inserir")
btnUpdate = Button(window, text="Atualizar Selecionados")
btnDel = Button(window, text="Deletar Selecionados")
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
btnViewALL.grid(row=4, column=0)
btnBuscar.grid(row=5, column=0, columnspan=2)
btnInserir.grid(row=6, column=0, columnspan=2)
btnUpdate.grid(row=7, column=0, columnspan=2)
btnDel.grid(row=8, column=0, columnspan=2)
btnClose.grid(row=9, column=0, columnspan=2)

#União do Scrollbar com a Listbox

listClientes.configure(yscrollcommand=scrollClientes.set)
scrollClientes.configure(command=listClientes.yview)

for child in window.winfo_children():
    widget_class = child.__class__.__name__
    if widget_class == "Button":
        child.grid_configure(sticky='We', padx=Gui.x_pad, pady=Gui.y_pad)
    elif widget_class == "Listbox":
        child.grid_configure(padx=0, pady=0, sticky='NS')
    elif widget_class == "Scrollbar":
        child.grid_configure(padx=0, pady=0, sticky='NS')
    else:
        child.grid_configure(padx=Gui.x_pad, pady=Gui.y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()
