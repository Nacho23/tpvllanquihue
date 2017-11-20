#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos
"""

import sqlite3 as sql
import sys
from DB.conexion import Conexion

def obtenerProveedores():
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "SELECT DISTINCT proveedor FROM producto"
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def obtenerDatosInforme(fecha, proveedor):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "SELECT codigo, descripcion, precio FROM producto, venta_producto, venta WHERE venta.idVenta = venta_producto.idVenta AND venta_producto.codigoProducto = producto.codigo AND producto.proveedor = ? AND venta.fecha = ?"
	conn.execute(query, (proveedor, fecha))
	resultado = conn.fetchall()
	conn.close()
	return resultado

def obtenerCantidad(fecha, codigo):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "SELECT cantidad FROM producto, venta, venta_producto AS vp WHERE vp.idVenta = venta.idVenta AND vp.codigoProducto = producto.codigo AND venta.fecha = ? AND producto.codigo = ?"
	conn.execute(query, (fecha, codigo))
	resultado = conn.fetchall()
	conn.close()
	return resultado