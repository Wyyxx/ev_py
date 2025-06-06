#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import Producto, Pedido
from utils import guardar_pedidos, cargar_pedidos

class TiendaVirtual(object):
    """Gestiona operaciones de la tienda: pedidos, productos y reportes"""
    
    def __init__(self):
        """Inicializa la tienda cargando pedidos existentes"""
        self.pedidos = cargar_pedidos()
    
    def validar_tipo_producto(self, tipo):
        """Valida y normaliza el tipo de producto"""
        if not isinstance(tipo, basestring):
            raise ValueError(u"El tipo debe ser una cadena de texto")
            
        tipos_validos = [Producto.TIPO_LIBRO, Producto.TIPO_ELECTRONICO, Producto.TIPO_ROPA]
        tipo = tipo.upper()
        if tipo not in tipos_validos:
            raise ValueError(u"Tipo de producto no valido. Tipos validos: {}".format(
                ", ".join(tipos_validos)))
        return tipo
    
    def crear_producto(self, nombre, tipo, precio):
        """Crea un nuevo producto validando sus datos"""
        tipo_validado = self.validar_tipo_producto(tipo)
        return Producto(nombre, tipo_validado, precio)
    
    def crear_pedido(self):
        """Interfaz para crear un nuevo pedido"""
        print(u"\n\nCrear nuevo pedido")
        print(u"-" * 20)
        
        while True:
            cliente = raw_input(u"\nNombre del cliente: ").strip()
            if not cliente:
                print(u"\nError: El nombre del cliente no puede estar vacio.")
                print(u"Por favor, ingrese un nombre valido.")
                continue
            break
        
        pedido = Pedido(cliente)
        
        while True:
            print(u"\n\nAgregar producto al pedido:")
            nombre = raw_input(u"\nNombre del producto (presione Enter para terminar): ").strip()
            if not nombre:
                break
            
            print(u"\nTipos de producto disponibles:")
            print(u"1. LIBRO")
            print(u"2. ELECTRONICO")
            print(u"3. ROPA")
            
            tipos = {
                "1": Producto.TIPO_LIBRO,
                "2": Producto.TIPO_ELECTRONICO,
                "3": Producto.TIPO_ROPA
            }
            
            while True:
                tipo_opcion = raw_input(u"\nSeleccione el tipo (1-3): ")
                if tipo_opcion in tipos:
                    tipo = tipos[tipo_opcion]
                    break
                print(u"\nError: Opcion no valida")
            
            while True:
                try:
                    precio = float(raw_input(u"\nPrecio unitario: $"))
                    if precio <= 0:
                        raise ValueError()
                    break
                except ValueError:
                    print(u"\nError: El precio debe ser un numero positivo")
            
            while True:
                try:
                    cantidad = int(raw_input(u"\nCantidad: "))
                    if cantidad <= 0:
                        raise ValueError()
                    break
                except ValueError:
                    print(u"\nError: La cantidad debe ser un numero entero positivo")
            
            producto = self.crear_producto(nombre, tipo, precio)
            pedido.agregar_producto(producto, cantidad)
            print(u"\nProducto agregado exitosamente!")
            print(u"Subtotal actual: ${:.2f}".format(pedido.calcular_total()))
        
        if pedido.productos:
            self.pedidos.append(pedido)
            guardar_pedidos(self.pedidos)
            print(u"\n\nPedido creado exitosamente!")
            print(pedido)
        else:
            print(u"\n\nEl pedido fue cancelado (no se agregaron productos)")
    
    def ver_pedidos(self):
        """Muestra lista de pedidos existentes"""
        if not self.pedidos:
            print(u"\n\nNo hay pedidos registrados")
            return
            
        print(u"\n\nLista de Pedidos")
        print(u"-" * 20)
        for i, pedido in enumerate(self.pedidos, 1):
            print(u"\nPedido #{}".format(i))
            print(pedido)
    
    def reporte_ventas(self):
        """Genera reporte con estadísticas de ventas"""
        if not self.pedidos:
            print(u"\n\nNo hay ventas registradas")
            return
            
        total_ventas = sum(p.calcular_total() for p in self.pedidos)
        num_pedidos = len(self.pedidos)
        promedio = total_ventas / num_pedidos if num_pedidos > 0 else 0
        
        # Encontrar pedido con mayor monto
        pedido_mayor = max(self.pedidos, key=lambda p: p.calcular_total())
        
        # Calcular ventas por tipo
        ventas_por_tipo = {
            Producto.TIPO_LIBRO: 0.0,
            Producto.TIPO_ELECTRONICO: 0.0,
            Producto.TIPO_ROPA: 0.0
        }
        
        for pedido in self.pedidos:
            for producto, cantidad in pedido.productos:
                ventas_por_tipo[producto.tipo] += producto.calcular_precio_con_impuesto() * cantidad
        
        print(u"\n\nReporte de Ventas")
        print(u"-" * 50)
        print(u"Total de pedidos: {}".format(num_pedidos))
        print(u"Total de ventas: ${:.2f}".format(total_ventas))
        print(u"Promedio por pedido: ${:.2f}".format(promedio))
        print(u"\nVentas por tipo de producto:")
        for tipo, total in ventas_por_tipo.items():
            print(u"  {}: ${:.2f}".format(tipo, total))
        print(u"\nPedido mas grande:")
        print(pedido_mayor) 