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
	query = "SELECT * FROM producto"
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def buscaProductoPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM producto WHERE codigo = '%s'" % codigo)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def ingresarProducto(codigo, descripcion, categoria, precio, proveedor, idInventario, stock):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "INSERT INTO producto(codigo, descripcion, categoria, precio, proveedor, estado) VALUES (?, ?, ?, ?, ?, 1)"
	conn.execute(query, (codigo, descripcion, categoria, precio, proveedor))
	conect.commit()
	query2 = "INSERT INTO inventario(idInventario, codigoProducto, stock) VALUES (?, ?, ?)"
	conn.execute(query2, (idInventario, codigo, stock))
	conect.commit()
	conn.close()

def modificarEstadoProducto(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("UPDATE producto SET estado = 1 WHERE codigo = '%s'" % codigo)
	conn.execute(query)
	conect.commit()
	conn.close()

def modificaProducto(codigo, descripcion, categoria, precio, proveedor, stock):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "UPDATE producto SET descripcion = ?, categoria = ?, precio = ?, proveedor = ? WHERE codigo = '%s'" % codigo
	conn.execute(query, (descripcion, categoria, precio, proveedor))
	conect.commit()
	query2 = "UPDATE inventario set stock = ? WHERE codigoProducto = '%s'" % codigo
	conn.execute(query2, (stock,))
	conect.commit()
	conn.close()

def buscaStockPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT stock FROM inventario WHERE codigoProducto = '%s'" % codigo)
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