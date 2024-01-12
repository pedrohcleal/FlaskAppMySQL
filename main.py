from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
import logging

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bd_python'

mysql = MySQL(app)

@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM products")
        data = cur.fetchall()
        cur.close()
        return render_template('index.html', data=data)
    except Exception as e:
        print(f"Erro na consulta SQL: {str(e)}")
        return "Erro ao acessar o banco de dados"

@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':
        nome = request.json['nome']
        descricao = request.json['descricao']
        preco = request.json['preco']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO products (nome, descricao, preco) VALUES (%s, %s, %s)", (nome, descricao, preco))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Produto criado com sucesso'})
    return jsonify({'message': 'Método não permitido'}), 405


@app.route('/edit', methods=['POST'])
def edit():
    if request.method == 'POST':
        id_edit = request.json['id']
        nome_edit = request.json['nome']
        descricao_edit = request.json['descricao']
        preco_edit = request.json['preco']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE products SET nome=%s, descricao=%s, preco=%s WHERE codigo=%s", (nome_edit, descricao_edit, preco_edit, id_edit))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Produto editado com sucesso'})
    return jsonify({'message': 'Método não permitido'}), 405


@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        id_delete = request.json['id']
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM products WHERE codigo=%s", [id_delete])
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Produto deletado com sucesso'})
    return jsonify({'message': 'Método não permitido'}), 405


if __name__ == '__main__':
    app.run(debug=True)
