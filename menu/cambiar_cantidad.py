# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambiar_cantidad.ui'
#
# Created: Tue Oct 24 17:28:24 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 171)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_codigo = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lb_codigo.setFont(font)
        self.lb_codigo.setText("")
        self.lb_codigo.setObjectName("lb_codigo")
        self.verticalLayout.addWidget(self.lb_codigo)
        self.lb_descripcion_producto = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lb_descripcion_producto.setFont(font)
        self.lb_descripcion_producto.setText("")
        self.lb_descripcion_producto.setObjectName("lb_descripcion_producto")
        self.verticalLayout.addWidget(self.lb_descripcion_producto)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_cantidad = QtGui.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.le_cantidad.setFont(font)
        self.le_cantidad.setObjectName("le_cantidad")
        self.horizontalLayout.addWidget(self.le_cantidad)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btn_aceptar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_aceptar.setFont(font)
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.verticalLayout.addWidget(self.btn_aceptar)
        self.btn_cancelar = QtGui.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.verticalLayout.addWidget(self.btn_cancelar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_cantidad, self.btn_aceptar)
        Dialog.setTabOrder(self.btn_aceptar, self.btn_cancelar)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Cambiar Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nueva Cantidad", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_aceptar.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancelar.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

