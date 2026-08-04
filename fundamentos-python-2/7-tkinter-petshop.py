import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x700")
root.title("Pet Shop AuQmia - Sistema de Agendamento")
root.configure(bg="#F3F3F3")


# TÍTULO
rotulo = tk.Label(
    root,
    text="Agendamento de Serviços",
    font=("Arial", 20),
    bg="#3C28F0",
    fg="#FFFFFF"
)
rotulo.pack(fill=tk.X, pady=20)


# CAMPO NOME DO DONO
rotulo_nomeDono = tk.Label(
    root,
    text="Nome do Dono:",
    font=("Arial", 12),
    bg="#F3F3F3"
)
rotulo_nomeDono.place(x=50, y=100)

caixa_nomeDono = tk.Entry(root, font=("Arial", 12))
caixa_nomeDono.place(x=170, y=100, width=400, height=30)


# CAMPO NOME DO PET
rotulo_nomePet = tk.Label(
    root,
    text="Nome do Pet:",
    font=("Arial", 12),
    bg="#F3F3F3"
)
rotulo_nomePet.place(x=65, y=150)

caixa_nomePet = tk.Entry(root, font=("Arial", 12))
caixa_nomePet.place(x=170, y=150, width=400, height=30)


# CAMPO ESPÉCIE
rotulo_especie = tk.Label(
    root,
    text="Espécie:",
    font=("Arial", 12),
    bg="#F3F3F3"
)
rotulo_especie.place(x=100, y=200)

opcao = tk.StringVar(value="Cachorro")

tk.Radiobutton(
    root,
    text="Cachorro",
    value="Cachorro",
    variable=opcao,
    bg="#F3F3F3"
).place(x=170, y=200)

tk.Radiobutton(
    root,
    text="Gato",
    value="Gato",
    variable=opcao,
    bg="#F3F3F3"
).place(x=170, y=230)


# CAIXA DE OPÇÕES
frame_opcoes = tk.LabelFrame(
    root,
    text="Selecione os Serviços",
    font=("Arial", 12),
    bg="#F3F3F3"
)
frame_opcoes.place(x=115, y=280, width=500, height=150)


# CHECKBUTTONS
var_banho = tk.BooleanVar()
var_tosa = tk.BooleanVar()
var_unhas = tk.BooleanVar()

tk.Checkbutton(
    frame_opcoes,
    text="Banho",
    variable=var_banho,
    bg="#F3F3F3"
).place(x=20, y=20)

tk.Checkbutton(
    frame_opcoes,
    text="Tosa",
    variable=var_tosa,
    bg="#F3F3F3"
).place(x=20, y=60)

tk.Checkbutton(
    frame_opcoes,
    text="Corte de unhas",
    variable=var_unhas,
    bg="#F3F3F3"
).place(x=20, y=100)


# OBSERVAÇÃO
rotulo_observacao = tk.Label(
    root,
    text="Observações adicionais:",
    font=("Arial", 12),
    bg="#F3F3F3"
)
rotulo_observacao.place(x=50, y=455)

caixa_observacao = tk.Text(
    root,
    height=4,
    width=85,
    font=("Arial", 11)
)
caixa_observacao.place(x=50, y=485)

# FUNÇÃO AGENDAR
def agendar():
    if not caixa_nomeDono.get() or not caixa_nomePet.get():
        messagebox.showwarning("Atenção", "Preencha Nome do Dono e do Pet!")
        return
    servicos = []
    if var_banho.get(): servicos.append("Banho")
    if var_tosa.get(): servicos.append("Tosa")
    if var_unhas.get(): servicos.append("Unhas")
    msg = (f"Agendamento confirmado!\n"
           f"Dono: {caixa_nomeDono.get()}\n"
           f"Pet: {caixa_nomePet.get()} ({opcao.get()})\n"
           f"Serviços: {', '.join(servicos) or 'Nenhum'}\n"
           f"Observações: {caixa_observacao.get('1.0', tk.END).strip()}")
    messagebox.showinfo("Confirmado", msg)

# BOTÃO AGENDAR
botao_agendar = tk.Button(
    root,
    text="AGENDAR HORÁRIO",
    command=agendar,
    font=("Arial", 12, "bold"),
    bg="#77DD77",
    fg="white",
    activebackground="#66CC66",
    activeforeground="white",
    width=20,
    height=2
)
botao_agendar.place(x=300, y=580)


root.mainloop()