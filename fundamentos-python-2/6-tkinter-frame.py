import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
tk.LabelFrame(root, text="Opções").place(x=5, y=10, width=250, height=100)
tk.Checkbutton(root, text="Opção 1").place(x=10, y=30)
tk.Checkbutton(root, text="Opção 2").place(x=10, y=50)
tk.Checkbutton(root, text="Opção 3").place(x=10, y=70)

opcao = tk.IntVar()

tk.Radiobutton(root, text="Opção A", value=1, variable=opcao).place(x=150, y=30)
tk.Radiobutton(root, text="Opção B", value=2, variable=opcao).place(x=150, y=50)
tk.Radiobutton(root, text="Opção C", value=3, variable=opcao).place(x=150, y=70)

tk.Label(root, text="Observação:").place(x=10, y=120)
tk.Text(root, height=5, width=30).place(x=10, y=150)
root.mainloop()