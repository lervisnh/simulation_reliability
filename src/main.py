from widgets import MainApp, LoginPage
from PyQt5 import QtWidgets, QtCore, QtGui
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    m = MainApp()
    l = LoginPage(parent=m)
    l.show()
    sys.exit(app.exec_())
