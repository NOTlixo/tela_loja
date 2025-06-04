import tkinter as tk
from tkinter import ttk, messagebox
from database import operacoes
from database.tabela import criar_tabela_pedidos

criar_tabela_pedidos()

class SistemaPedidos:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Pedidos - Loja de Roupas")
        self.root.geometry("600x400")

        self.nome_label = tk.Label(root, text="Nome do Cliente:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(root, width=40)
        self.nome_entry.pack()

        self.roupa_label = tk.Label(root, text="Tipo de Roupa:")
        self.roupa_label.pack()
        self.roupa_combobox = ttk.Combobox(root, values=["Camiseta", "Calça", "Vestido", "Jaqueta", "Saia"])
        self.roupa_combobox.pack()

        self.tamanho_label = tk.Label(root, text="Tamanho:")
        self.tamanho_label.pack()
        self.tamanho_combobox = ttk.Combobox(root, values=["PP", "P", "M", "G", "GG"])
        self.tamanho_combobox.pack()

        self.qtd_label = tk.Label(root, text="Quantidade:")
        self.qtd_label.pack()
        self.qtd_spinbox = tk.Spinbox(root, from_=1, to=100)
        self.qtd_spinbox.pack()

        self.adicionar_btn = tk.Button(root, text="Adicionar Pedido", command=self.adicionar_pedido)
        self.adicionar_btn.pack(pady=10)

        self.lista_pedidos = tk.Listbox(root, width=80)
        self.lista_pedidos.pack(pady=10)

        self.carregar_pedidos()

    def adicionar_pedido(self):
       nome = self.nome_entry.get()
       roupa = self.roupa_combobox.get()
       tamanho = self.tamanho_combobox.get()
       qtd = self.qtd_spinbox.get()

       if not nome or not roupa or not tamanho or not qtd:
           messagebox.showwarning("Atenção", "Preencha todos os campos.")
           return
       try:
           operacoes.inserir_pedido(nome, roupa, tamanho, int(qtd))
       except Exception as e:
           messagebox.showerror("Erro", f"Erro as salvar no banco de dados: {e}")
           return

       self.carregar_pedidos()

       self.nome_entry.delete(0, tk.END)
       self.roupa_combobox.set('')
       self.tamanho_combobox.set('')
       self.qtd_spinbox.delete(0, tk.END)
       self.qtd_spinbox.insert(0, '1')


    def carregar_pedidos(self):
        self.lista_pedidos.delete(0, tk.END)
        pedidos = operacoes.listar_pedidos()
        for pedido in pedidos:
            cliente, produto, tamanho, qtd = pedido[1], pedido[2], pedido[3], pedido[4]
            texto = f"{cliente} - {qtd}x {produto} (Tamanho: {tamanho})"
            self.lista_pedidos.insert(tk.END, texto)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPedidos(root)
    root.mainloop()