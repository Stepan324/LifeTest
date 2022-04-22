# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from instr import *

class FinalWin(QWidget):
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
        self.result_show = QLabel(txt_index)
        self.res_react = QLabel(txt_res1)
        self.ver_line = QVBoxLayout()
        self.ver_line.addWidget(self.result_show)
        self.ver_line.addWidget(self.res_react)
        self.setLayout(self.ver_line)
    def connects(self):
        pass