# -*- coding: UTF-8 -*-
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from calculate.cal import CalWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.number = ""
        self.setWindowTitle('计算器')
        self.base_widget = QWidget()
        self.cal = CalWidget()
        self.show_label = QLabel(str(0))
        self.show_label.setFrameStyle(QLabel.Box)
        self.base_layout = QVBoxLayout()
        self.base_layout.addWidget(self.show_label, 0)
        self.base_layout.addWidget(self.cal, 0)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        self.base_widget.setLayout(self.base_layout)
        self.setCentralWidget(self.base_widget)
        self.cal.btn_clicked.connect(self.add_number)
        self.cal.btn_plus.clicked.connect(self.plus)
        self.cal.btn_minus.clicked.connect(self.minus)
        self.cal.btn_multiply.clicked.connect(self.multiply)
        self.cal.btn_divide.clicked.connect(self.divide)
        self.cal.btn_del.clicked.connect(self.del_text)
        self.cal.btn_ok.clicked.connect(self.evaluate)

    def plus(self):
        self.number += '+'
        self.show_label.setText(self.number)

    def minus(self):
        self.number += '-'
        self.show_label.setText(self.number)

    def multiply(self):
        self.number += '*'
        self.show_label.setText(self.number)

    def divide(self):
        self.number += '/'
        self.show_label.setText(self.number)

    def add_number(self, num):
        self.number += str(num)
        self.show_label.setText(self.number)

    def del_text(self):
        self.number = self.number[0: -1]
        self.show_label.setText(self.number)
        if not self.number:
            self.show_label.setText(str(0))

    def evaluate(self):
        try:
            self.show_label.setText(str(eval(self.number)))
        except Exception as error:
            QMessageBox.critical(self, '错误', f'输入错误 (error message = {error})')

        self.number = ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())

