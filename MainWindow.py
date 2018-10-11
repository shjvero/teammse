import sys

import qdarkstyle
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from modules.UI.MenuBar import MenuBar
from modules.UI.StatusBar import StatusBar
from modules.UI.PrototpyeTable import PrototypeTable

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = self.width()
        self.h = self.height()
        self.initUI()

    def initUI(self):
        # 기본 설정
        self.setWindowTitle("Monkey Spanner")
        self.setWindowIcon(QIcon("logo.jpg"))
        self.setMinimumSize(self.width(), self.height())
        self.setMenuBar(MenuBar())
        self.setStatusBar(StatusBar())

        self.layout = QVBoxLayout()
        groupBox = QGroupBox("Select Software", self)
        radioLayout = QHBoxLayout()
        groupBox.setLayout(radioLayout)
        groupBox.move(10, 20)
        groupBox.resize(self.w * 2, 65)
        self.btnFlash = QRadioButton('Adobe Flash Player', self)
        self.btnFlash.toggled.connect(lambda: self.toggledRadioBtn(self.btnFlash))
        radioLayout.addWidget(self.btnFlash)
        self.btnHWP = QRadioButton('HWP')
        self.btnHWP.toggled.connect(lambda: self.toggledRadioBtn(self.btnHWP))
        radioLayout.addWidget(self.btnHWP)
        self.btnIE = QRadioButton('Internet Explorer')
        self.btnIE.setChecked(True)
        self.btnIE.toggled.connect(lambda: self.toggledRadioBtn(self.btnIE))
        radioLayout.addWidget(self.btnIE)
        self.btnOffice = QRadioButton('MS-Office')
        self.btnOffice.toggled.connect(lambda: self.toggledRadioBtn(self.btnOffice))
        radioLayout.addWidget(self.btnOffice)
        self.btnPDF = QRadioButton('PDF')
        self.btnPDF.toggled.connect(lambda: self.toggledRadioBtn(self.btnPDF))
        radioLayout.addWidget(self.btnPDF)
        self.layout.addWidget(groupBox)

        # 검색 기능
        self.search = QLineEdit(self)
        self.search.move(10, 100)
        self.search.setFixedWidth(groupBox.width())
        self.search.setPlaceholderText("Filtering...")
        self.search.editingFinished.connect(self.enterPressed)
        self.search.textChanged.connect(self.textChanged)
        self.layout.addWidget(self.search)

        # 테이블 기능
        self.createTable()
        self.setLayout(self.layout)

    def toggledRadioBtn(self, b):
        msg = b.text()
        if self.btnFlash.isChecked():
            print(msg + " is checked")
        elif self.btnHWP.isChecked():
            print(msg + " is checked")
        elif self.btnIE.isChecked():
            print(msg + " is checked")
        elif self.btnOffice.isChecked():
            print(msg + " is checked")
        elif self.btnPDF.isChecked():
            print(msg + " is checked")
        self.statusBar().showMessage(msg + " is checked")

    def textChanged(self):
        print("Text Changed: " + self.search.text())

    def enterPressed(self):
        print("Entered: " + self.search.text())

    def createTable(self):
        self.table = QTableWidget(self)
        self.table.setRowCount(10)
        self.table.setColumnCount(6)
        self.table.setItem(2, 3, QTableWidgetItem("TEST")) # 개별 항목
        # 행 레이블
        self.table.setVerticalHeaderItem(0, QTableWidgetItem("Prefetch"))
        self.table.setVerticalHeaderItem(1, QTableWidgetItem("Event Log"))
        self.table.setVerticalHeaderItem(2, QTableWidgetItem("[W] History"))
        self.table.setVerticalHeaderItem(3, QTableWidgetItem("Event Log"))
        self.table.setVerticalHeaderItem(4, QTableWidgetItem("$usnjrnl"))
        self.table.setVerticalHeaderItem(5, QTableWidgetItem("$usnjrnl"))
        self.table.setVerticalHeaderItem(6, QTableWidgetItem("Event Log"))
        self.table.setVerticalHeaderItem(7, QTableWidgetItem("Event Log"))
        self.table.setVerticalHeaderItem(8, QTableWidgetItem("Report.wer"))
        self.table.setVerticalHeaderItem(9, QTableWidgetItem("[W] Cookie"))

        # 열 레이블
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Timeline"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Path"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Value"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem(" - "))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem(" - "))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem(" - "))

        self.table.move(0, 110 + self.search.height())
        self.table.resize(self.search.width()+20, self.h+100)
        self.layout.addWidget(self.table)
        self.layout.addStretch()

        # table selection change
        self.table.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.table.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def contextMenuEvent(self, QContextMenuEvent):
        # 윈도우에서 마우스 우클릭 핸들링
        contextMenu = QMenu(self)
        quit = contextMenu.addAction("Quit")

        # quit 변수로 액션 발동 유무 파악
        action = contextMenu.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()     # QCoreApplication.instance().quit() 보다 더 간단함.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w = Main()
    w.showMaximized()
    sys.exit(app.exec_())