#!/usr/bin/python
# encoding: utf-8
"""

"""
import sys
from PySide import QtCore, QtGui
from cambiar_cantidad import Ui_Dialog
import controlador_menu

class Cambiar_Cantidad(QtGui.QDialog):

	def __init__(self, descripcion="", codigo="", cantidad=""):
		super(Cambiar_Cantidad, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.descripcion = descripcion
		self.codigo = codigo
		self.cantidad = cantidad

		self.setSignals()
		self.inicializarDatos()
		self.show()

	def setSignals(self):
		self.ui.btn_cancelar.clicked.connect(self.cancelar)
		self.ui.btn_aceptar.clicked.connect(self.cambiar_cantidad)

	def inicializarDatos(self):
		self.ui.lb_codigo.setText(str(self.codigo))
		self.ui.lb_descripcion_producto.setText(self.descripcion)
		self.ui.le_cantidad.setText(str(self.cantidad))

	def cambiar_cantidad(self):
		resultado = "HOLA"
		return resultado

	def cancelar(self):
		self.close()
