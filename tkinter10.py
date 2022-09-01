#SISTEMA DE CADASTRO PABLO 2022
#base:https://www.youtube.com/watch?v=RtrZcoVD1WM&list=PLqx8fDb-FZDFznZcXb_u_NyiQ7Nai674-
from tkinter import*
from tkinter import ttk
import sqlite3
root = Tk()

#classe para execultar a função de apagar os dados do formulario
class funcs():
#função para execultar a limpeza das label
    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.tel_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("cliente_bd")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self): 
        self.conn.close(); print("Conectando ao banco de dados")
    def monta_tabelas(self):
        self.conecta_bd()
# criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)

            );
        """)
        self.conn.commit(); print("banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.tel = self.tel_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """ , (self.nome, self.tel, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()
        
    def select_lista(self):
        
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listacli.insert("", END, values=i)
        self.desconecta_bd()
    def ondoubleclick(self, event):
        self.limpar_tela()
        self.listacli.selection()
        for n in self.listacli.selection():
            col1, col2, col3, col4 = self.listacli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.tel_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):       
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()



#classe para criar o formulario GUI        
class app(funcs):
#função para chamar as ações da construção da tela
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela1()
        self.frames_da_tela2()
        self.widget()
        self.monta_tabelas()
        self.select_lista()

        root.mainloop()

#função de criação da tela conforme projeto
    def tela (self):
#titulo da janela
        self.root.title("Cadastros Tkinter")

#cor da janela
        self.root.configure(background ='black')
# Geometria da janela
        self.root.geometry("600x600")
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


    def frames_da_tela1(self):
# telas sobrepostas frame sup
        self.frame_1 = Frame(self.root, bd = 5,
                             bg = 'snow4',highlightbackground= 'goldenrod',highlightthickness=5)   
        self.frame_1.place(relx= 0.01 , rely= 0.01, relwidth= 0.98, relheight=0.45)
# telas sobrepostas frame inf    
        self.frame_2 = Frame(self.root, bd=5,
                             bg='snow4', highlightbackground='goldenrod', highlightthickness=5)
        self.frame_2.place(relx=0.01, rely=0.47, relwidth=0.98, relheight=0.45)
    def widget(self):
# botão de limpar
        self.bt_limpar = Button(self.frame_1, text='LIMPAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'), command = self.limpar_tela)
        self.bt_limpar.place(relx= 0.01, rely=0, relwidth=0.11, relheight=0.15)
# botão de buscar
        self.bt_buscar = Button(self.frame_1, text='BUSCAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.bt_buscar.place(relx= 0.2, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de novo
        self.bt_novo = Button(self.frame_1, text='NOVO',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'), command = self.add_cliente)
        self.bt_novo.place(relx= 0.4, rely=0.0, relwidth=0.11, relheight=0.15)
# botão de alterar
        self.bt_alterar = Button(self.frame_1, text='ALTERAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.bt_alterar.place(relx= 0.6, rely=0.0, relwidth=0.12, relheight=0.15)
# botão de apagar
        self.bt_apagar = Button(self.frame_1, text='APAGAR',bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'), command=self.deleta_cliente )
        self.bt_apagar.place(relx= 0.85, rely=0.0, relwidth=0.12, relheight=0.15)
# criação label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "CÓDIGO",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_codigo.place(relx= 0.0, rely= 0.2)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx= 0.0, rely= 0.3)
# criação label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "NOME",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_nome.place(relx= 0.3, rely= 0.2)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx= 0.30, rely= 0.3)
# criação label e entrada do telefone
        self.lb_tel = Label(self.frame_1, text = "TELEFONE",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_tel.place(relx= 0.6, rely= 0.2)
        self.tel_entry = Entry(self.frame_1)
        self.tel_entry.place(relx= 0.6, rely= 0.3)
# criação label e entrada do CIDADE
        self.lb_cidade = Label(self.frame_1, text = "CIDADE",bd = 3, bg = 'royal blue', fg ='White'
                               , font = ('verdana',7,'bold'))
        self.lb_cidade.place(relx= 0.0, rely= 0.45)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx= 0.0, rely= 0.55)
    
    def frames_da_tela2(self):
        self.listacli = ttk.Treeview(self.frame_2, height = 3, column=("col1","col2","col3","col4"))
        self.listacli.heading("#0", text="")
        self.listacli.heading("#1", text="Codigo")
        self.listacli.heading("#2", text="Nome")
        self.listacli.heading("#3", text="Telefone")
        self.listacli.heading("#4", text="Cidade")
        self.listacli.column("#0", width=1)
        self.listacli.column("#1", width=50)
        self.listacli.column("#2", width=200)
        self.listacli.column("#3", width=125)
        self.listacli.column("#4", width=125)
        self.listacli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        self.scroollista = Scrollbar(self.frame_2, orient='vertical')
        self.listacli.configure(yscroll=self.scroollista.set)
        self.scroollista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85 )
        self.listacli.bind("<Double-1>", self.ondoubleclick )
        



app()