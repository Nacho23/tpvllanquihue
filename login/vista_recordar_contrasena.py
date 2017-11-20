#!/usr/bin/python
# encoding: utf-8

"""
Ventana que se ejecuta cuando se solicita recordar la contraseña
(enviar la nueva contraseña por correo), para que como programadores, no tengamos 
ningun contacto con la clave del usuario, al solicitar que se reponga, se crea un nueva
clave aleatoria, esta se almacena en base de datos y se envia por correo.
Cuando se ingrese al sistema usando esa clave, se solicitará crear una nueva clave al
usuario, y de esta forma darle el total control del programa.
"""

from PySide import QtCore, QtGui
from recordar_contrasena import Ui_Dialog
import controlador_login

class Recordar_Contrasena(QtGui.QDialog):


	def __init__(self, rut):
		super(Recordar_Contrasena, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.rut = rut

		self.setSignals()

	def setSignals(self):
		self.ui.btn_enviar.clicked.connect(self.modifica_contrasena)

	def modifica_contrasena(self):
		claveNueva = self.ui.le_recordar_contrasena.text().lstrip()
		confirmClave = self.ui.le_repetir_recordar_contrasena.text().lstrip()
		if(claveNueva == confirmClave):
			# clave_encriptada = controlador_login.encriptar_clave(claveNueva)
			controlador_login.modificar_clave(self.rut, claveNueva)
			controlador_login.correctMessage(self, u"""Contraseña cambiada correctamente""")
			self.close()
		else:
			controlador_login.correctMessage(self, u"""contraseñas no coinciden""")


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Recordar_Contrasena()
	sys.exit(app.exec_())