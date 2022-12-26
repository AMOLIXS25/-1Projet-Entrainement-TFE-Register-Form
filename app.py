import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from RegisterWIndow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()
        