CREATE TABLE `Cuenta` (
  `rut` VARCHAR(10) NOT NULL,
  `contrasena` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`rut`),
  CONSTRAINT `rut`
    FOREIGN KEY (`rut`)
    REFERENCES `Trabajador` (`rut`));
;
CREATE TABLE `Producto` (
  `codigo` INT NOT NULL,
  `descripcion` VARCHAR(100) NOT NULL,
  `categoria` VARCHAR(45) NULL,
  `precio` INT NOT NULL,
  `proveedor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo`));
;
CREATE TABLE `Ingreso` (
  `idIngreso` INT NOT NULL,
  `rut` VARCHAR(10) NOT NULL,
  `fecha` DATETIME NOT NULL,
  PRIMARY KEY (`idIngreso`),
  CONSTRAINT `rut`
    FOREIGN KEY (`rut`)
    REFERENCES `Trabajador` (`rut`));
;
CREATE TABLE `Venta` (
  `idVenta` INT NOT NULL,
  `fecha` DATETIME NULL,
  `rutTrabajador` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idVenta`),
  CONSTRAINT `rutTrabajador`
    FOREIGN KEY (`rutTrabajador`)
    REFERENCES `Trabajador` (`rut`));
;
CREATE TABLE `Inventario` (
  `idInventario` INT NOT NULL,
  `codigoProducto` INT NOT NULL,
  `stock` INT NULL,
  PRIMARY KEY (`idInventario`),
  CONSTRAINT `codigoProducto`
    FOREIGN KEY (`codigoProducto`)
    REFERENCES `Producto` (`codigo`));
;
CREATE TABLE `venta_producto` (
  `idVenta` INT NOT NULL,
  `codigoProducto` INT NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`idVenta`, `codigoProducto`),
  CONSTRAINT `idVenta`
    FOREIGN KEY (`idVenta`)
    REFERENCES `Venta` (`idVenta`),
  CONSTRAINT `codigoProducto`
    FOREIGN KEY (`codigoProducto`)
    REFERENCES `Producto` (`codigo`));
;
CREATE TABLE `Modifica` (
  `idModifica` INT NOT NULL,
  `rutTrabajador` VARCHAR(10) NOT NULL,
  `idInventario` INT NOT NULL,
  `codigoProducto` INT NOT NULL,
  `accion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idModifica`),
  CONSTRAINT `rutTrabajador`
    FOREIGN KEY (`rutTrabajador`)
    REFERENCES `Trabajador` (`rut`),
  CONSTRAINT `idInventario`
    FOREIGN KEY (`idInventario`)
    REFERENCES `Inventario` (`idInventario`),
  CONSTRAINT `codigoProducto`
    FOREIGN KEY (`codigoProducto`)
    REFERENCES `Producto` (`codigo`));
;
CREATE TABLE `Informe` (
  `idInforme` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `ingresoTotal` INT NOT NULL,
  `ganancia` INT NOT NULL,
  `rutTrabajador` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`idInforme`),
  CONSTRAINT `rutTrabajador`
    FOREIGN KEY (`rutTrabajador`)
    REFERENCES`Trabajador` (`rut`));
;
CREATE TABLE trabajador (
    "rut" VARCHAR(10) NOT NULL,
    "nombre" VARCHAR(45) NOT NULL,
    "email" VARCHAR(100)
, "apellido" TEXT);
