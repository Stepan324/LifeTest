# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit
from instr import *
from final_win import FinalWin
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.text_name = QLabel(txt_name)
        self.age = QLabel(txt_age)
        self.text_timer = QLabel(txt_timer)

        self.name_input = QLineEdit(txt_hintname)
        self.age_input = QLineEdit(txt_hintage)
        
        self.test1 = QLabel(txt_test1)
        self.test2 = QLabel(txt_test2)
        self.test3 = QLabel(txt_test3)

        self.starttest1 = QPushButton(txt_starttest1)
        self.starttest2 = QPushButton(txt_starttest2)
        self.starttest3 = QPushButton(txt_starttest3)
        self.btn_next = QPushButton(txt_sendresults)


        self.test1_results = QLineEdit(txt_hinttest1)
        self.test3_result_1 = QLineEdit(txt_hinttest3)
        self.test3_result_2 = QLineEdit(txt_hinttest3)

        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.name_input, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.age, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.age_input, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test1_results, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.starttest3, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test3_result_1, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.test3_result_2, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)
    def connects(self):
        self.btn_next.clicked.connect(self.click_next)
    def click_next(self):
        self.hide()
        self.tw = FinalWin()