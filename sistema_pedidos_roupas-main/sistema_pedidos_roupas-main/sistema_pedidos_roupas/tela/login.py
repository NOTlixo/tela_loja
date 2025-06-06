import tkinter as tk
from tkinter import messagebox
from cadastro import TelaCadastro
from sistema_pedidos import SistemaPedidos
from database.conexao import conectar

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.title("Login do Cliente")
        self.root.geometry("300x250")

        tk.Label(root, text="Bem-vindo à Loja de Roupas", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Label(root, text="Usuário:").pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        tk.Label(root, text="Senha:").pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        tk.Button(root, text="Entrar", command=self.validar_login).pack(pady=10)
        tk.Button(root, text="Criar nova conta", command=self.abrir_cadastro).pack()

    def validar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            self.root.withdraw()
            root_principal = tk.Toplevel()
            SistemaPedidos(root_principal, self.root)
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def abrir_cadastro(self):
        cadastro_janela = tk.Toplevel(self.root)
        TelaCadastro(cadastro_janela)

if __name__ == "__main__":
    root = tk.Tk()
    TelaLogin(root)
    root.mainloop()