# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 604)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 20, 491, 531))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(220, 20, 111, 16))
        self.login_lineEdit = QLineEdit(self.frame)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        self.login_lineEdit.setGeometry(QRect(20, 100, 113, 20))
        self.login_label = QLabel(self.frame)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setGeometry(QRect(20, 80, 91, 16))
        self.mail_label = QLabel(self.frame)
        self.mail_label.setObjectName(u"mail_label")
        self.mail_label.setGeometry(QRect(20, 140, 91, 16))
        self.mail_lineEdit = QLineEdit(self.frame)
        self.mail_lineEdit.setObjectName(u"mail_lineEdit")
        self.mail_lineEdit.setGeometry(QRect(20, 160, 113, 20))
        self.password_lineEdit = QLineEdit(self.frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(20, 230, 113, 20))
        self.password_label = QLabel(self.frame)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(20, 210, 91, 16))
        self.confirm_password_label = QLabel(self.frame)
        self.confirm_password_label.setObjectName(u"confirm_password_label")
        self.confirm_password_label.setGeometry(QRect(20, 280, 171, 16))
        self.confirm_password_lineEdit = QLineEdit(self.frame)
        self.confirm_password_lineEdit.setObjectName(u"confirm_password_lineEdit")
        self.confirm_password_lineEdit.setGeometry(QRect(20, 300, 113, 20))
        self.pp_label = QLabel(self.frame)
        self.pp_label.setObjectName(u"pp_label")
        self.pp_label.setGeometry(QRect(20, 340, 171, 16))
        self.pp_picture = QLabel(self.frame)
        self.pp_picture.setObjectName(u"pp_picture")
        self.pp_picture.setGeometry(QRect(20, 360, 151, 91))
        self.browser_button = QFrame(self.frame)
        self.browser_button.setObjectName(u"browser_button")
        self.browser_button.setGeometry(QRect(20, 460, 111, 31))
        self.browser_button.setFrameShape(QFrame.StyledPanel)
        self.browser_button.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.browser_button)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 10, 81, 16))
        self.label_9 = QLabel(self.browser_button)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 30, 81, 16))
        self.confirm_button = QFrame(self.frame)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setGeometry(QRect(200, 490, 101, 31))
        self.confirm_button.setFrameShape(QFrame.StyledPanel)
        self.confirm_button.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.confirm_button)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 10, 81, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 546, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"S'enregistrer", None))
        self.login_label.setText(QCoreApplication.translate("MainWindow", u"Identifiant", None))
        self.mail_label.setText(QCoreApplication.translate("MainWindow", u"Adresse mail", None))
        self.password_label.setText(QCoreApplication.translate("MainWindow", u"Mot de passe", None))
        self.confirm_password_label.setText(QCoreApplication.translate("MainWindow", u"Confirmation mot de passe", None))
        self.pp_label.setText(QCoreApplication.translate("MainWindow", u"Photo de profil", None))
        self.pp_picture.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Parcourir", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Parcourir", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Confirmer", None))
    # retranslateUi

