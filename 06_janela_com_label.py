import sys
from PyQt5 import QtWidgets, QtGui

def basicWindow():
    app = QtWidgets.QApplication(sys.argv)
    windowExample = QtWidgets.QWidget()
    labelA = QtWidgets.QLabel(windowExample)
    labelB = QtWidgets.QLabel(windowExample)
    labelA.setText('Label Example')
    labelB.setPixmap(QtGui.QPixmap('python02.png'))
    windowExample.setWindowTitle('Label Example')
    windowExample.setGeometry(100, 100, 400, 400)
    labelA.move(100, 40)
    labelB.move(120, 120)
    windowExample.show()
    sys.exit(app.exec_())

basicWindow()
