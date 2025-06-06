import tkinter as tk
from tkinter import ttk, messagebox
from database import operacoes
from database.tabela import criar_tabela_pedidos, criar_tabela_usuario
from datetime import datetime


criar_tabela_pedidos()
criar_tabela_usuario()

class SistemaPedidos:
    def __init__(self, root, tela_login):
        self.root = root
        self.tela_login = tela_login
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

        self.roupa_combobox.bind("<<ComboboxSelected>>", self.atualizar_preco)

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

        self.resumo_btn = tk.Button(root, text="Resumo de Pedidos", command=self.abrir_resumo_pedidos)
        self.resumo_btn.pack(pady=5)

        self.atualizar_btn = tk.Button(root, text="Atualizar Pedido", command=self.atualizar_pedido)
        self.atualizar_btn.pack(pady=5)

        self.remover_btn = tk.Button(root, text="Remover Pedido", command=self.remover_pedido)
        self.remover_btn.pack(pady=5)

        self.lista_pedidos = tk.Listbox(root, width=80)
        self.lista_pedidos.pack(pady=10)

        self.precos_roupas = {
            "Camiseta": 39.90,
            "Calça": 89.90,
            "Vestido": 129.90,
            "Jaqueta": 159.90,
            "Saia": 59.90
        }

        self.sair_btn = tk.Button(root, text="Sair", command=self.voltar_para_login)
        self.sair_btn.pack(pady=10)

        self.carregar_pedidos()



    def adicionar_pedido(self):
       nome = self.nome_entry.get()
       roupa = self.roupa_combobox.get()
       tamanho = self.tamanho_combobox.get()
       qtd = self.qtd_spinbox.get()

       if not nome or not roupa or not tamanho or not qtd:
           messagebox.showwarning("Atenção", "Preencha todos os campos.")
           return

       preco_unitario = self.precos_roupas.get(roupa, 49.99)
       data_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

       operacoes.inserir_pedido(nome, roupa, tamanho, int(qtd), preco_unitario, data_pedido)

       self.nome_entry.delete(0, tk.END)
       self.roupa_combobox.set('')
       self.tamanho_combobox.set('')
       self.qtd_spinbox.delete(0, tk.END)
       self.qtd_spinbox.insert(0, '1')

       messagebox.showinfo("Pedido Adicionado", "Pedido salvo com sucesso no banco de dados!")
       self.carregar_pedidos()


    def carregar_pedidos(self):
        self.lista_pedidos.delete(0, tk.END)
        pedidos = operacoes.listar_pedidos()

        for pedido in pedidos:
            id, cliente, produto, tamanho, qtd, preco_unitario, data_pedido = pedido
            total = qtd * preco_unitario
            texto = f"{id} - {cliente} - {qtd}x {produto} (Tam: {tamanho}) - R${total:.2f} em {data_pedido}"
            self.lista_pedidos.insert(tk.END, texto)

    def abrir_resumo_pedidos(self):
        pedidos = operacoes.listar_pedidos()

        resumo_janela = tk.Toplevel()
        resumo_janela.title("Resumo de Pedidos")

        tk.Label(resumo_janela, text="Resumo de Pedidos", font=("Arial", 14, "bold")).pack(pady=10)

        total_geral = 0.0

        for pedido in pedidos:
            id, cliente, produto, tamanho, qtd, preco_unitario, data_pedido = pedido
            total = qtd * preco_unitario
            total_geral += total

            texto = f"Cliente: {cliente} | Produto: {produto} | Tamanho: {tamanho} | Qtd: {qtd} | " \
                f"Preço Unit.: R${preco_unitario:.2f} | Total: R${total:.2f} | Data: {data_pedido}"
            tk.Label(resumo_janela, text=texto, anchor="w", justify="left").pack(fill='x', padx=10, pady=2)

        tk.Label(resumo_janela, text=f"Total Geral: R${total_geral:.2f}", font=("Arial", 12, "bold")).pack(pady=10)

    def atualizar_pedido(self):
        try:
            selected_index = self.lista_pedidos.curselection()[0]
            pedido = self.lista_pedidos.get(selected_index)
            id_pedido = int(pedido.split(" - ")[0])

            pedidos = operacoes.listar_pedidos()
            pedido_escolhido = next(p for p in pedidos if p[0] == id_pedido)

            self.abrir_janela_edicao(pedido_escolhido)

        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um pedido para atualizar.")

    def abrir_janela_edicao(self, pedido):
        id_pedido, cliente, produto, tamanho, quantidade, preco_unitario, data_pedido = pedido

        edicao = tk.Toplevel(self.root)
        edicao.title(f"Editar Pedido ID {id_pedido}")
        edicao.geometry("300x350")

        tk.Label(edicao, text="Cliente:").pack()
        entry_cliente = tk.Entry(edicao)
        entry_cliente.insert(0, cliente)
        entry_cliente.pack()

        tk.Label(edicao, text="Produto:").pack()
        entry_produto = tk.Entry(edicao)
        entry_produto.insert(0, produto)
        entry_produto.pack()

        tk.Label(edicao, text="Tamanho:").pack()
        entry_tamanho = tk.Entry(edicao)
        entry_tamanho.insert(0, tamanho)
        entry_tamanho.pack()

        tk.Label(edicao, text="Quantidade:").pack()
        entry_qtd = tk.Entry(edicao)
        entry_qtd.insert(0, str(quantidade))
        entry_qtd.pack()

        tk.Label(edicao, text="Preço Unitário:").pack()
        entry_preco = tk.Entry(edicao)
        entry_preco.insert(0, str(preco_unitario))
        entry_preco.pack()

        tk.Label(edicao, text="Data do Pedido (YYYY-MM-DD):").pack()
        entry_data = tk.Entry(edicao)
        entry_data.insert(0, data_pedido)
        entry_data.pack()

        def salvar_edicao():
            novo_cliente = entry_cliente.get()
            novo_produto = entry_produto.get()
            novo_tamanho = entry_tamanho.get()
            nova_qtd = int(entry_qtd.get())
            novo_preco = float(entry_preco.get())
            nova_data = entry_data.get()

            operacoes.atualizar_pedido(id_pedido, novo_cliente, novo_produto, novo_tamanho, nova_qtd, novo_preco,
                                       nova_data)
            messagebox.showinfo("Sucesso", "Pedido atualizado com sucesso.")
            edicao.destroy()
            self.carregar_pedidos()

        tk.Button(edicao, text="Salvar Alterações", command=salvar_edicao).pack(pady=20)

    def remover_pedido(self):
        try:
            selected_index = self.lista_pedidos.curselection()[0]
            pedido = self.lista_pedidos.get(selected_index)

            id_pedido = int(pedido.split(" - ")[0])

            confirmar = messagebox.askyesno("Confirmar Remoção", f"Deseja remover o pedido ID {id_pedido}?")

            if confirmar:
                operacoes.remover_pedido(id_pedido)
                messagebox.showinfo("Remover Pedido", "Pedido removido com sucesso!")
                self.carregar_pedidos()
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um pedido para remover.")

    def atualizar_preco(self, event):
        roupa = self.roupa_combobox.get()
        preco = self.precos_roupas.get(roupa, 0)
        messagebox.showinfo("Preço", f"O preço da {roupa} é R${preco:.2f}")

    def voltar_para_login(self):
        self.root.destroy()
        if self.tela_login:
            self.tela_login.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaPedidos(root, None)
    root.mainloop()