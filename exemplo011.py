
import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import *


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.primeiraLabel()
        self.segundaLabel()
        self.primeiroBotao()
        self.segundoBotao()
        self.primeiraLinha()
        self.segundaLinha()
        self.terceiraLinha()
        self.listaGeral()
        self.CarregarJanela()



    def primeiraLabel(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.move(20, 20)
        self.label1.resize(200, 60)
        self.label1.setAlignment(QtCore.Qt.AlignLeft)
        self.label1.setText("Digite seus dados:")
        self.label1.setFont(QtGui.QFont("Arial", 12,
                                   QtGui.QFont.Black))

    def segundaLabel(self):
        label2 = QtWidgets.QLabel(self)
        label2.move(20, 210)
        label2.resize(200, 60)
        label2.setAlignment(QtCore.Qt.AlignLeft)
        label2.setText("Lista de informações")
        label2.setFont(QtGui.QFont("Arial", 12,
                                   QtGui.QFont.Black))

    def primeiroBotao(self):
        self.botao1 = QPushButton("Cadastrar", self)
        self.botao1.move(20, 140)
        self.botao1.resize(100, 30)
        self.botao1.clicked.connect(self.Botao_Cadastrar)

    def segundoBotao(self):
        self.botao2 = QPushButton("Limpar Lista", self)
        self.botao2.move(20, 450)
        self.botao2.resize(100, 30)
        self.botao2.clicked.connect(self.Botao_Limpar)

    def primeiraLinha(self):
        self.linha1 = QLineEdit("", self)
        self.linha1.move(20, 50)
        self.linha1.resize(400, 20)
        self.linha1.setMaxLength(50)
        self.linha1.setPlaceholderText("Digite seu nome")

    def segundaLinha(self):
        self.linha2 = QLineEdit("", self)
        self.linha2.move(20, 80)
        self.linha2.resize(100, 20)
        self.linha2.setMaxLength(3)
        self.linha2.setPlaceholderText("Digite sua idade")

    def terceiraLinha(self):
        self.linha3 = QLineEdit("", self)
        self.linha3.move(20, 110)
        self.linha3.resize(400, 20)
        self.linha3.setMaxLength(50)
        self.linha3.setPlaceholderText("Digite seu e-mail")

    def listaGeral(self):

        cadastros = [
            {'nome': "Maria", 'idade': "30", 'email': "maria@email.com"}
        ]

        self.lista = QTableWidget(self)
        self.lista.setRowCount(len(cadastros))
        self.lista.setColumnCount(3)
        self.lista.setHorizontalHeaderLabels(('Nome', 'Idade', 'E-mail'))
        #self.lista.setColumnWidth(0,120)
        #self.lista.setColumnWidth(1,50)
        self.lista.move(20, 240)
        self.lista.resize(400, 200)

        inserir_linha = 0

        for cadastro in cadastros:
            self.lista.setItem(inserir_linha, 0, QTableWidgetItem(str(cadastro['nome'])))
            self.lista.setItem(inserir_linha, 1, QTableWidgetItem(str(cadastro['idade'])))
            self.lista.setItem(inserir_linha, 2, QTableWidgetItem(str(cadastro['email'])))
            inserir_linha += 1

    def CarregarJanela(self):
        self.setGeometry(700,100,440,500)
        self.setWindowTitle("002_app")
        self.setFixedSize(440,500)
        self.setWindowIcon(QtGui.QIcon("python01.png"))
        self.show()

    def Botao_Cadastrar(self):
        nome = self.linha1.text()
        idade = self.linha2.text()
        email = self.linha3.text()

        if nome and idade is not None:
            contarLinha = self.lista.rowCount()
            self.lista.insertRow(contarLinha)
            self.lista.setItem(contarLinha, 0, QTableWidgetItem(nome))
            self.lista.setItem(contarLinha, 1, QTableWidgetItem(idade))
            self.lista.setItem(contarLinha, 2, QTableWidgetItem(email))

        self.linha1.setText("")
        self.linha2.setText("")
        self.linha3.setText("")

    def Botao_Limpar(self):
        self.lista.clearContents()
        self.lista.setRowCount(0)




aplicacao = QApplication(sys.argv)
j = Janela()
j.show()
sys.exit(aplicacao.exec_())

















