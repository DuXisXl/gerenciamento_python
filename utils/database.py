import sqlite3

class DataBase():
    def __init__(self, name = "system.db") -> None:
        self.name = name

    def conectar(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

    def create_table_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS users (
                               id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                               nome_usuario TEXT NOT NULL,
                               usuario TEXT UNIQUE NOT NULL,
                               senha TEXT NOT NULL,
                               id_acesso INTEGER DEFAULT 1,
                               id_status_bloqueio INTEGER DEFAULT 1
                           );
                           """)
        except AttributeError:
            print('Faça a conexão primeiramente.')

    def create_table_produtos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS produtos (
                               id_produto INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                               nome_produto TEXT NOT NULL,
                               descricao_produto TEXT NOT NULL,
                               quantidade TEXT NOT NULL,
                               valor_produto INTEGER NOT NULL
                           );
                           """)
        except AttributeError:
            print('Faça a conexão primeiramente.')

    def insert_produtos(self, nome_produto, descricao_produto, quantidade, valor_produto):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           
                           INSERT INTO produtos(nome_produto, descricao_produto, quantidade, valor_produto)
                           VALUES (?, ?, ?, ?)
                           
                           """, (nome_produto, descricao_produto, quantidade, valor_produto))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão primeiro")

    def insert_users(self, nome_usuario, usuario, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           
                           INSERT INTO users(nome_usuario, usuario, senha)
                           VALUES (?,?,?)
                           
                           """,(nome_usuario, usuario, senha))
            self.connection.commit()
        except AttributeError:
            print('Faça a conexão primeiro.')

    def insert_pagamento(self, id_usuario, id_pagamento, valor, descricao, status, data_mili):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           
                           INSERT INTO pagamentos(id_usuario, id_pagamento, valor, descricao, status, data_mili)
                           VALUES (?, ?, ?, ?, ?, ?)
                           
                           """, (id_usuario, id_pagamento, valor, descricao, status, data_mili))
            self.connection.commit()
        except AttributeError:
            print("Faça a conexão primeiro")

    def check_user(self, usuario, senha):
        try:
            cursor = self.connection.cursor()
            login = cursor.execute("""
                                   
                                  SELECT *
                                  FROM users
                                  WHERE usuario = (?) AND senha = (?)
                                  
                                  """,(usuario, senha))
            if login.fetchone() is not None:
                return True
            else:
                return False
        except AttributeError:
            print('Faça a conexão primeiro.')

    def create_table_pagamentos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS pagamentos (
                               id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                               id_pagamento INTEGER NOT NULL,
                               valor INTEGER NOT NULL,
                               descricao TEXT NOT NULL,
                               status TEXT NOT NULL,
                               data_mili INTEGER NOT NULL
                           );
                           """)
        except AttributeError:
            print('Faça a conexão primeiramente.')

    def buscar_pagamento(self, id_usuario):
        try:
            cursor = self.connection.cursor()
            pagamentos = cursor.execute("""
                                   
                                  SELECT *
                                  FROM pagamentos
                                  WHERE id_usuario = (?)
                                  
                                  """,(id_usuario))
            # Obtém os nomes das colunas
            columns = [column[0] for column in cursor.description]
            
            # Obtem todas as linhas da coluna
            rows = cursor.fetchall()
            
            # Cria uma lista de dicionários para representar os resultados
            results = []
            for row in rows:
                result = {}
                for i, value in enumerate(row):
                    result[columns[i]] = value
                results.append(result)
            return results
        except AttributeError:
            print('Faça a conexão primeiro')

if __name__ == '__main__':
    db = DataBase()
    db.conectar()
    db.create_table_pagamentos()
    db.create_table_produtos()
    db.close_connection()
