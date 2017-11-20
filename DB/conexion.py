#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as sql
import sys

class Conexion():

	def conectarBD(self):
		conect = sql.connect('C:/Users/naxo_/Google Drive/BDTPVLLANQ/bdtpvllanq.db')
		return conect