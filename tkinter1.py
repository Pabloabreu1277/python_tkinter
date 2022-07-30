from tkinter import*

root = Tk()

class app():
    def __init__(self):
        self.root = root
        self.tela()
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
        self.root.iconbitmap('customer-service-gear.ico')


app()