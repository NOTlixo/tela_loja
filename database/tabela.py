from database.conexao import conectar

def criar_tabela_pedidos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                produto TEXT NOT NULL,
                tamanho TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco_unitario REAL NOT NULL,
                data_pedido TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()