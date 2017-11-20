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
from random import choice
import modelo_formulario

def buscaProductoPorCodigo(self, codigo):
	resultado = modelo_formulario.buscaProductoPorCodigo(codigo)
	return resultado

def obtenerProductos():
	resultado = modelo_formulario.obtenerProductos()
	return resultado

def ingresarProducto(codigo, descripcion, categoria, precio, proveedor, stock):
	idInventario = generar_id()
	modelo_formulario.ingresarProducto(codigo, descripcion, categoria, precio, proveedor, idInventario, stock)

def modificarEstadoProducto(codigo):
	modelo_formulario.modificarEstadoProducto(codigo)

def generar_id():
	longitud = 4
	valores = "0123456789"
	clave_temp = ""
	clave_temp = clave_temp.join([choice(valores) for i in range(longitud)])
	return clave_temp

def buscaStockPorCodigo(codigo):
	resultado = modelo_formulario.buscaStockPorCodigo(codigo)
	return resultado

def modificaProducto(codigo, descripcion, categoria, precio, proveedor, stock):
	modelo_formulario.modificaProducto(codigo, descripcion, categoria, precio, proveedor, stock)

def registrarModificacion(rut, codigo, accion):
	idModifica = generar_id()
	modelo_formulario.registrarModificacion(idModifica, rut, codigo, accion)


def errorMessage(self, message):
    """Función que despliega un mensaje de error.
    @param message"""
    QtGui.QMessageBox.warning(
    	self,
        u"ERROR!",
        message)

def correctMessage(self, message):
    """Función que despliega un mensaje de operacion correcta.
    @param message"""
    QtGui.QMessageBox.information(
    	self,
        u"Operacion correcta",
        message)