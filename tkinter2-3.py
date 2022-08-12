from tkinter import*

root = Tk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widget()
        root.mainloop()
    def tela (self):
#titulo da janela
        self.root.title("cadastro de O.S")

#cor da janela
        self.root.configure(background ='bisque')
# Geometria da janela
        self.root.geometry("500x500")
# redimensionável sim ou não
#         self.root.resizable(False, False)
        self.root.resizable(True, True)
# Maxima dimensão
        self.root.maxsize(width = 1000, height = 1000)
# minima dimensão
        self.root.minsize(width = 500, height = 500)
# transparencia de 0 a 1
        self.root.attributes('-alpha',1)
# prioridade no empilhamento de janelas.
        self.root.attributes('-topmost', 1)
# iconis https://iconscout.com/icons/service?price=free
        self.root.iconbitmap("customer-service-gear.ico")


    def frames_da_tela(self):
# telas sobrepostas frame sup
        self.frame_1 = Frame(self.root, bd = 5,
                             bg = 'azure3',highlightbackground= 'black',highlightthickness=5)   
        self.frame_1.place(relx= 0.01 , rely= 0.01, relwidth= 0.98, relheight=0.45)
# telas sobrepostas frame inf    
        self.frame_2 = Frame(self.root, bd=5,
                             bg='azure3', highlightbackground='black', highlightthickness=5)
        self.frame_2.place(relx=0.01, rely=0.47, relwidth=0.98, relheight=0.45)
    def widget(self):
# botão de limpar
        self.bt_limpar = Button(self.frame_1, text='LIMPAR')
        self.bt_limpar.place(relx= 0.01, rely=0, relwidth=0.11, relheight=0.15)
# botão de buscar
        self.bt_buscar = Button(self.frame_1, text='BUSCAR')
        self.bt_buscar.place(relx= 0.2, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de novo
        self.bt_novo = Button(self.frame_1, text='NOVO')
        self.bt_novo.place(relx= 0.4, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de alterar
        self.bt_alterar = Button(self.frame_1, text='ALTERAR')
        self.bt_alterar.place(relx= 0.6, rely=0.0, relwidth=0.12, relheight=0.15)
# botão de apagar
        self.bt_apagar = Button(self.frame_1, text='APAGAR')
        self.bt_apagar.place(relx= 0.85, rely=0.0, relwidth=0.12, relheight=0.15)
# criação label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "CÓDIGO")
        self.lb_codigo.place(relx= 0.0, rely= 0.2)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.0, rely= 0.3)
# criação label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "NOME")
        self.lb_nome.place(relx= 0.3, rely= 0.2)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.30, rely= 0.3)
# criação label e entrada do telefone
        self.lb_tel = Label(self.frame_1, text = "TELEFONE")
        self.lb_tel.place(relx= 0.6, rely= 0.2)
        self.tel_entry = Entry(self.frame_1)
        self.tel_entry.place(relx= 0.6, rely= 0.3)
# criação label e entrada do CIDADE
        self.lb_cidade = Label(self.frame_1, text = "CIDADE")
        self.lb_cidade.place(relx= 0.0, rely= 0.45)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.0, rely= 0.55)




app()