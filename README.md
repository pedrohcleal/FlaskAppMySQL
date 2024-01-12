**# Aplicativo Nunes Sports**

**## Visão geral**

Este aplicativo gerencia um catálogo de produtos usando um servidor web Flask e um banco de dados MySQL para armazenar informações sobre os produtos. Ele fornece os seguintes recursos:

* **Exibição de produtos:** Visualize uma lista de todos os produtos, com seus nomes, descrições e preços.
* **Criação de produtos:** Adicione novos produtos ao banco de dados.
* **Edição de produtos:** Modifique detalhes existentes dos produtos.
* **Remoção de produtos:** Remova produtos do banco de dados.

**## Instalação**

1. Certifique-se de ter Python, Flask e Flask-MySQLdb instalados.
2. Crie um banco de dados MySQL chamado `bd_python` com uma tabela chamada `products` contendo as seguintes colunas:
   * `codigo` (INT, chave primária)
   * `nome` (VARCHAR(50))
   * `descricao` (VARCHAR(255))
   * `preco` (DECIMAL(10,2))
3. Atualize a configuração do banco de dados em `main.py` com suas credenciais do MySQL:
   ```python
   app.config['MYSQL_HOST'] = 'seu_host_mysql'
   app.config['MYSQL_USER'] = 'seu_usuario_mysql'
   app.config['MYSQL_PASSWORD'] = 'sua_senha_mysql'
   ```

**## Uso**

1. Execute o aplicativo:
   ```bash
   python main.py
   ```
2. Acesse o aplicativo no seu navegador web em http://127.0.0.1:5000/.
3. Use o menu suspenso para selecionar a função desejada:
   * **Exibir Produtos:** Exibe a lista de produtos.
   * **Criar Produto:** Fornece campos para criar um novo produto.
   * **Editar Produto:** Permite editar um produto existente pelo ID.
   * **Excluir Produto:** Exclui um produto pelo ID.

**## Solução de problemas**

* Verifique se há mensagens de erro no console ao executar o aplicativo.
* Certifique-se de que seu banco de dados MySQL está em execução e acessível.
* Verifique se a configuração do banco de dados em `main.py` corresponde ao seu ambiente.

**## Contribuindo**

Sinta-se à vontade para contribuir para este projeto! Siga o fluxo de trabalho Git padrão para contribuir com alterações.

**Alterações feitas**

* **Título:** Alterado para "Aplicativo Nunes Sports" para refletir o nome da empresa.
* **Visão geral:** Adicionado um parágrafo explicando que o aplicativo usa um servidor web Flask e um banco de dados MySQL.
* **Instalação:** Adicionado um parágrafo explicando as etapas necessárias para instalar o aplicativo.
* **Uso:** Adicionado um parágrafo explicando como usar o menu suspenso para selecionar uma função.
* **Solução de problemas:** Adicionado um parágrafo fornecendo dicas para solucionar problemas comuns.
* **Contribuindo:** Adicionado um parágrafo convidando os usuários a contribuir com o projeto.

Além disso, foram feitas algumas alterações menores para melhorar a legibilidade e a clareza do texto.
