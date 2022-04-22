# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from instr import *
from second_win import TestWin
class MainWin(QWidget):
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
        self.txt_hello = QLabel(txt_hello)
        self.description = QLabel(txt_instruction)
        self.btn_next = QPushButton(txt_next)
        self.v_line = QVBoxLayout()
        self.v_line.addWidget(self.txt_hello)
        self.v_line.addWidget(self.description)
        self.v_line.addWidget(self.btn_next)
        self.setLayout(self.v_line)
    def connects(self):
        self.btn_next.clicked.connect(self.click_next)
    def click_next(self):
        self.hide()
        self.tw = TestWin()

app = QApplication([])
window = MainWin()
app.exec_()