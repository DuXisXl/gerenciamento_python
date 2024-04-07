# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_login2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(833, 607)
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(29, 19, 771, 571))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -10, 771, 581))
        self.label.setPixmap(QPixmap(u"../../Downloads/new_login/Desktop - 1.png"))
        self.label.setScaledContents(True)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 310, 20, 21))
        self.label_6.setPixmap(QPixmap(u"../../Downloads/new_login/key.png"))
        self.label_6.setScaledContents(True)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 270, 20, 20))
        self.label_5.setPixmap(QPixmap(u"../../Downloads/new_login/account.png"))
        self.label_5.setScaledContents(True)
        self.txt_password = QLineEdit(self.frame)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setEnabled(True)
        self.txt_password.setGeometry(QRect(320, 310, 151, 20))
        self.txt_password.setAutoFillBackground(False)
        self.txt_password.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.txt_password.setFrame(False)
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setClearButtonEnabled(False)
        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setEnabled(True)
        self.txt_login.setGeometry(QRect(320, 270, 151, 21))
        self.txt_login.setAutoFillBackground(False)
        self.txt_login.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.txt_login.setFrame(False)
        self.txt_login.setEchoMode(QLineEdit.Normal)
        self.txt_login.setClearButtonEnabled(False)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(350, 360, 71, 21))
        self.btn_login.setCursor(QCursor(Qt.ClosedHandCursor))
        self.btn_login.setStyleSheet(u"background-color: transparent;\n"
"border: none;")

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.txt_password.setText("")
        self.txt_password.setPlaceholderText("")
        self.txt_login.setText("")
        self.txt_login.setPlaceholderText("")
        self.btn_login.setText("")
    # retranslateUi

