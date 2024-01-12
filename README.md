# Nunes Sports - Sistema de Gerenciamento de Produtos

Este é um simples sistema de gerenciamento de produtos desenvolvido em Python usando o framework Flask e MySQL como banco de dados.

## Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Flask
- Flask-MySQLdb
- MySQL Server

## Configuração do Banco de Dados

- Host: localhost
- Usuário: root
- Senha: root
- Banco de Dados: bd_python

## Execução

Execute o arquivo `main.py` para iniciar o servidor Flask. Abra o navegador e acesse `http://127.0.0.1:5000/` para utilizar o sistema.

## Funcionalidades

### 1. Exibir Produtos

- Acesse a página inicial para visualizar a lista de produtos cadastrados.

### 2. Criar Produto

- Selecione a opção "Criar Produto" no menu suspenso.
- Preencha os campos necessários e clique em "Confirmar" para adicionar um novo produto.

### 3. Editar Produto

- Selecione a opção "Editar Produto" no menu suspenso.
- Escolha o ID do produto a ser editado, preencha os novos valores e clique em "Confirmar" para salvar as alterações.

### 4. Deletar Produto

- Selecione a opção "Deletar Produto" no menu suspenso.
- Escolha o ID do produto a ser deletado e clique em "Confirmar" para remover o produto.

## Estrutura do Projeto

- `main.py`: Contém a lógica principal do sistema, incluindo rotas para exibir, criar, editar e deletar produtos.
- `index.html`: Página HTML para a interface do usuário, com funcionalidades dinâmicas usando JavaScript.

## Estilo Visual

A interface do usuário é simples e amigável, com uma tabela para exibir os produtos e formulários dinâmicos para criação, edição e exclusão.

## Observações

Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o aplicativo. Recomenda-se a utilização de ambientes virtuais para evitar conflitos de dependências.

Para quaisquer problemas ou dúvidas, entre em contato com o desenvolvedor.

**Desenvolvido por [Seu Nome]**
