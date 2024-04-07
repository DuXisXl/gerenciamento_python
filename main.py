from PySide6.QtWidgets import(QApplication, QFileDialog, QMainWindow, QWidget, QMessageBox, QTreeWidgetItem)
from PySide6 import QtCore
from design.ui_login import Ui_Login
from design.ui_main import Ui_MainWindow
import sys
from utils.database import DataBase
import pandas as pd
import sqlite3


class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do Sistema")

        self.btn_login.clicked.connect(self.checkLogin)

    def checkLogin(self):
        db = DataBase()
        db.conectar()
        autenticado = db.check_user(self.txt_login.text(), self.txt_password.text())
        if autenticado == True:
            main = MainWindow()
            main.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'Usuario ou senha invalidos \n \n Tentativas: {self.tentativas +1} de 3')
                msg.setWindowTitle("Erro ao acessar")
                msg.exec_()
                self.tentativas += 1
            if self.tentativas == 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'Reinicie o programa e tente novamente!')
                msg.setWindowTitle("Erro ao acessar")
                msg.exec_()
                db.close_connection()
                sys.exit(5)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")

        # Paginas do sistema

        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_pg_import.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_import))
        self.btn_cadastrar.clicked.connect(self.criar_usuario)
        self.btn_insert_produto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro_produto))
        self.btn_cadastrar_produto.clicked.connect(self.inserir_produto)
        self.table_estoque()

    def criar_usuario(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("As senhas não conferem")
            msg.setWindowTitle("Senhas Divergentes")
            msg.exec_()
            return None

        nome_usuario = self.txt_nome.text()
        usuario = self.txt_usuario.text()
        senha = self.txt_senha.text()

        db = DataBase()
        db.conectar()
        db.insert_users(nome_usuario, usuario, senha)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cadastro Criado com sucesso!")
        msg.setWindowTitle("Cadastro de Usuario")
        msg.exec_()

    def inserir_produto(self):
        nome_produto = self.nome_produto.text()
        descricao_produto = self.descricao_produto.text()
        quantidade = self.quantidade.text()
        valor_produto = self.valor_produto.text()

        db = DataBase()
        db.conectar()
        db.insert_produtos(nome_produto, descricao_produto, quantidade, valor_produto)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Produto Cadastrado com Sucesso!")
        msg.setWindowTitle("Cadastro Produto")
        msg.exec_()
        self.tw_estoque.clear()
        self.table_estoque()

    def table_estoque(self):
        self.tw_estoque.setStyleSheet(u" QHeaderView{ color:black }; color:#fff; font-size:15px;")

        cn = sqlite3.connect('system.db')
        result = pd.read_sql_query("SELECT * FROM produtos WHERE quantidade <> 0", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            i = list(map(str, i))
            ultimo_item = i[-1]
            ultimo_item_formatado = 'R$ {:,.2f}'.format(float(ultimo_item)).replace('.', ',').replace(',', '.', 1)
            i[-1] = ultimo_item_formatado
            # Faz o check no produto e para adicionar um nivel.
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.tw_estoque, i)
                self.campo.setCheckState(0, QtCore.Qt.CheckState.Unchecked)

            self.x = i[0]

        self.tw_estoque.setSortingEnabled(True)

        for i in range(1, 15):
            self.tw_estoque.resizeColumnToContents(i)

    def table_saida(self):
        pass

    def table_geral(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()