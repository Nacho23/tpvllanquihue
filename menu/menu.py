# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Sat Nov 11 12:47:41 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1440, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lb_nombre = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.lb_nombre.setFont(font)
        self.lb_nombre.setObjectName("lb_nombre")
        self.horizontalLayout_4.addWidget(self.lb_nombre)
        self.lb_apellido = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(13)
        self.lb_apellido.setFont(font)
        self.lb_apellido.setObjectName("lb_apellido")
        self.horizontalLayout_4.addWidget(self.lb_apellido)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.lb_rut = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(8)
        self.lb_rut.setFont(font)
        self.lb_rut.setObjectName("lb_rut")
        self.horizontalLayout_5.addWidget(self.lb_rut)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_codigo = QtGui.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.le_codigo.setFont(font)
        self.le_codigo.setInputMask("")
        self.le_codigo.setReadOnly(False)
        self.le_codigo.setPlaceholderText("")
        self.le_codigo.setObjectName("le_codigo")
        self.horizontalLayout.addWidget(self.le_codigo)
        self.btn_buscar_producto = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_buscar_producto.setFont(font)
        self.btn_buscar_producto.setObjectName("btn_buscar_producto")
        self.horizontalLayout.addWidget(self.btn_buscar_producto)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lb_precio_total = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(34)
        font.setWeight(75)
        font.setBold(True)
        self.lb_precio_total.setFont(font)
        self.lb_precio_total.setLineWidth(1)
        self.lb_precio_total.setMargin(20)
        self.lb_precio_total.setIndent(-4)
        self.lb_precio_total.setObjectName("lb_precio_total")
        self.verticalLayout_2.addWidget(self.lb_precio_total)
        self.btn_pagar = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.btn_pagar.setFont(font)
        self.btn_pagar.setIconSize(QtCore.QSize(20, 20))
        self.btn_pagar.setShortcut("Ctrl+F")
        self.btn_pagar.setAutoDefault(False)
        self.btn_pagar.setDefault(False)
        self.btn_pagar.setFlat(False)
        self.btn_pagar.setObjectName("btn_pagar")
        self.verticalLayout_2.addWidget(self.btn_pagar)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tw_lista_productos = QtGui.QTableWidget(self.centralwidget)
        self.tw_lista_productos.setEnabled(True)
        self.tw_lista_productos.setColumnCount(0)
        self.tw_lista_productos.setObjectName("tw_lista_productos")
        self.tw_lista_productos.setColumnCount(0)
        self.tw_lista_productos.setRowCount(0)
        self.tw_lista_productos.horizontalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tw_lista_productos)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_quitar_producto = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_quitar_producto.setFont(font)
        self.btn_quitar_producto.setObjectName("btn_quitar_producto")
        self.horizontalLayout_2.addWidget(self.btn_quitar_producto)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btn_cambiar_cantidad = QtGui.QPushButton(self.centralwidget)
        self.btn_cambiar_cantidad.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btn_cambiar_cantidad.setFont(font)
        self.btn_cambiar_cantidad.setObjectName("btn_cambiar_cantidad")
        self.horizontalLayout_2.addWidget(self.btn_cambiar_cantidad)
        self.btn_mas = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_mas.setFont(font)
        self.btn_mas.setObjectName("btn_mas")
        self.horizontalLayout_2.addWidget(self.btn_mas)
        self.btn_menos = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_menos.setFont(font)
        self.btn_menos.setObjectName("btn_menos")
        self.horizontalLayout_2.addWidget(self.btn_menos)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 26))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuInventario = QtGui.QMenu(self.menubar)
        self.menuInventario.setObjectName("menuInventario")
        self.menuInformes = QtGui.QMenu(self.menubar)
        self.menuInformes.setObjectName("menuInformes")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_inventario = QtGui.QAction(MainWindow)
        self.actionAbrir_inventario.setObjectName("actionAbrir_inventario")
        self.actionGenerar_Informe_Diario = QtGui.QAction(MainWindow)
        self.actionGenerar_Informe_Diario.setObjectName("actionGenerar_Informe_Diario")
        self.actionMostrar_Resumen = QtGui.QAction(MainWindow)
        self.actionMostrar_Resumen.setObjectName("actionMostrar_Resumen")
        self.menuInventario.addAction(self.actionAbrir_inventario)
        self.menuInformes.addAction(self.actionGenerar_Informe_Diario)
        self.menuInformes.addSeparator()
        self.menuInformes.addAction(self.actionMostrar_Resumen)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuInventario.menuAction())
        self.menubar.addAction(self.menuInformes.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.le_codigo, self.btn_buscar_producto)
        MainWindow.setTabOrder(self.btn_buscar_producto, self.btn_pagar)
        MainWindow.setTabOrder(self.btn_pagar, self.btn_quitar_producto)
        MainWindow.setTabOrder(self.btn_quitar_producto, self.btn_cambiar_cantidad)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_nombre.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_apellido.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_rut.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar_producto.setText(QtGui.QApplication.translate("MainWindow", "BUSCAR", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar_producto.setShortcut(QtGui.QApplication.translate("MainWindow", "Return", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "IMAGEN", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "TOTAL", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_precio_total.setText(QtGui.QApplication.translate("MainWindow", "$0", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_pagar.setToolTip(QtGui.QApplication.translate("MainWindow", "Finaliza la venta", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_pagar.setText(QtGui.QApplication.translate("MainWindow", "PAGAR", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quitar_producto.setToolTip(QtGui.QApplication.translate("MainWindow", "Elimina producto de la lista", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quitar_producto.setText(QtGui.QApplication.translate("MainWindow", "QUITAR PRODUCTO", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quitar_producto.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cambiar_cantidad.setText(QtGui.QApplication.translate("MainWindow", "CAMBIAR CANTIDAD", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cambiar_cantidad.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_mas.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_menos.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInventario.setTitle(QtGui.QApplication.translate("MainWindow", "Inventario", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInformes.setTitle(QtGui.QApplication.translate("MainWindow", "Informes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir_inventario.setText(QtGui.QApplication.translate("MainWindow", "Abrir Inventario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerar_Informe_Diario.setText(QtGui.QApplication.translate("MainWindow", "Generar Informe Diario", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMostrar_Resumen.setText(QtGui.QApplication.translate("MainWindow", "Mostrar Resumen", None, QtGui.QApplication.UnicodeUTF8))
