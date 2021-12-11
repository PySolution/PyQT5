import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel, QPushButton

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 500
        self.largura = 350
        self.altura = 350
        self.titulo = "App Teste"
        #Usar self para o método ficar visível fora do construtor.
        self.label_1 = QLabel(self)
        self.label_1.resize(200, 25)
        self.label_1.setText("Olá, Tudo bem?")
        self.label_1.move(100, 100)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 20px; color: "red"}')
        botao = QPushButton("Clique aqui", self)
        botao.move(100, 200)
        botao.resize(150, 80)
        botao.clicked.connect(self.Clicar_Botao)
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def Clicar_Botao(self):
        print("Botão Clicado")
        self.label_1.setText("Botão Clicado")
        self.label_1.move(50, 60)
        self.label_1.resize(300, 100)
        self.label_1.setStyleSheet('QLabel {font: bold; font-size: 40px; color: "Green"}')

aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())


