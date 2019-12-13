from views import Ui_MainWindow
from models import LogReader
from PyQt5 import QtCore, QtGui, QtWidgets


class MainController(object):
    def __init__(self, datapath):
        self.mainWindows = Ui_MainWindow()
        self.logreader = LogReader(datapath)
        self.list = self.logreader.loglist

    def populate_table(self):
        # self.mainWindows.tableModel.appendRow
        # self.mainWindows.tableModel.appendRow()
        loglenght = len(self.logreader.loglist)

        for i in range(0, loglenght):
            item = QtGui.QStandardItem(self.list[i].name)
            self.mainWindows.tableModel.setItem(i, 0, item)
            item = QtGui.QStandardItem(self.list[i].thread)
            self.mainWindows.tableModel.setItem(i, 1, item)
            item = QtGui.QStandardItem(self.list[i].date)
            self.mainWindows.tableModel.setItem(i, 2, item)
            item = QtGui.QStandardItem(self.list[i].time)
            self.mainWindows.tableModel.setItem(i, 3, item)
