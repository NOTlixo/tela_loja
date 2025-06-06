# Sistema de Controle de Pedidos - Loja de Roupas

Este é um sistema de controle de pedidos feito em Python utilizando Tkinter para a interface gráfica e SQLite como banco de dados. O sistema permite que usuários façam login, cadastrem pedidos de roupas e visualizem os pedidos feitos.

## Funcionalidades

- Login de usuário
- Cadastro de novos usuários
- Cadastro de pedidos com nome do cliente, tipo de roupa, tamanho, quantidade e preço
- Visualização dos pedidos cadastrados
- Resumo dos pedidos com total geral
- Atualização e remoção de pedidos
- Retorno para a tela de login

## Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/NOTlixo/Sistema_loja_de_roupas.git
   ```

2. Abra o projeto em um editor como PyCharm, VSCode ou outro de sua preferência.

3. Execute o arquivo principal da aplicação:

   O arquivo principal do projeto é o `tela_login.py`, que fica na pasta onde está a interface de login. É por ele que o sistema deve ser iniciado.

   Para rodar, use:
   ```bash
   python login.py
   ```

4. O sistema abrirá a tela de login. A partir dela você pode:
   - Entrar com um usuário existente
   - Criar uma nova conta
   - Após o login, acessar a tela de pedidos



## Requisitos

- Python 3.10 ou superior
- Bibliotecas padrão: tkinter, sqlite3, datetime

## Observações

- O banco de dados SQLite será criado automaticamente na primeira execução.
- Todas as interações são feitas através da interface gráfica (Tkinter).
- Recomendado executar o projeto em um ambiente virtual para evitar conflitos com outras bibliotecas.
