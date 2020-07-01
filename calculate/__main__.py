from . import MainWindow
from PyQt5.QtWidgets import QApplication

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
