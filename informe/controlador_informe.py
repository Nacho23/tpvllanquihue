#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

import sys
from PySide import QtCore, QtGui
import modelo_informe

def obtenerProveedores():
	resultado = modelo_informe.obtenerProveedores()
	return resultado

def obtenerDatosInforme(fecha, proveedor):
	resultado = modelo_informe.obtenerDatosInforme(fecha, proveedor)
	return resultado

def obtenerCantidad(fecha, codigo):
	resultado = modelo_informe.obtenerCantidad(fecha, codigo)
	return resultado

def errorMessage(self, message):
	"""Función que despliega un mensaje de error.
	@param message"""
	QtGui.QMessageBox.warning(self, u"ERROR!", message)

def correctMessage(self, message):
	"""Función que despliega un mensaje de operacion correcta.
	@param message"""
	QtGui.QMessageBox.information(self, u"Operacion correcta", message)
