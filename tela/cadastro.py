import tkinter as tk
from tkinter import messagebox

class TelaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Novo Cliente")
        self.root.geometry("300x300")

        tk.Label(root, text="Cadastro de Cliente", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(root, text="Nome completo:").pack()
        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        tk.Label(root, text="Usuário:").pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        tk.Label(root, text="Senha:").pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        tk.Label(root, text="Confirmar senha:").pack()
        self.entry_confirma = tk.Entry(root, show="*")
        self.entry_confirma.pack()

        tk.Button(root, text="Cadastrar", command=self.cadastrar).pack(pady=10)

    def cadastrar(self):
        nome = self.entry_nome.get()
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        confirma = self.entry_confirma.get()

        if not nome or not usuario or not senha or not confirma:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")
            return

        if senha != confirma:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        try:
            with open("clientes.txt", "r") as file:
                for linha in file:
                    if usuario == linha.strip().split(";")[0]:
                        messagebox.showerror("Erro", "Usuário já existe.")
                        return
        except FileNotFoundError:
            pass

        with open("clientes.txt", "a") as file:
            file.write(f"{usuario};{senha};{nome}\n")

        messagebox.showinfo("Sucesso", f"Cliente '{nome}' cadastrado com sucesso!")
        self.root.destroy()