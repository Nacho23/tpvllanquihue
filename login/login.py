# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri Sep 29 14:29:25 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 240)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.le_usuario = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.le_usuario.setFont(font)
        self.le_usuario.setObjectName("le_usuario")
        self.verticalLayout.addWidget(self.le_usuario)
        self.le_contrasena = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.le_contrasena.setFont(font)
        self.le_contrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.le_contrasena.setObjectName("le_contrasena")
        self.verticalLayout.addWidget(self.le_contrasena)
        self.btn_Entrar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.btn_Entrar.setFont(font)
        self.btn_Entrar.setObjectName("btn_Entrar")
        self.verticalLayout.addWidget(self.btn_Entrar)
        self.btn_recordar_contrasena = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.btn_recordar_contrasena.setFont(font)
        self.btn_recordar_contrasena.setObjectName("btn_recordar_contrasena")
        self.verticalLayout.addWidget(self.btn_recordar_contrasena)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "INICIAR SESIÓN", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_Entrar.setText(QtGui.QApplication.translate("Dialog", "ACCEDER", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_recordar_contrasena.setText(QtGui.QApplication.translate("Dialog", "RECORDAR CONTRASEÑA", None, QtGui.QApplication.UnicodeUTF8))

