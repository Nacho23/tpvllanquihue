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
import modelo_inventario
from random import choice

def obtenerProductos():
	resultado = modelo_inventario.obtenerProductos()
	return resultado

def buscaStockPorCodigo(codigo):
	resultado = modelo_inventario.buscaStockPorCodigo(codigo)
	return resultado

def descontinuarProducto(codigo):
	stock = buscaStockPorCodigo(codigo)
	print(stock[0][0])
	if(stock[0][0] != 0):
		msgBox = QtGui.QMessageBox()
		msgBox.setIcon(QtGui.QMessageBox.Critical)
		msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
		msgBox.setWindowTitle(u"Advertencia")
		msgBox.setText(u"Aún existe stock en el inventario, ¿descontinuar producto de todas formas?")
		press = msgBox.exec_()
		if(press == QtGui.QMessageBox.Ok):
			modelo_inventario.descontinuarProducto(codigo)
			return True
		else:
			return False
	else:
		modelo_inventario.descontinuarProducto(codigo)

def buscarProductos(entrada):
	entrada = "%" + entrada + "%"
	resultado = modelo_inventario.buscarProductos(entrada)
	return resultado

def buscarProductosPorCodigo(codigo):
	resultado = modelo_inventario.buscarProductosPorCodigo(codigo)
	return resultado

def validaTexto(text,entrada):
	"""
	Valida si el texto ingresado es correcto o no. 
	Hace uso de metodos de validaTexto desde otras clases.
	""" 
	valido=True
	if (entrada == "rut"):
		cadena = "0123456789kK"
	if (entrada == "num"):
		cadena = "0123456789"
	if (entrada == "sinSimbolos"):
		cadena = " ,.-abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789"
	if (entrada == "texto"):
		cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"
	if (entrada == "rut_login"):
		cadena = "0123456789kK-"
	i=0
	string_num=str(text.encode('utf-8'))
	if(len(string_num)==0):
		valido=False
	while(valido and (i<len(string_num))):
		if (not string_num[i] in cadena):
			valido=False
		i=i+1
	return valido

def generar_id():
	longitud = 4
	valores = "0123456789"
	clave_temp = ""
	clave_temp = clave_temp.join([choice(valores) for i in range(longitud)])
	return clave_temp

def registrarModificacion(rut, codigo, accion):
	idModifica = generar_id()
	modelo_inventario.registrarModificacion(idModifica, rut, codigo, accion)

def errorMessage(self, message):
	"""Función que despliega un mensaje de error.
	@param message"""
	QtGui.QMessageBox.warning(self, u"ERROR!", message)

def correctMessage(self, message):
	"""Función que despliega un mensaje de operacion correcta.
	@param message"""
	QtGui.QMessageBox.information(self, u"Operacion correcta", message)