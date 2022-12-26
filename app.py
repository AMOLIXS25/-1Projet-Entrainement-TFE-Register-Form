import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from RegisterWIndow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


def load_style(app: QApplication):
    """Load the style for my application thanks to a qss file style"""
    with open('styles.qss', 'r') as f:
        styles = f.read()
        app.setStyleSheet(styles)


app = QApplication(sys.argv)
main_window = MainWindow()
app.exec()
        