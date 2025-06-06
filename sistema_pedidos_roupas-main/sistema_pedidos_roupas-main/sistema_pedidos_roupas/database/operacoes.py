from database.conexao import conectar


def inserir_pedido(cliente, produto, tamanho, quantidade, preco_unitario, data_pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pedidos (cliente, produto, tamanho, quantidade, preco_unitario, data_pedido)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (cliente, produto, tamanho, quantidade, preco_unitario, data_pedido))
    conn.commit()
    conn.close()

def listar_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return pedidos

def atualizar_pedido(id, cliente, produto, tamanho, quantidade, preco_unitario, data_pedido):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE pedidos
        SET cliente=?, produto=?, tamanho=?, quantidade=?, preco_unitario=?, data_pedido=?
        WHERE id=?
    """, (cliente, produto, tamanho, quantidade, preco_unitario, data_pedido, id))
    conn.commit()
    conn.close()


def remover_pedido(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id=?", (id,))
    conn.commit()
    conn.close()