#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos
"""

import sqlite3 as sql
import sys
from DB.conexion import Conexion

def obtenerProductos():
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "SELECT * FROM producto WHERE estado = 1"
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def buscaStockPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT stock FROM inventario WHERE codigoProducto = '%s'" % codigo)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def descontinuarProducto(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("UPDATE producto SET estado = 0 WHERE codigo = '%s'" % codigo)
	conn.execute(query)
	conect.commit()
	conn.close()

def buscarProductos(entrada):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "SELECT * FROM producto WHERE descripcion LIKE ? OR codigo LIKE ? OR proveedor LIKE ? AND estado = 1"
	conn.execute(query, (entrada, entrada, entrada))
	resultado = conn.fetchall()
	conn.close()
	return resultado

def buscarProductosPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM producto WHERE codigo = '%s' AND estado = 1" % codigo)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def registrarModificacion(idModifica, rut, codigo, accion):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "INSERT INTO modifica(idModifica, rutTrabajador, codigoProducto, accion) VALUES (?, ?, ?, ?)"
	conn.execute(query, (idModifica, rut, codigo, accion))
	conect.commit()
	conn.close()