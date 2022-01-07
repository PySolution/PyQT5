
import sys
from PyQt5 import QtWidgets

def janelaBasica():
    app = QtWidgets.QApplication(sys.argv)
    janelaExemplo = QtWidgets.QWidget()
    janelaExemplo.setWindowTitle('Exemplo de Janela Básica')
    janelaExemplo.show()
    sys.exit(app.exec_())

janelaBasica()
