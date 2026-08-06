import tkinter as tk
root = tk.Tk()
root.title("Formulário de Cadastro")
# row=linha, column=coluna (começa do 0)
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=8, sticky="e") # Opções de alinhamento: n, s, e, w (norte, sul, leste, oeste)

tk.Entry(root, width=25).grid(row=0, column=1, padx=10, pady=8)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=8, sticky="e")

tk.Entry(root, width=25).grid(row=1, column=1, padx=10, pady=8)
tk.Label(root, text="Telefone:").grid(row=2, column=0, padx=10, pady=8, sticky="e")

tk.Entry(root, width=25).grid(row=2, column=1, padx=10, pady=8)
# Columnspan: ocupa 2 colunas
tk.Button(root, text="Cadastrar", width=15).grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()