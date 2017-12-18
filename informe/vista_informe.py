#!/usr/bin/python
# encoding: utf-8
"""

"""
import sys
from PySide import QtCore, QtGui
from informe import Ui_Dialog
import controlador_informe
import time
from reportlab.pdfgen import canvas

class Informe(QtGui.QDialog):

	
	def __init__(self):
		super(Informe, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.__proveedores__ = []
		self.datos_informe = []

		self.inicializar()
		self.setSignals()
		self.show()

	def setSignals(self):
		self.ui.btn_generar.clicked.connect(self.captura_datos)
		self.ui.btn_cancelar.clicked.connect(self.cancelar)

	def inicializar(self):
		proveedores = controlador_informe.obtenerProveedores()
		for data in proveedores:
			self.__proveedores__.append(data)

		for data in self.__proveedores__:
			self.ui.cb_proveedor.addItem(data[0])
		fecha = time.strftime('%d-%m-%y')
		self.ui.date_fecha.setDate(QtCore.QDate.currentDate())

	def captura_datos(self):
		fecha = (self.ui.date_fecha.date()).toString("yy-MM-dd")
		proveedor = self.ui.cb_proveedor.currentText()
		if(proveedor == "TODOS"):
			for data in self.__proveedores__:
				self.generar_informe(fecha, data[0])
		else:

			self.generar_informe(fecha, proveedor)
		controlador_informe.correctMessage(self, "Informe(s) Generado(s) correctamente")

	def generar_informe(self, fecha, proveedor):
		resultado_aux = list(controlador_informe.obtenerDatosInforme(fecha, proveedor))
		resultado = []
		for i in resultado_aux:
			if i not in resultado:
				resultado.append(i)
		for data in resultado:
			venta = []
			cantidad = controlador_informe.obtenerCantidad(fecha, data[0])
			total_cantidad = 0
			for i in cantidad:
				total_cantidad = total_cantidad + i[0]
			total_ingreso = total_cantidad * int(str(data[2])[1:])
			venta.append(data[1])
			venta.append(str(total_cantidad))
			venta.append(str(total_ingreso))
			self.datos_informe.append(venta)
		self.generarPDF(proveedor)

	def generarPDF(self, proveedor):
		fecha = (self.ui.date_fecha.date()).toString("dd-MMMM-yyyy")
		c = canvas.Canvas("C:/Users/naxo_/Documents/TPVLLANQUIHUE/Documentos/informes/"+ proveedor + "_" + fecha + ".pdf")
		c.drawString(100,750,"Fecha: " + fecha)
		c.drawString(300,750,"Proveedor: " + proveedor)
		c.drawString(100,700,"Producto")
		c.drawString(300,700,"cantidad")
		c.drawString(400,700,"Total")
		eje_y = 680
		total_venta = 0
		for i in range(len(self.datos_informe)):
			c.drawString(100,eje_y,str(self.datos_informe[i][0]))
			c.drawString(300,eje_y,str(self.datos_informe[i][1]))
			c.drawString(400,eje_y,"$"+str(self.datos_informe[i][2]))
			total_venta = total_venta + int(self.datos_informe[i][2])
			eje_y -= 15

		c.drawString(100, eje_y-50, "Total Ventas: " + str(total_venta))

		if(proveedor == "coca-cola" or proveedor == "CCU"):
			c.drawString(100, eje_y-70, "Total Ganancias: " + str(total_venta*0.3))
		else:
			c.drawString(100, eje_y-70, "Total Ganancias: " + str(total_venta*0.2))

		fecha_generado = (QtCore.QDateTime.currentDateTime()).toString("dd-MM-yy hh:mm:ss")
		c.drawString(100, eje_y-100, "Fecha de generacion de informe: " + fecha_generado)

		c.save()
		self.datos_informe = []



	def cancelar(self):
		self.close()