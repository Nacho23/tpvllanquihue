#!/usr/bin/python
# encoding: utf-8
"""

"""
import sys
from PySide import QtCore, QtGui
from formulario import Ui_Dialog
import controlador_formulario

class Formulario(QtGui.QDialog):

	def __init__(self, accion="", rut="", id=""):
		super(Formulario, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.accion = accion
		self.id = id
		self.rut = rut
		self.setSignals()
		self.inicializa_valores()
		self.show()

	def setSignals(self):
		self.ui.btn_aceptar.clicked.connect(self.guardar)
		self.ui.btn_cancelar.clicked.connect(self.cerrar)

	def inicializa_valores(self):
		if(self.accion == "editar"):
			producto = controlador_formulario.buscaProductoPorCodigo(self, self.id)
			self.ui.le_codigo.setText(unicode(str(producto[0][0])))
			self.ui.le_descripcion.setText(unicode(producto[0][1]))
			self.ui.le_categoria.setText(unicode(producto[0][2]))
			self.ui.le_proveedor.setText(unicode(producto[0][4]))
			self.ui.le_precio_unitario.setText(unicode(str(producto[0][3])))
			stock = controlador_formulario.buscaStockPorCodigo(self.id)
			self.ui.sb_cantidad_inventario.setValue(stock[0][0])
			print(producto)
		else:
			pass

	def guardar(self):
		if(self.accion == "ingresar"):
			codigo = self.ui.le_codigo.text().lstrip()
			descripcion = self.ui.le_descripcion.text().lstrip()
			categoria = self.ui.le_categoria.text().lstrip()
			proveedor = self.ui.le_proveedor.text().lstrip()
			precio = self.ui.le_precio_unitario.text().lstrip()
			stock = self.ui.sb_cantidad_inventario.value()
			# stock = str(stock_valor)
			if(len(codigo) == 0 or len(descripcion) == 0 or len(categoria) == 0 
				or len(proveedor) == 0 or len(precio) == 0):
				controlador_formulario.errorMessage(self, "Complete todos los datos")
			else:
				resultado = controlador_formulario.buscaProductoPorCodigo(self, codigo)
				if(len(resultado) == 0):
					controlador_formulario.ingresarProducto(codigo, descripcion, categoria, 
							precio, proveedor, stock)
					controlador_formulario.registrarModificacion(self.rut, codigo, self.accion)
					controlador_formulario.correctMessage(self, "Producto Ingresado Correctamente")
					self.close()
				else:
					estado_producto = resultado[0][5]
					if(estado_producto == 0):
						controlador_formulario.modificarEstadoProducto(codigo)
						controlador_formulario.correctMessage(self, "El producto ya existía anteriormente, se volvió a habilitar")
						self.close()
					else:
						controlador_formulario.errorMessage(self, "EL producto ya existe")
		if(self.accion == "editar"):
			codigo = self.ui.le_codigo.text().lstrip()
			descripcion = self.ui.le_descripcion.text().lstrip()
			categoria = self.ui.le_categoria.text().lstrip()
			precio = self.ui.le_precio_unitario.text().lstrip()
			proveedor = self.ui.le_proveedor.text().lstrip()
			stock = self.ui.sb_cantidad_inventario.value()
			arreglo_producto = [codigo, descripcion, categoria, proveedor, precio]
			print("----")
			print(arreglo_producto)
			if(len(arreglo_producto) < 5):
				controlador_formulario.errorMessage(self, "Complete todos los datos")
			else:
				controlador_formulario.modificaProducto(codigo, descripcion, categoria, 
					precio, proveedor, stock)
				controlador_formulario.registrarModificacion(self.rut, codigo, self.accion)
				controlador_formulario.correctMessage(self, "Producto Modificado Correctamente")
				self.close()


	def cerrar(self):
		self.close()