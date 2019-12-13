"""
Main description
"""
import sys
from models import LogReader
from views import Ui_MainWindow
from controllers import MainController
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

# MAIN WINDOWS
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
# ui.setupUi(MainWindow)
MainWindow.show()
# path = ui.open_dialog_box()
# ctrl = MainController(path)
# ctrl.populate_table()


sys.exit(app.exec_())
