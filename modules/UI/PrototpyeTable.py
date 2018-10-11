import sys
from PyQt5.Qt import *

class PrototypeTable(QTableWidget):
    def __init__(self, sw):
        super().__init__()
        # 사이즈, 기타 기능 준비
        self.load(sw)
        '''
            1. load() : 프로로타입 로드
            2. initUI() : 테이블 UI 로드
            3. copy() : 셀 우클릭 시 복사
            4. changeColumnHeader() : 항목 클릭 시 컬럼헤더 변화
            5. showDetail() : 항목 더블클릭 시 뷰어 켜기
            6. search() : 검색, 스크롤 바 이동까지 포함
        '''

    def load(self, sw=None, timeline=None):
        print("ready")
        if sw:
            print("다른 SW선택")
            if timeline:
                print("타임라인 설정 O")
            else:
                print("타임라인 설정 X")
        else:
            print("기존 SW 선택")
        # sw에 따라서 프로토타입 가져오기 -- 배열 or 객체
        # self.initUI(prototype)

    def initUI(self, prototype):
        print("initUI")
        # self.prototype 에 저장된 데이터들 모두 테이블에 로드

    def changeColumnHeader(self):
        print("changeColumnHeader")

    def showDetail(self):
        print("showDetail")

    def search(self, keyword):
        print("search: " + keyword)
