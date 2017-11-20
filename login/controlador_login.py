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
import modelo_login
import cryptoraf as c
from random import choice
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def buscaTrabajador(self, rut, contrasena):
	rut_valido = validaRut(rut)
	if(rut_valido):
		resultado = modelo_login.buscaTrabajador(rut, contrasena)
		if(len(resultado) == 0):
			pass
		else:
			tupla_resultado = resultado[0]
			rut = tupla_resultado[0]
			contrasena = tupla_resultado[1]
			arreglo_resultado = [rut, contrasena]
			return arreglo_resultado
	else:
		pass
	# return resultado

def buscaTrabajadorPorRut(self, rut):
	rut_valido = validaRut(rut)
	if(rut_valido):
		resultado = modelo_login.buscaTrabajadorPorRut(rut)
		tupla_resultado = resultado[0]
		rut = tupla_resultado[0]
		nombre = tupla_resultado[1]
		apellido = tupla_resultado[3]
		email = tupla_resultado[2]
		arreglo_resultado = [rut, nombre, apellido, email]
		return arreglo_resultado
	else:
		errorMessage(self, "Rut Invalido")


def validaRut(rut):
	"""
	Valida si el rut ingresado es correcto o no. 
	Hace uso de metodos de validaRut desde otras clases.
	"""      
	rutValido = False
	suma = 0
	multi= 2
	datos_rut = rut.split('-') #separamos la cadena por '-'
	if(len(datos_rut) == 2 and datos_rut[1] != ""):
		rutValido = validaTexto(datos_rut[0],"num")
		if(len(datos_rut[1])==1 and rutValido):
			rutValido = validaTexto(datos_rut[1],"rut")
		else:
			rutValido = False
		rut_1 = datos_rut[0]
		dig = datos_rut[1]
		if(len(rut_1)>= 6 and rutValido):
			for r in rut_1[::-1]:
				suma += int(r)* multi
				multi+= 1
				if multi == 8:
					multi = 2
			resto = suma%11
			resta = 11 - resto
			if resta == 11:
				dig_r = 0
			elif resta == 10:
				dig_r = 'k'
			else:
				dig_r = resta
			if(str(dig_r) != str(dig)):
				rutValido = False
			else:
				rutValido = True
		else:
			rutValido = False
	else:
		rutValido = False
	return rutValido

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

def enviar_email(email, clave):
	"""
	Envia un email al correo electronico con la contraseña para poder ingresar, si esta se le olvida.
	Se crea una contraseña aleatoria la cual se envia al correo y se almacena en la base de datos,
	con motivo de no tener acceso a la contraseña real del usuario.
	"""
	destinatario = email
	print(u"Se envio su contraseña al \ncorreo electrónico: \n" + email)
	user = "equipodesarrolloss@gmail.com"
	password = "equipo123456"
	#para las cabeceras del email
	remitente = "equipodesarrolloss@gmail.com"
	asunto = "Recuperacion contraseña"
	mensaje = ("Su contraseña es: " + clave)
	#Host y puerto SMTP de Gmail
	gmail = smtplib.SMTP('smtp.gmail.com:587')
	#protocolo de cifrado de datos utilizado por gmail
	gmail.starttls()
	#credenciales
	gmail.login(user, password)
	#muestra la depuracion de la operacion de envío (1 = true)
	gmail.set_debuglevel(1)
	
	header = MIMEMultipart()
	header['Subject'] = asunto
	header['From'] = remitente
	header['To'] = destinatario

	mensaje = MIMEText(mensaje, 'html')
	header.attach(mensaje)
	#Enviar email
	gmail.sendmail(remitente, destinatario, header.as_string())
	#cerrar conexion SMTP
	gmail.quit()

def generar_clave():
	longitud = 10
	valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	clave_temp = ""
	clave_temp = clave_temp.join([choice(valores) for i in range(longitud)])
	return clave_temp

def modificar_clave(rut, clave):
	clave_encriptada = encriptar_clave(clave)
	modelo_login.modificar_clave(rut, clave_encriptada)

def encriptar_clave(clave):
	crypt = c.CryptoRAF()
	clave_encriptada = crypt.encrypt(clave, "asdlkjqweiou12308zmxncbdjdjdal")
	return clave_encriptada

def errorMessage(self, message):
	"""Función que despliega un mensaje de error.
	@param message"""
	QtGui.QMessageBox.warning(self, u"ERROR!", message)

def correctMessage(self, message):
	"""Función que despliega un mensaje de operacion correcta.
	@param message"""
	QtGui.QMessageBox.information(self, u"Operacion correcta", message)