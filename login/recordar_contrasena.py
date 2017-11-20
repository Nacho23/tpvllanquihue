# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recordar_contrasena.ui'
#
# Created: Wed Oct 11 18:43:19 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(424, 169)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_recordar_contrasena = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.le_recordar_contrasena.setFont(font)
        self.le_recordar_contrasena.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.le_recordar_contrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.le_recordar_contrasena.setObjectName("le_recordar_contrasena")
        self.verticalLayout_2.addWidget(self.le_recordar_contrasena)
        self.le_repetir_recordar_contrasena = QtGui.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.le_repetir_recordar_contrasena.setFont(font)
        self.le_repetir_recordar_contrasena.setEchoMode(QtGui.QLineEdit.Password)
        self.le_repetir_recordar_contrasena.setObjectName("le_repetir_recordar_contrasena")
        self.verticalLayout_2.addWidget(self.le_repetir_recordar_contrasena)
        self.btn_enviar = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_enviar.setFont(font)
        self.btn_enviar.setObjectName("btn_enviar")
        self.verticalLayout_2.addWidget(self.btn_enviar)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_recordar_contrasena, self.le_repetir_recordar_contrasena)
        Dialog.setTabOrder(self.le_repetir_recordar_contrasena, self.btn_enviar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Recordar Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Recordar Contraseña", None, QtGui.QApplication.UnicodeUTF8))
        self.le_recordar_contrasena.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Contraseña Nueva", None, QtGui.QApplication.UnicodeUTF8))
        self.le_repetir_recordar_contrasena.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Repetir Contraseña Nueva", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_enviar.setText(QtGui.QApplication.translate("Dialog", "Enviar Nueva Contraseña", None, QtGui.QApplication.UnicodeUTF8))

