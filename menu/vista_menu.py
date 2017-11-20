#!/usr/bin/python
# encoding: utf-8
"""
Muestra la ventana de login para identificarse en el sistema.
"""
import sys
from PySide import QtCore, QtGui
from menu import Ui_MainWindow
from inventario.vista_inventario import Inventario
from informe.vista_informe import Informe
from vista_cambiar_cantidad import Cambiar_Cantidad
import controlador_menu
import modelo_menu
import time

class Menu(QtGui.QMainWindow):

	__header_table__ = [(u"Código"),
						(u"Descripción"),
						(u"Categoria"),
						(u"Proveedor"),
						(u"Precio Unitario"),
						(u"Cantidad"),
						(u"Total")]

	def __init__(self, rut=""):
		super(Menu, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.rut = rut

		self.productos = []
		self.cantidad = 1

		self.setSignals()

		self.show()
		self.inicializaValores()
		self.inicializar_tabla()

	def setSignals(self):
		self.ui.tw_lista_productos.currentCellChanged.connect(self.obtiene_id_producto)
		self.ui.actionAbrir_inventario.triggered.connect(self.abrir_inventario)
		self.ui.actionGenerar_Informe_Diario.triggered.connect(self.abrir_generar_informe)
		self.ui.btn_buscar_producto.clicked.connect(self.agregar_producto)
		self.ui.btn_pagar.clicked.connect(self.realizar_venta)
		self.ui.btn_quitar_producto.clicked.connect(self.quitar_producto)

		# SOLUCION MOMENTANEA ----------------------------------------------
		self.ui.btn_mas.clicked.connect(self.agregar_cantidad)
		self.ui.btn_menos.clicked.connect(self.disminuir_cantidad)
		# ------------------------------------------------------------------

		# self.ui.tw_lista_productos.cellChanged.connect(self.modificar_cantidad)


	def inicializaValores(self):
		self.ui.lb_precio_total.setText("$0")
		resultado = controlador_menu.buscaTrabajador(self.rut)
		self.ui.lb_nombre.setText("Bienvenido " + resultado[1])
		self.ui.lb_apellido.setText(resultado[2])
		self.ui.lb_rut.setText(resultado[0])
		

	def inicializar_tabla(self):
		self.ui.tw_lista_productos.sortItems(0, QtCore.Qt.AscendingOrder)
		self.ui.tw_lista_productos.setColumnCount(7)
		self.ui.tw_lista_productos.setHorizontalHeaderLabels(self.__header_table__)
		self.ui.tw_lista_productos.setSelectionBehavior(QtGui.QTableWidget.SelectRows)

		self.ui.tw_lista_productos.sortItems(0, QtCore.Qt.DescendingOrder)
		self.ui.tw_lista_productos.resizeColumnsToContents()
		self.ui.tw_lista_productos.horizontalHeader().setResizeMode(3, 
			self.ui.tw_lista_productos.horizontalHeader().Stretch)

	def obtiene_id_producto(self, fila_actual, columna_actual, fila_previa, columna_previa):
		producto = self.ui.tw_lista_productos.item(fila_actual, 0)
		try:
			self.id = producto.text()
		except:
			pass

	def agregar_producto(self):
		entrada = self.ui.le_codigo.text().lstrip()
		valido = controlador_menu.validaTexto(entrada, "num")
		if(valido):
			aux_producto = controlador_menu.buscarProductoPorCodigo(entrada)
			if(len(aux_producto) != 0):
				producto = list(aux_producto[0])
				repetido = False
				for j in range(len(self.productos)):
					if(producto[0] == self.productos[j][0]):
						repetido = True
				if(repetido == False):
					stock1 = controlador_menu.verificaStock(entrada, 0)
					if(stock1):
						print("El producto se agrega como nuevo producto")
						producto.append(1)
						self.productos.append(producto)
						self.actualiza_tabla()
					else:
						controlador_menu.errorMessage(self, "No hay mas stock")
				else:
					# Aumentar el contador del producto
					print("El producto se repite")
					indice_producto = self.encontrar_sublista(self.productos,producto[0])[0]
					stock = controlador_menu.verificaStock(entrada, self.productos[indice_producto][6])
					if(stock):
						self.productos[indice_producto][6] += 1 
						print("Hay stock para comprar")
						self.actualiza_tabla()
					else:
						controlador_menu.errorMessage(self, "No hay mas stock")
			else:
				controlador_menu.errorMessage(self, "No existe el producto")
		else:
			controlador_menu.errorMessage(self, "Ingrese un codigo valido")
		self.ui.le_codigo.setText("")

	def quitar_producto(self):
		index = self.ui.tw_lista_productos.currentIndex()
		if(index.row() == -1):
			controlador_menu.errorMessage(self, "No se ha seleccionado nada")
		else:
			msgBox = QtGui.QMessageBox()
			msgBox.setIcon(QtGui.QMessageBox.Critical)
			msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
			msgBox.setWindowTitle(u"Advertencia")
			msgBox.setText(u"Eliminar producto de la venta?")
			press = msgBox.exec_()
			if(press == QtGui.QMessageBox.Ok):
				producto = list(controlador_menu.buscarProductoPorCodigo(self.id)[0])
				indice = self.encontrar_sublista(self.productos, producto[0])
				print(indice)
				self.productos.pop(indice[0])

				self.actualiza_tabla()
			else:
				return False



	def actualiza_tabla(self):

		row = len(self.productos)
		self.ui.tw_lista_productos.setRowCount(row)

		for i, data in enumerate(self.productos):
			row = [QtGui.QTableWidgetItem(str(data[0])),
			QtGui.QTableWidgetItem(data[1]),
			QtGui.QTableWidgetItem(data[2]),
			QtGui.QTableWidgetItem(data[4]),
			QtGui.QTableWidgetItem(data[3]),
			QtGui.QTableWidgetItem(str(data[6])),
			QtGui.QTableWidgetItem("$"+(str(int(data[6])*int(str(data[3])[1:]))))]
			for j, cell in enumerate(row):
				self.ui.tw_lista_productos.setItem(i, j, cell)

			self.ui.tw_lista_productos.resizeColumnsToContents()
			self.ui.tw_lista_productos.horizontalHeader().setResizeMode(3, 
				self.ui.tw_lista_productos.horizontalHeader().Stretch)


		suma_total = 0
		if(len(self.productos) != 0):
			for x in range (len(self.productos)):
				total_por_producto = self.ui.tw_lista_productos.item(x,6)
				suma_total = suma_total + int(str(total_por_producto.text())[1:])
				self.ui.lb_precio_total.setText("$" + str(suma_total))
		else:
			self.ui.lb_precio_total.setText("$0")

	def realizar_venta(self):
		fecha = time.strftime('%y-%m-%d')
		trabajador = self.ui.lb_rut.text()
		idVenta = controlador_menu.guardarVenta(fecha, trabajador)
		for i in range(len(self.productos)):
			codigo = (self.ui.tw_lista_productos.item(i,0)).text()
			cantidad = (self.ui.tw_lista_productos.item(i,5)).text()
			controlador_menu.guardarVentaProducto(idVenta, codigo, cantidad)
			controlador_menu.modificarStockPorCodigo(codigo, cantidad)
		controlador_menu.correctMessage(self, "Venta Realizada Correctamente")
		self.productos = []
		self.cantidad = 1
		self.actualiza_tabla()


	def abrir_inventario(self):
		self.inventario = Inventario(self.rut)
		self.inventario.show()

	def abrir_generar_informe(self):
		self.informe = Informe()
		self.informe.show()

	def encontrar_sublista(self, lista, valor):
		for sub_i, sublist in enumerate(lista):
			try:
				return (sub_i, sublist.index(valor))
			except ValueError:
				pass

	def agregar_cantidad(self):
		index = self.ui.tw_lista_productos.currentIndex()
		if(index.row() == -1):
			controlador_menu.errorMessage(self, "No se ha seleccionado nada")
		else:
			producto = list(controlador_menu.buscarProductoPorCodigo(self.id)[0])
			indice_producto = self.encontrar_sublista(self.productos,producto[0])[0]
			stock = controlador_menu.verificaStock(self.id, self.productos[indice_producto][6])
			if(stock):
				self.productos[indice_producto][6] += 1 
				print("Hay stock para comprar")
				self.actualiza_tabla()
			else:
				controlador_menu.errorMessage(self, "No hay mas stock")

	def disminuir_cantidad(self):
		producto = list(controlador_menu.buscarProductoPorCodigo(self.id)[0])
		indice_producto = self.encontrar_sublista(self.productos,producto[0])[0]
		self.productos[indice_producto][6] -= 1 
		self.actualiza_tabla()
		


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Menu()
	sys.exit(app.exec_())