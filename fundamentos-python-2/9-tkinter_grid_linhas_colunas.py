import tkinter as tk
root = tk.Tk()

root.title("Exemplo de Grid")

# Criando rótulos (labels) para cada célula da grade
rotulo1 = tk.Label(root, text="linha 0, coluna 0", bg="lightblue")
rotulo1.grid(row=0, column=0)

botao1 = tk.Button(root, text="linha 1, coluna 0", bg="lightgreen")
botao1.grid(row=1, column=0)

botao2 = tk.Button(root, text="linha 2, coluna 0", bg="lightyellow")
botao2.grid(row=2, column=0)

botao3 = tk.Button(root, text="linha 3, coluna 0", bg="lightpink")
botao3.grid(row=3, column=0)

bota4 = tk.Button(root, text="linha 0, coluna 1", bg="lightpink")
bota4.grid(row=0, column=1)

botao5 = tk.Button(root, text="linha 1, coluna 1", bg="lightgray")
botao5.grid(row=1, column=1)

botao6 = tk.Button(root, text="linha 2, coluna 1", bg="lightcoral")
botao6.grid(row=2, column=1)

botao7 = tk.Button(root, text="linha 3, coluna 1", bg="lightcyan")
botao7.grid(row=3, column=1)

botao8 = tk.Button(root, text="linha 0, coluna 2", bg="lightcyan")
botao8.grid(row=0, column=2)

botao9 = tk.Button(root, text="linha 1, coluna 2", bg="lightgoldenrod")
botao9.grid(row=1, column=2)

botao10 = tk.Button(root, text="linha 2, coluna 2", bg="lightseagreen")
botao10.grid(row=2, column=2)

botao11 = tk.Button(root, text="linha 3, coluna 2", bg="lightsteelblue")
botao11.grid(row=3, column=2)

root.mainloop()