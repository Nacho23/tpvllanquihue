# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventario.ui'
#
# Created: Thu Dec 07 12:25:27 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 900)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_agregar.setFont(font)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_editar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_editar.setFont(font)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout.addWidget(self.btn_editar)
        self.btn_descontinuar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_descontinuar.setFont(font)
        self.btn_descontinuar.setObjectName("btn_descontinuar")
        self.horizontalLayout.addWidget(self.btn_descontinuar)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.le_buscar = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.le_buscar.setFont(font)
        self.le_buscar.setObjectName("le_buscar")
        self.horizontalLayout.addWidget(self.le_buscar)
        self.btn_buscar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_buscar.setFont(font)
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tw_inventario = QtGui.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.tw_inventario.setFont(font)
        self.tw_inventario.setObjectName("tw_inventario")
        self.tw_inventario.setColumnCount(0)
        self.tw_inventario.setRowCount(0)
        self.verticalLayout.addWidget(self.tw_inventario)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.btn_agregar, self.btn_editar)
        Dialog.setTabOrder(self.btn_editar, self.btn_descontinuar)
        Dialog.setTabOrder(self.btn_descontinuar, self.le_buscar)
        Dialog.setTabOrder(self.le_buscar, self.btn_buscar)
        Dialog.setTabOrder(self.btn_buscar, self.tw_inventario)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Invetario", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Dialog", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Dialog", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_descontinuar.setText(QtGui.QApplication.translate("Dialog", "Descontinuar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Dialog", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setShortcut(QtGui.QApplication.translate("Dialog", "Return", None, QtGui.QApplication.UnicodeUTF8))

