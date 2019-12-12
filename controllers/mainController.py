from views import Ui_MainWindow
from models import LogReader


class MainController(object):
    def __init__(self):
        self.mainWindows = Ui_MainWindow()
        self.logreader = LogReader()
