#   ---------- Sorteador de Palavras ---------- #

# Desenvolvido por: Guilherme Evaristo
# Twitter: @guilhermigg
# 2018

# Importar os módulos
import random
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk

# Definições

lista = []
FONTE = 'Berlin Sans'
p2 = 'white'
p1 = '#005fb8'

# Montagem do programa

class Janela:
    def __init__(self, janela):
        janela.title('Sorteador de Palavras')
        janela.configure(bg=p1)
        janela.geometry('350x250')
        janela.resizable(False,False)

        # Criar e posicionar a entrada da palavra #
        
        self.palavra = Entry(janela,width=20,borderwidth=3,bg=p2,fg=p1)
        self.palavra.place(x=110,y=100)

        # Criar e posicionar as Labels #

        self.m_title = Label(janela,text='          Sorteador\t\t\t\t\t',font=('PRIMETIME','20'),bg=p2,fg=p1)
        self.m_title.place(x=0,y=0)

        self.m_msg = Label(janela,text='\t\t         Palavra: \t\t\t\t',bg=p2,fg=p1,font=(FONTE,'10'))
        self.m_msg.place(x=0,y=70)
                
        self.m_créditos = Label(janela, text=' \tCréditos: Guilherme Evaristo / Twitter: @guilhermigg\t\t\t\t',fg=p1,bg=p2,font=('Arial','8'))
        self.m_créditos.place(x=0,y=230)
        
        # Criar e posicionar os botões #
    
        self.bt_adicionar = Button(janela,text='Adicionar',fg=p1,bg=p2,font=(FONTE,'10'),command=self.adicionar)
        self.bt_adicionar.place(x=250,y=97)

        self.bt_sortear = Button(janela, text='Sortear', command=self.sorteio,bg=p2,fg=p1,borderwidth=3,state=DISABLED)
        self.bt_sortear.place(x=150,y=130)

        self.bt_reset = Button(janela,text='Resetar',command=self.reset,bg=p2,fg=p1,borderwidth=3)
        self.bt_reset.place(x=150,y=190)

        self.bt_mostrar = Button(janela,text='Visualizar',bg=p2,fg=p1,command=self.view,borderwidth=3)
        self.bt_mostrar.place(x=145,y=160)

        self.bt_remover = Button(janela,text='Remover',bg=p2,fg=p1,command=self.remove)
        self.bt_remover.place(x=40,y=100)

# Função que sorteia a palavra

    def sorteio(self):
        try:
            sortear = random.choice(lista)
            word_sort = str(f'A Palavra sorteada foi: {sortear}')
            msgbox.showinfo('Palavra Sorteado', word_sort)
        except IndexError:
            msgbox.showerror('Nenhuma palavra foi adicionada','Por favor, adicione uma palavra')

# Função que adiciona a palavra à lista de palavras
    def adicionar(self):
        palavra = self.palavra.get()
        palavra = (palavra).strip()
        if palavra == '':
            msgbox.showerror('Campo vazio',' Preencha o campo')

        elif palavra in lista:
            msgbox.showerror('Palavra já adicionada','A palavra já foi adicionada')

        else:
            lista.append(palavra)
            self.palavra.delete(0,END)
            if len(lista) >= 2:
                self.bt_sortear['state'] = NORMAL

# Função que remove uma palavra da lista

    def remove(self):
        x = self.palavra.get()
        if x not in lista:
            msgbox.showerror('Inexistente','A palavra não pode ser removida por que não foi adicionada')
        else:
            perg = msgbox.askquestion('Confirmar',(f'Você realmente quer remover a palavra {x}'))
            if perg == 'yes':
                lista.remove(x)
                self.palavra.delete(0,END)
                if len(lista) < 2:
                    self.bt_sortear['state'] = DISABLED
            else:
                print()

# Função que limpa/reinicia a lista
    
    def reset(self):
        pergunta = 'no'
        if lista == []:
            msgbox.showerror('Sem palavras','Não há nenhuma palavra para ser removida')
        else:
            pergunta = msgbox.askquestion('Confirma','Tem certeza que quer remover todas as palavras já adicionadas?')   
        if pergunta == 'yes':
            lista.clear()
            self.bt_sortear['state'] = DISABLED
        else:
            print()

# Função que mostra todas as palavras adicionadas ao usuário

    def view(self):
        if lista == []:
            msgbox.showerror('Sem palavras','Não há palavras adicionadas')
        else:
            words = str(lista)
            msgbox.showinfo('Palavras',words)

# Roda o programa

root = Tk()
Janela(root)
root.mainloop()
