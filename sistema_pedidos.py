import tkinter as tk
from tkinter import ttk, messagebox

class SistemaPedidos:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Pedidos - Loja de Roupas")
        self.root.geometry("400x300")
        self.pedidos = []

        tk.Label(root, text="Nome do Cliente:").pack()
        self.nome_entry = tk.Entry(root, width=40)
        self.nome_entry.pack()

        tk.Label(root, text="Tipo de Roupa:").pack()
        self.roupa_combobox = ttk.Combobox(root, values=["Camiseta", "Calça", "Vestido", "Jaqueta", "Saia"])
        self.roupa_combobox.pack()

        tk.Label(root, text="Tamanho:").pack()
        self.tamanho_combobox = ttk.Combobox(root, values=["PP", "P", "M", "G", "GG"])
        self.tamanho_combobox.pack()

        tk.Label(root, text="Quantidade:").pack()
        self.qtd_spinbox = tk.Spinbox(root, from_=1, to=100)
        self.qtd_spinbox.pack()

        tk.Button(root, text="Adicionar Pedido", command=self.adicionar_pedido).pack(pady=10)
        tk.Button(root, text="Ver pedidos", command=self.abrir_resumo_pedidos).pack()

    def adicionar_pedido(self):
        nome = self.nome_entry.get()
        roupa = self.roupa_combobox.get()
        tamanho = self.tamanho_combobox.get()
        qtd = self.qtd_spinbox.get()

        if not nome or not roupa or not tamanho or not qtd:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        pedido = f"{nome} - {qtd}x {roupa} (Tamanho: {tamanho})"
        self.pedidos.append(pedido)
        messagebox.showinfo("Sucesso", "Pedido adicionado com sucesso!")

        self.nome_entry.delete(0, tk.END)
        self.roupa_combobox.set('')
        self.tamanho_combobox.set('')
        self.qtd_spinbox.delete(0, tk.END)
        self.qtd_spinbox.insert(0, '1')

    def abrir_resumo_pedidos(self):
        ResumoPedidos(tk.Toplevel(self.root), self.pedidos)

class ResumoPedidos:
    def __init__(self, root, pedidos):
        self.root = root
        self.root.title("Resumo dos Pedidos")
        self.root.geometry("500x350")
        self.pedidos = pedidos

        tk.Label(root, text="Pedidos Realizados:", font=("Arial", 12, "bold")).pack(pady=10)

        self.listbox = tk.Listbox(root, width=70)
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.atualizar_listbox()

        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)

        tk.Button(frame_botoes, text="Editar", command=self.editar_pedido).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botoes, text="Remover", command=self.remover_pedido).pack(side=tk.LEFT, padx=5)

    def atualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for pedido in self.pedidos:
            self.listbox.insert(tk.END, pedido)

    def editar_pedido(self):
        selecionado = self.listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um pedido para editar.")
            return

        index = selecionado[0]
        pedido_antigo = self.pedidos[index]

        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Editar Pedido")

        tk.Label(nova_janela, text="Novo Pedido:").pack()
        entry = tk.Entry(nova_janela, width=60)
        entry.insert(0, pedido_antigo)
        entry.pack(pady=5)

        def salvar_edicao():
            novo_pedido = entry.get()
            if not novo_pedido:
                messagebox.showwarning("Aviso", "O pedido não pode estar vazio.")
                return
            self.pedidos[index] = novo_pedido
            self.atualizar_listbox()
            nova_janela.destroy()
            messagebox.showinfo("Sucesso", "Pedido editado com sucesso!")

        tk.Button(nova_janela, text="Salvar", command=salvar_edicao).pack(pady=10)

    def remover_pedido(self):
        selecionado = self.listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um pedido para remover.")
            return

        index = selecionado[0]
        confirm = messagebox.askyesno("Confirmação", "Deseja realmente remover o pedido?")
        if confirm:
            del self.pedidos[index]
            self.atualizar_listbox()
            messagebox.showinfo("Sucesso", "Pedido removido com sucesso!")
