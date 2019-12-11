"""
Main description
"""
import sys
from models import LogReader
from views import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

# MAIN WINDOWS
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


sys.exit(app.exec_())
