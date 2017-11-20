#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Controlador.
Es una capa intermedia entre la Vista y el Modelo.
Valida los datos de entrada que envía la vista y decide que información
enviar a la Vista.
"""

from PySide import QtCore, QtGui
import sys
import modelo_menu

def obtieneTodo():
	resultado = modelo_menu.obtieneTodo()

def buscaTrabajador(rut):
	resultado = modelo_menu.buscaTrabajador(rut)
	tupla_resultado = resultado[0]
	rut = tupla_resultado[0]
	nombre = tupla_resultado[1]
	apellido = tupla_resultado[3]
	arreglo_resultado = [rut, nombre, apellido]
	return arreglo_resultado

def verificaStock(codigo, stock_venta_actual):
	stock_actual = modelo_menu.buscarStockPorCodigo(codigo)[0][0]
	if(stock_actual < stock_venta_actual + 1):
		return False
	else:
		return True


def buscarProductoPorCodigo(codigo):
	resultado = modelo_menu.buscarProductoPorCodigo(codigo)
	return resultado

def guardarVenta(fecha, trabajador):
	idVenta = modelo_menu.guardarVenta(fecha, trabajador)
	return idVenta

def guardarVentaProducto(idVenta, codigo, cantidad):
	modelo_menu.guardarVentaProducto(idVenta, codigo, cantidad)

def modificarStockPorCodigo(codigo, cantidad):
	stock_actual = modelo_menu.buscarStockPorCodigo(codigo)[0][0]
	stock_nuevo = int(stock_actual)-int(cantidad)
	modelo_menu.modificarStockPorCodigo(codigo, stock_nuevo)

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


def errorMessage(self, message):
	"""Función que despliega un mensaje de error.
	@param message"""
	QtGui.QMessageBox.warning(self, u"ERROR!", message)

def correctMessage(self, message):
	"""Función que despliega un mensaje de operacion correcta.
	@param message"""
	QtGui.QMessageBox.information(self, u"Operacion correcta", message)