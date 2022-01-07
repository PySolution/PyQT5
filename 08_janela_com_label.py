import sys
from PyQt5 import QtWidgets, QtGui, QtCore


def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelLeft = QtWidgets.QLabel(windowExample)
    labelRight = QtWidgets.QLabel(windowExample)
    labelCenter = QtWidgets.QLabel(windowExample)
    labelLeft.setText('Alinhamento esquerdo')
    labelRight.setText('Alinhamento direito')
    labelCenter.setText('Alinhamento central')
    windowExample.setWindowTitle('Exemplo de alinhamento de Label')
    windowExample.setGeometry(100, 100, 350, 200)
    labelLeft.setFixedWidth(160)
    labelRight.setFixedWidth(160)
    labelCenter.setFixedWidth(160)
    labelLeft.setStyleSheet("border-radius: 7px;border: 1px solid black;")
    labelRight.setStyleSheet("border-radius: 0px;border: 2px solid black;")
    labelCenter.setStyleSheet("border-radius: 10px;border: 1px solid black;")
    labelLeft.setAlignment(QtCore.Qt.AlignLeft)
    labelRight.setAlignment(QtCore.Qt.AlignRight)
    labelCenter.setAlignment(QtCore.Qt.AlignCenter)
    labelLeft.move(100, 40)
    labelRight.move(100, 80)
    labelCenter.move(100, 120)

    windowExample.show()
    sys.exit(app.exec_())

basicWindow()


