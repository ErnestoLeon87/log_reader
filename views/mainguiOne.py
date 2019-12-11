# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from models import Log


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1068, 663)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        # self.tableWidget.setGeometry(QtCore.QRect(20, 50, 1031, 561))
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(0)

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 1031, 561))
        self.tableView.setObjectName("tableView")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 10, 91, 21))

        font = QtGui.QFont()
        font.setPointSize(18)

        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(lambda: self.open_dialog_box())

        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionClose.triggered.connect(lambda: self.exit_app())

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.path = ""

        # lgreader = LogReader()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "ErrorList"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindows", "Ctr+O"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    def open_dialog_box(self):
        file = QtWidgets.QFileDialog.getOpenFileName()
        self.path = file[0]
        print(self.path)

    def exit_app(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        sys.exit(app.exec_())

    def populate_list(self):
        pass
