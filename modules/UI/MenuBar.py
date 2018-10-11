from PyQt5.QtWidgets import QMenuBar, QMenu, QAction, qApp, QFileDialog
from modules.UI.SubWindow import SubWindow

class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        # 메뉴 생성
        fileMenu = self.addMenu("File")  # 메뉴그룹 생성
        fileMenu.triggered[QAction].connect(self.openFileDialog)
        viewMenu = self.addMenu("View")
        # viewMenu.triggered[QAction].connect(self.openFileDialog)
        helpMenu = self.addMenu("Help")

        subMenu = QMenu("Import", self)  # 서브메뉴 생성
        importUsnjrnl = QAction("$usnjrnl", self)
        importMFT = QAction("$mft", self)
        importLogFile = QAction("$LogFile", self)
        subMenu.addAction(importUsnjrnl)
        subMenu.addAction(importMFT)
        subMenu.addAction(importLogFile)
        fileMenu.addMenu(subMenu)

        exit_menu = QAction("Exit", self)  # 메뉴 객체 생성
        exit_menu.setShortcut("Ctrl+Q")  # 단축키 생성
        exit_menu.setStatusTip("종료")
        exit_menu.triggered.connect(qApp.quit)
        fileMenu.addAction(exit_menu)

        reloadAction1 = QAction("Reload", self)
        reloadAction1.setShortcut("F5")
        timelineAction2 = QAction("Reload with Timeline", self)
        timelineAction2.setShortcut("F6")
        fullScreenAction3 = QAction("Full Screen", self, checkable=True)
        fullScreenAction3.setShortcut("F11")
        fullScreenAction3.setChecked(False)
        viewAction4 = QAction("View Option 4", self, checkable=True)
        viewAction4.setChecked(False)
        viewMenu.addAction(reloadAction1)
        viewMenu.addAction(timelineAction2)
        viewMenu.addAction(fullScreenAction3)
        viewMenu.addAction(viewAction4)

        envAction = QAction("Environment", self)
        envAction.triggered.connect(self.showUserEnvironment)
        shortcutAction = QAction("Shortcut", self)
        shortcutAction.triggered.connect(self.showShortcutInfo)
        helpMenu.addAction(envAction)
        helpMenu.addAction(shortcutAction)

    def openFileDialog(self, type):
        print(type.text() + " is triggered")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*)", options=options)
        fileType = type.text()
        if fileType == "$usnjrnl":
            SubWindow(fileName).showUsnjrnl()
        elif fileType == "$MFT":
            SubWindow(fileName).showMFT()
        elif fileType == "$LogFile":
            SubWindow(fileName).showLogFile()

    def showUserEnvironment(self):
        print("showUserEnvironment")

    def showShortcutInfo(self):
        print("showShortcutInfo")