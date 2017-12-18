#!/usr/bin/python
# encoding: utf-8
"""
Muestra la ventana de login para identificarse en el sistema.
"""
import sys
from PySide import QtCore, QtGui
from login import Ui_Dialog
from menu.vista_menu import Menu
from vista_recordar_contrasena import Recordar_Contrasena
import controlador_login
import modelo_login
from twilio.rest import Client

class Login(QtGui.QDialog):

	def __init__(self):
		super(Login, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		self.notificacion = False

		self.setSignals()
		self.show()


	def setSignals(self):
		self.ui.btn_Entrar.clicked.connect(self.login)
		self.ui.btn_recordar_contrasena.clicked.connect(self.recordar_contrasena)
		

	def login(self):
		input_usuario = self.ui.le_usuario.text().lstrip()
		input_contrasena = self.ui.le_contrasena.text().lstrip()
		if(input_usuario == "" or input_contrasena == ""):
			controlador_login.correctMessage(self, "Existen campos en blanco")
		else:
			clave_encriptada = controlador_login.encriptar_clave(input_contrasena)
			resultado = controlador_login.buscaTrabajador(self, input_usuario, clave_encriptada)
			if(resultado == None):
				controlador_login.errorMessage(self, "Datos invalidos")
			else:
				if(len(resultado) > 0):
					if(self.notificacion == True):
						controlador_login.registrarIngreso(input_usuario)
						self.menu = Menu(resultado[0])
						self.menu.show()
						self.close()
						self.recordar_contrasena = Recordar_Contrasena(resultado[0])
						self.recordar_contrasena.exec_()
						self.notificacion = False
					else:
						controlador_login.registrarIngreso(input_usuario)
						self.menu = Menu(resultado[0])
						self.menu.show()
						self.close()

	def recordar_contrasena(self):
		rut_trabajador = self.ui.le_usuario.text().lstrip()
		trabajador = controlador_login.buscaTrabajadorPorRut(self, rut_trabajador)
		if(trabajador != None):
			# ENVIO CORREO ELECTRONICO CON SMTPLIB
			self.notificacion = True   #Booleano para saber si se recupero contraseña o no, y pedir nueva contraseña al inciar el sistema.
			email_trabajador = trabajador[3]
			clave_generada = controlador_login.generar_clave()
			controlador_login.correctMessage(self, "Clave enviada al correo electronico")
			controlador_login.enviar_email(email_trabajador, clave_generada)
			controlador_login.modificar_clave(rut_trabajador, clave_generada)

			# ENVIO SMS CON TWILIO
			# account_sid = "AC6c5ab8dd17c29e38dae1442aeb88c0d0"
			# auth_token = "85820a2f9cd30c197f6ea7c1291c68e5"
			# client = Client(account_sid, auth_token)
			# message = client.messages.create(to="+56982655627", from_="+56945950795", body="HOLAAA")
			# print(message.sid)
		else: 
			controlador_login.errorMessage(self, "Datos Invalidos")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Login()
    sys.exit(app.exec_())