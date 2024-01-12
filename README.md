 **# Nunes Sports Application**

**## Overview**

This application manages a product catalog using a Flask web server and a MySQL database to store product information. It provides the following features:

* **Displaying products:** View a list of all products with their names, descriptions, and prices.
* **Creating products:** Add new products to the database.
* **Editing products:** Modify existing product details.
* **Deleting products:** Remove products from the database.

**## Installation**

1. Ensure you have Python, Flask, and Flask-MySQLdb installed.
2. Create a MySQL database named `bd_python` with a table named `products` containing the following columns:
   * `codigo` (INT, primary key)
   * `nome` (VARCHAR(50))
   * `descricao` (VARCHAR(255))
   * `preco` (DECIMAL(10,2))
3. Update the database configuration in `main.py` with your MySQL credentials:
   ```python
   app.config['MYSQL_HOST'] = 'your_mysql_host'
   app.config['MYSQL_USER'] = 'your_mysql_user'
   app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
   ```

**## Usage**

1. Run the application: 
   ```bash
   python main.py
   ```
2. Access the application in your web browser at http://127.0.0.1:5000/.
3. Use the dropdown menu to select the desired function:
   * **Exibir Produtos:** Displays the product list.
   * **Criar Produto:** Provides fields to create a new product.
   * **Editar Produto:** Allows editing an existing product by ID.
   * **Deletar Produto:** Deletes a product by ID.

**## Troubleshooting**

* Check for any error messages in the console when running the application.
* Ensure your MySQL database is running and accessible.
* Verify that the database configuration in `main.py` matches your environment.

**## Contributing**

Feel free to contribute to this project! Please follow the standard Git workflow for contributing changes.
