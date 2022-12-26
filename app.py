import sys

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from RegisterWIndow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.show()

    def connect_signals_to_slots(self):
        """Connect all the signals of the application to them slots"""
        self.browser_button.mousePressEvent = self.on_browser_button_clicked

    def on_browser_button_clicked(self, event):
        """Slots for browser the image and display it"""
        image_name = QFileDialog.getOpenFileName(self, "Open file")
        print(image_name)
        self.pixmap = QPixmap(image_name[0])
        self.pp_picture.setPixmap(self.pixmap)

def load_style(app: QApplication):
    """Load the style for my application thanks to a qss file style"""
    with open('styles.qss', 'r') as f:
        styles = f.read()
        app.setStyleSheet(styles)


app = QApplication(sys.argv)
load_style(app)
main_window = MainWindow()
app.exec()
        