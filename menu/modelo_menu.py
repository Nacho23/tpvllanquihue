#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos
"""

import sqlite3 as sql
import sys
from DB.conexion import Conexion

def obtieneTodo():
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM trabajador")
	conn.execute(query)
	resultado = conn.fetchone()
	return resultado

def buscaTrabajador(rut):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM trabajador WHERE rut = '%s'" % rut)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def buscarProductoPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM producto WHERE codigo = '%s' AND estado = 1" % codigo)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def guardarVenta(fecha, trabajador):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query2 = "SELECT COUNT (*) FROM venta"
	conn.execute(query2)
	idVenta = (conn.fetchone())[0]
	idVenta += 1
	query = "INSERT INTO venta(idVenta, fecha, rutTrabajador) VALUES (?, ?, ?)"
	conn.execute(query, (idVenta, fecha, trabajador))
	conect.commit()
	conn.close()
	return idVenta

def guardarVentaProducto(idVenta, codigo, cantidad):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "INSERT INTO venta_producto(idVenta, codigoProducto, cantidad) VALUES (?, ?, ?)"
	conn.execute(query, (idVenta, codigo, cantidad))
	conect.commit()
	conn.close()

def buscarStockPorCodigo(codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT stock FROM inventario WHERE codigoProducto = '%s'" % codigo)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado


def modificarStockPorCodigo(codigo, stock_nuevo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "UPDATE inventario SET stock = ? WHERE codigoProducto = ?"
	conn.execute(query, (stock_nuevo, codigo))
	conect.commit()
	conn.close()