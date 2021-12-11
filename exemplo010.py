
import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.botao = QPushButton("Clique Aqui", self)
        self.botao.move(70, 140)
        self.botao.resize(100, 30)
        self.botao.setStyleSheet('QPushButton {background-color: #466321; font: bold; font-size: 15px;}')
        self.botao.clicked.connect(self.Botao_Click)

        self.linha = QLineEdit("", self)
        self.linha.move(20, 20)
        self.linha.resize(200, 20)
        self.linha.setMaxLength(15)
        self.linha.setPlaceholderText("Digite seu nome")

        self.label = QtWidgets.QLabel(self)
        self.label.move(20, 60)
        self.label.resize(200, 60)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(800,400,240,190)
        self.setWindowTitle("001_app")
        self.setFixedSize(240,190)
        self.setWindowIcon(QtGui.QIcon("python01.png"))
        self.show()

    def Botao_Click(self):
        self.label.setText(f"Olá {self.linha.text()}")
        self.label.setStyleSheet('QLabel {font: bold; font-size: 20px; color: "Green"}')


aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())






















