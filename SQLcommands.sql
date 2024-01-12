create database bd_python;

select * from products;
S


create table products (
nome varchar(30) NOT NULL,
codigo int(4) AUTO_INCREMENT PRIMARY KEY,
descricao varchar(30),
preco DECIMAL(10,2) NOT NULL
);

DROP DATABASE bd_python;
DROP TABLE products;

INSERT INTO products (nome, descricao, preco) VALUES 
  ('Camiseta', 'Camiseta de algodão preta', 19.99),
  ('Tênis', 'Tênis esportivo leve', 49.99),
  ('Notebook', 'Notebook de última geração', 899.99),
  ('Mouse', 'Mouse sem fio ergonômico', 29.99),
  ('Livro', 'Romance best-seller', 14.99);
