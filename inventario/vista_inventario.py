#!/usr/bin/python
# encoding: utf-8
"""

"""
import sys
from PySide import QtCore, QtGui
from inventario import Ui_Dialog
from formulario_producto.vista_formulario import Formulario
import controlador_inventario

class Inventario(QtGui.QDialog):

	__header_table__ = [(u"Código"),
						(u"Descripción"),
						(u"Categoría"),
						(u"Proveedor"),
						(u"Precio Unitario"),
						(u"estado"),
						(u"Stock")]

	def __init__(self, rut=""):
		super(Inventario, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.rut = rut

		self.setSignals()

		self.inicializar_tabla()
		self.show()

	def setSignals(self):
		self.ui.tw_inventario.currentCellChanged.connect(self.obtiene_id_producto)
		self.ui.btn_agregar.clicked.connect(self.abrir_formulario)
		self.ui.btn_editar.clicked.connect(self.editar_formulario)
		self.ui.tw_inventario.cellDoubleClicked.connect(self.editar_formulario)
		self.ui.btn_descontinuar.clicked.connect(self.descontinuar_formulario)
		self.ui.btn_buscar.clicked.connect(self.buscar_productos)
		self.ui.le_buscar.textChanged.connect(self.buscar_productos)

	def obtiene_id_producto(self, fila_actual, columna_actual, fila_previa, columna_previa):
		producto = self.ui.tw_inventario.item(fila_actual, 0)
		try:
			self.id = producto.text()
		except:
			pass

	def inicializar_tabla(self):
		self.ui.tw_inventario.sortItems(1, QtCore.Qt.AscendingOrder)
		self.ui.tw_inventario.setColumnCount(7)
		self.ui.tw_inventario.setHorizontalHeaderLabels(self.__header_table__)
		self.ui.tw_inventario.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

		productos = controlador_inventario.obtenerProductos()
		row = len(productos)
		self.ui.tw_inventario.setRowCount(row)

		for i, data in enumerate(productos):
			stock = controlador_inventario.buscaStockPorCodigo(data[0])
			row = [QtGui.QTableWidgetItem(str(data[0])),
			QtGui.QTableWidgetItem(data[1]),
			QtGui.QTableWidgetItem(data[2]),
			QtGui.QTableWidgetItem(data[4]),
			QtGui.QTableWidgetItem(data[3]),
			QtGui.QTableWidgetItem(str(data[5])),
			QtGui.QTableWidgetItem(str(stock[0][0]))]
			for j, cell in enumerate(row):
				self.ui.tw_inventario.setItem(i, j, cell)

		self.ui.tw_inventario.sortItems(1, QtCore.Qt.DescendingOrder)
		self.ui.tw_inventario.resizeColumnsToContents()
		self.ui.tw_inventario.horizontalHeader().setResizeMode(3, 
			self.ui.tw_inventario.horizontalHeader().Stretch)

	def recargar_tabla(self):
		self.ui.tw_inventario.setRowCount(0)
		self.inicializar_tabla()

	def abrir_formulario(self):
		self.formulario = Formulario("ingresar", self.rut, id="")
		self.formulario.finished.connect(self.inicializar_tabla) 
		self.formulario.exec_()

	def editar_formulario(self):
		index = self.ui.tw_inventario.currentIndex()
		if(index.row() == -1):
			errorMessage(self, "No se ha seleccionado nada")
		else:
			self.formulario = Formulario("editar", self.rut, self.id)
			self.formulario.finished.connect(self.inicializar_tabla) 
			self.formulario.exec_()
			self.ui.tw_inventario.selectRow(index.row())

	def descontinuar_formulario(self):
		index = self.ui.tw_inventario.currentIndex()
		if(index.row() == -1):
			errorMessage(self, "No se ha seleccionado nada")
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			msgBox.setWindowTitle(u"Advertencia")
			msgBox.setText(u"Esta seguro en descontinuar producto seleccionado?")
			press = msgBox.exec_()
			if(press == QtGui.QMessageBox.Ok):
				retorno = controlador_inventario.descontinuarProducto(self.id)
				if(retorno):
					controlador_inventario.registrarModificacion(self.rut, self.id, "descontinuar")
					self.recargar_tabla()
				else:
					pass
			else:
				return False

	def buscar_productos(self):
		entrada = self.ui.le_buscar.text().lstrip()
		if(controlador_inventario.validaTexto(entrada, "num")):
			productos = controlador_inventario.buscarProductosPorCodigo(entrada)
		else:
			productos = controlador_inventario.buscarProductos(entrada)

		row = len(productos)
		self.ui.tw_inventario.setRowCount(row)

		for i, data in enumerate(productos):
			stock = controlador_inventario.buscaStockPorCodigo(data[0])
			row = [QtGui.QTableWidgetItem(str(data[0])),
			QtGui.QTableWidgetItem(data[1]),
			QtGui.QTableWidgetItem(data[2]),
			QtGui.QTableWidgetItem(data[3]),
			QtGui.QTableWidgetItem(data[4]),
			QtGui.QTableWidgetItem(str(data[5])),
			QtGui.QTableWidgetItem(str(stock[0][0]))]
			for j, cell in enumerate(row):
				self.ui.tw_inventario.setItem(i, j, cell)

		self.ui.tw_inventario.sortItems(7, QtCore.Qt.DescendingOrder)
		self.ui.tw_inventario.resizeColumnsToContents()
		self.ui.tw_inventario.horizontalHeader().setResizeMode(3, 
			self.ui.tw_inventario.horizontalHeader().Stretch)

