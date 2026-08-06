import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

produtos = [
    {"nome": "Nootbook", "cat":"Notebooks", "preco": 3299.90,"estoque": 5},
    {"nome": "Mouse", "cat":"Periféricos", "preco": 79.90, "estoque": 15},
    {"nome": "Teclado", "cat":"Periféricos", "preco": 149.90, "estoque": 10},
    {"nome": "Monitor", "cat":"Monitores", "preco": 899.90, "estoque": 7},
    {"nome": "Impressora", "cat":"Periféricos", "preco": 499.90, "estoque": 3},
    {"nome": "Cadeira Gamer", "cat":"Móveis", "preco": 1299.90, "estoque": 2}
]

# Temas = ["superhero", "flatly", "darkly", "cosmo", "cyborg", "minty", "pulse", "sandstone", "simplex", "sketchy", "slate", "solar", "spacelab", "united"]
root = tb.Window(themename="lumen")
root.title("TechStore - Catálago")
root.geometry("600x430")

# --- Filtros ------------------------------------------
frame_filtro = tk.Frame(root, bg="#F1F5F9", pady=8)
frame_filtro.pack(fill="x")

tk.Label(frame_filtro, text="Buscar:", bg="#F1F5F9").pack(side="left", padx=8)
entry_busca = tk.Entry(frame_filtro, width=20)
entry_busca.pack(side="left", padx=5)

cats = ["Todos"] + sorted({p["cat"] for p in produtos})
var_cat = tk.StringVar(value="Todos")
ttk.Combobox(frame_filtro, textvariable=var_cat, values=cats, state="readonly", width=14).pack(side="left", padx=8)
tk.Button(frame_filtro, text="Filtrar", command=lambda: filtrar()).pack(side="left", padx=5)

# -- Tabela (Treeview) ------------------------------------------
cols = ("Produto", "Categoria", "Preço", "Estoque")
tree = ttk.Treeview(root, columns=cols, show="headings", height=15)
for c in cols:
    tree.heading(c, text=c)
    tree.column(c, width=130 if c=="Produto" else 100, anchor="c" if c=="Estoque" else "w")
tree.pack(fill="x", padx=10, pady=8)

def popular(lista):
    tree.delete(*tree.get_children())
    for p in lista:
        tree.insert("", "end", values=(p["nome"], p["cat"], f"R$ {p['preco']:.2f}", p["estoque"]))

def filtrar():
    termo = entry_busca.get().lower()
    cat = var_cat.get()
    res = [p for p in produtos
           if termo in p["nome"].lower()
           and (cat=="Todos" or p["cat"]==cat)]
    popular(res)

popular(produtos) # Carrega todos ao reiniciar

# -- Rodapé ------------------------------------------
label_info = tk.Label(root, text="Selecione um produto para ver detalhes", fg="gray", font=("Arial", 9))
label_info.pack(pady=4)

def on_select(event):
    sel = tree.selection()
    if sel:
        vals = tree.item(sel[0], "values")
        label_info.config(text=f" {vals[0]} | {vals[1]} | {vals[2]} | Estoque: {vals[3]} un.")

tree.bind("<<TreeviewSelect>>", on_select)
root.mainloop()