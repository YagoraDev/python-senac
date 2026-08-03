# Entrada de dados com Entry() - Cria um campo de entrada de texto para o usuário digitar informações.
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.geometry("300x200")
tk.Label(window,font=("Arial black", 12), text="Digite seu nome:").place(x=50, y=50)
caixa_texto = tk.Entry(window)
caixa_texto.place(x=50, y=100, width=200, height=30)
tk.Button(window, text="Enviar", command=lambda: messagebox.showinfo("Saudação", "Olá, " + caixa_texto.get() + "!")).place(x=100, y=150)
# Cria um botão que, quando clicado, exibe uma mensagem de saudação usando o texto digitado no campo de entrada
window.mainloop()