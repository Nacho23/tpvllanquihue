#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from login.vista_login import Login
from PySide import QtGui

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    login = Login()
    login.show()
    app.setStyleSheet(open("estilos.qss","r").read())
sys.exit(app.exec_())