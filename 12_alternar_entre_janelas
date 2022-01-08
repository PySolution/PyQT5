

# ALTERNAR ENTRE 2 JANELAS.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QTableWidget, QTableWidgetItem

#CLASSE REFERENTE A SEGUNDA JANELA:
class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.listaGeral()
        self.carregarJanela2()

    #CARACTERÍSTICAS DA SEGUNDA JANELA:
    def carregarJanela2(self):
        self.setGeometry(1200,100,440,500)
        self.setWindowTitle("Janela 2")
        self.setFixedSize(440,500)

    #EVENTO PARA RETORNAR A PRIMEIRA JANELA
    #APÓS CLICAR NO BOTÃO DE FECHAMENTO DA JANELA ATUAL
    def closeEvent(self, event):
        self.retornaJanela1 = TelaPrincipal()
        self.retornaJanela1.show()
        event.accept()

    #CARACTERÍSTICAS DA TABELA DE VISUALIZAÇÃO DOS DADOS
    def listaGeral(self):
        self.lista = QTableWidget(self)
        self.lista.setColumnCount(4)
        self.lista.setHorizontalHeaderLabels(('ID','Nome', 'Idade', 'E-mail'))
        self.lista.setColumnWidth(0,120)
        self.lista.setColumnWidth(1,50)
        self.lista.move(20, 50)
        self.lista.resize(400, 400)



#CLASSE REFERENTE A JANELA PRINCIPAL
class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.jan2 = Janela2()
        self.primeiroBotao()
        self.carregarJanela()

#CARACTERÍSTICAS DA PRIMEIRA JANELA
    def carregarJanela(self):
        self.setGeometry(700,200,300,200)
        self.setWindowTitle("Janela1")
        self.setFixedSize(300,200)

#CARACTERÍSTICAS DO BOTÃO
    def primeiroBotao(self):
        self.botao1 = QPushButton("Visualizar Dados", self)
        self.botao1.move(20, 20)
        self.botao1.resize(100, 30)
        self.botao1.clicked.connect(self.mudarJanela)

#FUNÇÃO A SER EXECUTADA AO CLICAR O BOTÃO
    def mudarJanela(self):
        self.jan2.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela1 = TelaPrincipal()
    tela1.show()
    sys.exit(app.exec_())


