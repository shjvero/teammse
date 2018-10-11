import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Push me!', self)
        btn.resize(btn.sizeHint()) # 글씨 기준으로 크기 조절
        btn.setToolTip('this is <strong>tooltip</strong>')
        btn.move(20, 30) # 버튼 움직이기.

        # 눌렀을 때, 시그널을 보내면, 받고 꺼지도록,
        # connect 인자에는 함수명만 들어감
        # ...connect(self.on_click)
        btn.clicked.connect(QCoreApplication.instance().quit)

        #self.setGeometry(300, 300, 400, 500) # 창크기 조절
        self.resize(500, 500) # 바탕화면 정중앙 배치.
        self.setWindowTitle("TEST Title")

        self.show()

    ''' from PyQt5.QtCore import pyqtSlot
    @pyqtSlot()
    def on_click(self):
        print("Button clicked")
    '''

    # 이벤트 재정의 (옆에 파란색버튼뜸) -- 윈도우 이벤트 (버튼이벤트 X)
    def closeEvent(self, QCloseEvent):
        print("종료시 이벤트를 여기서 받아요.")
        # 네번째 인자는 사용자가 결정하는 값
        # 마지막 인자는 디폴트값.
        ans = QMessageBox.question(self, "종료 확인", "프롬프트: 종료하시겠습니까?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if ans == QMessageBox.Yes:
            QCloseEvent.accept() # 이벤트 발생 승인
        elif ans == QMessageBox.No:
            QCloseEvent.ignore() # 이벤트 발생 무시

app = QApplication(sys.argv)
w = Exam()
sys.exit(app.exec_()) # 이벤트 처리 루프를 위해 exec가 아닌 exec_를 실행(메인루프)