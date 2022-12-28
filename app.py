import re
import sys

from PySide6.QtGui import QPixmap
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from RegisterWIndow import Ui_MainWindow
from User import User
from database import open_connection_to_database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connection_to_database = None
        self.pp_path = ""
        self.setupUi(self)
        self.connect_signals_to_slots()
        self.connection_to_database = open_connection_to_database("QSQLITE", "main.db")
        self.show()

    def get_the_path_of_pp_selected(self):
        """Get the absolute path of the profil picture selected"""
        pp = QFileDialog.getOpenFileName(self, "Open file")
        pp_path = pp[0]
        return pp_path

    def connect_signals_to_slots(self):
        """Connect all the signals of the application to them slots"""
        self.browser_button.mousePressEvent = self.on_browser_button_clicked
        self.confirm_button.mousePressEvent = self.on_confirm_button_clicked

    def on_browser_button_clicked(self, event):
        """Slots for browser the image and display it"""
        self.pp_name = QFileDialog.getOpenFileName(self, "Open file")
        pixmap = QPixmap(self.pp_name[0])
        self.pp_picture.setPixmap(pixmap)

    def confirm_password_match(self):
        """Confirm if the password is the same of the confirm password"""
        return self.password_lineEdit.text() == self.confirm_password_lineEdit.text()

    def mail_enter_is_valid(self):
        """Confirm if the mail enter is a valid mail or not"""
        regex: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex, self.mail_lineEdit.text())

    def create_a_new_user(self) -> User:
        """Create a new user thanks to register form"""
        new_user: User = None
        new_user = User(self.login_lineEdit.text(),
                        self.mail_lineEdit.text(),
                        self.password_lineEdit.text(),
                        self.get_the_path_of_pp_selected()
                        )
        return new_user

    def on_confirm_button_clicked(self, event):
        error_message: str = ""
        entry_is_valid: bool = True
        if not self.confirm_password_match():
            error_message += "The password doesn't match ! \n"
            entry_is_valid = False
        if not self.mail_enter_is_valid():
            error_message += "The mail is not correct ! \n"
            entry_is_valid = False
        if not entry_is_valid:
            QMessageBox.warning(self, "Entries aren't valid !", error_message)
        else:
            new_user: User = self.create_a_new_user()
            self.create_new_user_query(new_user)

    def create_new_user_query(self, user: User):
        """Create the sql query to create a new user into the database"""
        insert_a_new_user = QSqlQuery()
        insert_a_new_user.prepare(
            """
            INSERT INTO users (
                login,
                mail,
                password,
                pp
            ) VALUES (?, ?, ?, ?)
            """
        )
        insert_a_new_user.addBindValue(user.login)
        insert_a_new_user.addBindValue(user.mail)
        insert_a_new_user.addBindValue(user.password)
        insert_a_new_user.addBindValue(user.pp)
        insert_a_new_user.exec()

def load_style(app: QApplication):
    """Load the style for my application thanks to a qss file style"""
    with open('styles.qss', 'r') as f:
        styles = f.read()
        app.setStyleSheet(styles)


app = QApplication(sys.argv)
load_style(app)
main_window = MainWindow()
app.exec()
