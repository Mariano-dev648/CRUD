from tkinter import *

class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.wm_title("Cadastro de Clientes")

        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        self.entNome = Entry(self.window, textvariable=self.txtNome)
        self.entNome.grid(row=0, column=1)

        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome)
        self.entSobrenome.grid(row=0, column=3)

        self.entEmail = Entry(self.window, textvariable=self.txtEmail)
        self.entEmail.grid(row=1, column=1)

        self.entCPF = Entry(self.window, textvariable=self.txtCPF)
        self.entCPF.grid(row=1, column=3)

        self.listClientes = Listbox(self.window, width=80, height=10)
        self.listClientes.grid(row=2, column=0, columnspan=4, rowspan=6)

        self.scrollClientes = Scrollbar(self.window)
        self.scrollClientes.grid(row=2, column=4, rowspan=6, sticky='ns')

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        self.btnViewAll = Button(self.window, text="Ver todos")
        self.btnViewAll.grid(row=2, column=5)

        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnBuscar.grid(row=3, column=5)

        self.btnInserir = Button(self.window, text="Inserir")
        self.btnInserir.grid(row=4, column=5)

        self.btnUpdate = Button(self.window, text="Atualizar")
        self.btnUpdate.grid(row=5, column=5)

        self.btnDel = Button(self.window, text="Deletar")
        self.btnDel.grid(row=6, column=5)

        self.btnClose = Button(self.window, text="Fechar")
        self.btnClose.grid(row=7, column=5)

    def run(self):
        self.window.mainloop()