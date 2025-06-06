#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

class Producto(object):
    """Representa un producto con su tipo e impuesto asociado"""
    
    TIPO_LIBRO = "LIBRO"
    TIPO_ELECTRONICO = "ELECTRONICO"
    TIPO_ROPA = "ROPA"
    
    # Impuestos por tipo de producto
    IMPUESTOS = {
        TIPO_LIBRO: 0.0,        # Libros sin impuesto
        TIPO_ELECTRONICO: 0.16, # Electrónicos 16%
        TIPO_ROPA: 0.08         # Ropa 8%
    }
    
    def __init__(self, nombre, tipo, precio_unitario):
        """Crea un producto con nombre, tipo y precio"""
        if not isinstance(nombre, basestring):
            raise ValueError(u"El nombre debe ser una cadena de texto")
        if not isinstance(tipo, basestring):
            raise ValueError(u"El tipo debe ser una cadena de texto")
        
        self.nombre = nombre
        tipo = tipo.upper()
        if tipo not in self.IMPUESTOS:
            raise ValueError(u"Tipo de producto no valido")
        self.tipo = tipo
        
        try:
            precio_unitario = float(precio_unitario)
            if precio_unitario <= 0:
                raise ValueError()
        except (TypeError, ValueError):
            raise ValueError(u"El precio debe ser un numero positivo")
        self.precio_unitario = precio_unitario
    
    def calcular_precio_con_impuesto(self):
        """Retorna el precio final con impuesto aplicado"""
        impuesto = self.IMPUESTOS.get(self.tipo, 0.0)
        return round(self.precio_unitario * (1 + impuesto), 2)
    
    def __str__(self):
        return "{} ({}) - ${:.2f} (con impuesto: ${:.2f})".format(
            self.nombre, 
            self.tipo, 
            self.precio_unitario,
            self.calcular_precio_con_impuesto()
        )

class Pedido(object):
    """Representa un pedido con sus productos y cantidades"""
    
    def __init__(self, cliente, productos=None):
        """Crea un pedido para un cliente"""
        self.cliente = cliente
        self.fecha = datetime.now()
        self.productos = productos if productos else []  # Lista de (Producto, cantidad)
    
    def agregar_producto(self, producto, cantidad=1):
        """Añade un producto al pedido"""
        self.productos.append((producto, cantidad))
    
    def calcular_total(self):
        """Calcula el total incluyendo impuestos"""
        total = 0.0
        for producto, cantidad in self.productos:
            total += producto.calcular_precio_con_impuesto() * cantidad
        return round(total, 2)
    
    def total_productos(self):
        """Retorna cantidad total de items"""
        return sum(cantidad for _, cantidad in self.productos)
    
    def __str__(self):
        productos_str = "\n".join(
            "  - {} x {} = ${:.2f}".format(
                str(p), 
                c, 
                p.calcular_precio_con_impuesto() * c
            ) for p, c in self.productos
        )
        return """
Pedido de: {}
Fecha: {}
Productos:
{}
Total productos: {}
Total a pagar: ${:.2f}
""".format(
            self.cliente,
            self.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            productos_str,
            self.total_productos(),
            self.calcular_total()
        ) 