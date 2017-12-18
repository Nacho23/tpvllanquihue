#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Modelo.
Accede a la base de datos
"""

import sqlite3 as sql
import sys
from DB.conexion import Conexion

def buscaTrabajador(rut, contrasena):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM cuenta WHERE rut = '%s'" % rut + 
		" AND contrasena = '%s'" % contrasena)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def buscaTrabajadorPorRut(rut):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = ("SELECT * FROM trabajador WHERE rut = '%s'" % rut)
	conn.execute(query)
	resultado = conn.fetchall()
	conn.close()
	return resultado

def modificar_clave(rut, clave):
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "UPDATE cuenta SET contrasena = ? WHERE rut = ?"
	conn.execute(query, (clave, rut))
	conect.commit()
	conn.close()

def registrarIngreso(rut, fecha):
	print(rut + " " + fecha)
	conexion = Conexion()
	conect = conexion.conectarBD()
	conn = conect.cursor()
	query = "INSERT INTO ingreso(rut, fecha) VALUES (?, ?)"
	conn.execute(query, (rut, fecha))
	conect.commit()
	conn.close()

