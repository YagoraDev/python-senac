from tkinter import messagebox # Importa a caixa de mensagem
import tkinter as tk

# Exemplo de janela com botões e caixa de mensagem
def clique():
    '''
    Função para exibir a caixa de mensagem e fechar a janelase o usuário clicar em "Sim"
    '''
    mensagem = messagebox.askquestion("fechar janela?", "Sim ou não?")
    if mensagem == "yes":
        janela.destroy()
  

def saudar():
    label_resultado.config(text="Óla! Bem-vindo ao sistema!")

root = tk.Tk()
root.title("Label e Button")
root.geometry("350x180")
janela = tk.Tk() # Cria a janela

# Label - exibir mensagem
label_titulo = tk.Label(root, text="Sistema de Exemplo",
                        font=("Arial", 14, "bold"), fg="#1A2E4A")
label_titulo.pack(pady=10)

# Resultado (Começa vazio)
label_resultado = tk.Label(root, text="", fg="#2563EB", font=("Arial", 11))
label_resultado.pack()

# Button - chama função ao clicar
btn = tk.Button(root, text="Clicar aqui", command=saudar,
                bg="#2563EB", fg="white", font=("Arial", 10, "bold"),
                padx=15, pady=5)
btn.pack(pady=10)

#Cria o botão e associa a função clique() ao evento clique
btn2 = tk.Button(janela,bg="#E02323", text="Fechar Janela",
                 pady=10, command=clique).pack(pady=20) 

root.mainloop()