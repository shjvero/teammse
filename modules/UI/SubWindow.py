import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class SubWindow(QWidget):
    def __init__(self, _path):
        super().__init__()
        self.path = _path

    def showUsnjrnl(self):
        print("Show $usnjrnl: " + self.path)
        self.initUI()

    def showMFT(self):
        print("Show $MFT: " + self.path)
        self.initUI()

    def showLogFile(self):
        print("Show $LogFile: " + self.path)
        self.initUI()

    def initUI(self):
        print("initUI")
