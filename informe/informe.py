# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'informe.ui'
#
# Created: Wed Nov 15 14:03:14 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 136)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.date_fecha = QtGui.QDateEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.date_fecha.setFont(font)
        self.date_fecha.setObjectName("date_fecha")
        self.horizontalLayout_3.addWidget(self.date_fecha)
        self.cb_proveedor = QtGui.QComboBox(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.cb_proveedor.setFont(font)
        self.cb_proveedor.setObjectName("cb_proveedor")
        self.cb_proveedor.addItem("")
        self.horizontalLayout_3.addWidget(self.cb_proveedor)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.btn_generar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_generar.setFont(font)
        self.btn_generar.setObjectName("btn_generar")
        self.verticalLayout.addWidget(self.btn_generar)
        self.btn_cancelar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.verticalLayout.addWidget(self.btn_cancelar)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Generar Informe", None, QtGui.QApplication.UnicodeUTF8))
        self.date_fecha.setDisplayFormat(QtGui.QApplication.translate("Dialog", "dd-MM-yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_proveedor.setItemText(0, QtGui.QApplication.translate("Dialog", "TODOS", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_generar.setText(QtGui.QApplication.translate("Dialog", "GENERAR", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "CANCELAR", None, QtGui.QApplication.UnicodeUTF8))

