# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="TPVLLANQUIHUE", 
 version="1.0", 
 description="Breve descripcion", 
 author="Fingers Valdivia", 
 author_email="valdiviafingers@gmail.com", 
 url="url del proyecto", 
 license="pagada", 
 scripts=["index.py"], 
 console=["index.py"],
 options={'py2exe': 
 	{
 		'bundle_files': 1, 
 		'dll_excludes': ["MSVCP90.dll", "HID.DLL", "w9xpopen.exe"],
 		'includes': ['PySide.QtNetwork']
 	}
 },
 zipfile=None)