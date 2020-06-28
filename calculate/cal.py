from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QApplication, QButtonGroup, QPushButton

import sys


class CalWidget(QWidget):
    btn_clicked = pyqtSignal(int)

    def __init__(self, parent=None):
        super(CalWidget, self).__init__(parent)
        self.show_label = QLabel()
        self.show_label.setFrameStyle(QLabel.Box)
        self.cal_buttons = QButtonGroup()
        self.btn_1 = QPushButton(str(1))
        self.btn_2 = QPushButton(str(2))
        self.btn_3 = QPushButton(str(3))
        self.btn_4 = QPushButton(str(4))
        self.btn_5 = QPushButton(str(5))
        self.btn_6 = QPushButton(str(6))
        self.btn_7 = QPushButton(str(7))
        self.btn_8 = QPushButton(str(8))
        self.btn_9 = QPushButton(str(9))
        self.btn_0 = QPushButton(str(0))
        self.btn_plus = QPushButton('+')
        self.btn_minus = QPushButton('-')
        self.btn_multiply = QPushButton('*')
        self.btn_divide = QPushButton('/')
        self.btn_del = QPushButton('⬅')
        self.btn_ok = QPushButton('=')
        self.grid_layout = QGridLayout()
        self.__init_ui()

    def __init_ui(self):
        self.setLayout(self.grid_layout)
        self.grid_layout.addWidget(self.btn_1, 0, 0)
        self.grid_layout.addWidget(self.btn_2, 0, 1)
        self.grid_layout.addWidget(self.btn_3, 0, 2)
        self.grid_layout.addWidget(self.btn_del, 0, 3)
        #
        self.grid_layout.addWidget(self.btn_4, 1, 0)
        self.grid_layout.addWidget(self.btn_5, 1, 1)
        self.grid_layout.addWidget(self.btn_6, 1, 2)
        self.grid_layout.addWidget(self.btn_plus, 1, 3)
        self.grid_layout.addWidget(self.btn_minus, 1, 4)
        #
        self.grid_layout.addWidget(self.btn_7, 2, 0)
        self.grid_layout.addWidget(self.btn_8, 2, 1)
        self.grid_layout.addWidget(self.btn_9, 2, 2)
        self.grid_layout.addWidget(self.btn_multiply, 2, 3)
        self.grid_layout.addWidget(self.btn_divide, 2, 4)
        #
        self.grid_layout.addWidget(self.btn_0, 3, 1)
        self.grid_layout.addWidget(self.btn_ok, 3, 2)
        #
        self.btn_0.clicked.connect(lambda: self.button_clicked(0))
        self.btn_1.clicked.connect(lambda: self.button_clicked(1))
        self.btn_2.clicked.connect(lambda: self.button_clicked(2))
        self.btn_3.clicked.connect(lambda: self.button_clicked(3))
        self.btn_4.clicked.connect(lambda: self.button_clicked(4))
        self.btn_5.clicked.connect(lambda: self.button_clicked(5))
        self.btn_6.clicked.connect(lambda: self.button_clicked(6))
        self.btn_7.clicked.connect(lambda: self.button_clicked(7))
        self.btn_8.clicked.connect(lambda: self.button_clicked(8))
        self.btn_9.clicked.connect(lambda: self.button_clicked(9))

    def button_clicked(self, button: int):
        self.btn_clicked.emit(button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cal = CalWidget()
    cal.btn_clicked.connect(print)
    cal.show()
    sys.exit(app.exec_())
