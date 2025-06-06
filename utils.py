#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
import codecs
from datetime import datetime
from models import Producto, Pedido

# Configuración de codificación para Python 2.7
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # Configurar la salida estandar para UTF-8
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

def guardar_pedidos(pedidos, archivo="pedidos.txt"):
    """Guarda pedidos en archivo de texto"""
    with open(archivo, 'w') as f:
        for pedido in pedidos:
            # Formatear productos
            productos_str = []
            for producto, cantidad in pedido.productos:
                productos_str.append("{}x {} {} (${:.2f})".format(
                    cantidad,
                    producto.nombre,
                    producto.tipo,
                    producto.precio_unitario
                ))
            
            # Formato: Cliente | Fecha | Productos | Total
            f.write("Cliente: {} | Fecha: {} | Productos: {} | Total: ${:.2f}\n".format(
                pedido.cliente,
                pedido.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                " + ".join(productos_str),
                pedido.calcular_total()
            ))

def cargar_pedidos(archivo="pedidos.txt"):
    """Lee y reconstruye pedidos desde archivo"""
    pedidos = []
    if not os.path.exists(archivo):
        return pedidos

    try:
        with open(archivo, 'r') as f:
            for linea in f:
                try:
                    # Parsear secciones del pedido
                    secciones = linea.strip().split(" | ")
                    if len(secciones) != 4:
                        continue
                    
                    # Extraer cliente
                    cliente = secciones[0].replace("Cliente: ", "").strip()
                    pedido = Pedido(cliente)
                    
                    # Extraer fecha
                    fecha_str = secciones[1].replace("Fecha: ", "").strip()
                    pedido.fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                    
                    # Reconstruir productos
                    productos_str = secciones[2].replace("Productos: ", "").strip()
                    for prod in productos_str.split(" + "):
                        partes = prod.split()
                        cantidad = int(partes[0].replace("x", ""))
                        tipo = partes[-2]
                        precio = float(partes[-1].strip("()$"))
                        nombre = " ".join(partes[1:-2])
                        
                        producto = Producto(nombre, tipo, precio)
                        pedido.agregar_producto(producto, cantidad)
                    
                    pedidos.append(pedido)
                except Exception as e:
                    print(u"Error al procesar linea: {}".format(str(e)))
                    continue
                
    except Exception as e:
        print(u"Error al cargar pedidos: {}".format(str(e)))
        return []
        
    return pedidos

def validar_numero(valor):
    """Valida y convierte a número positivo"""
    try:
        numero = float(valor)
        if numero <= 0:
            raise ValueError(u"El numero debe ser mayor que cero")
        return numero
    except ValueError:
        raise ValueError(u"Por favor, ingrese un numero valido")

def validar_cantidad(valor):
    """Valida y convierte a entero positivo"""
    try:
        cantidad = int(valor)
        if cantidad <= 0:
            raise ValueError(u"La cantidad debe ser mayor que cero")
        return cantidad
    except ValueError:
        raise ValueError(u"Por favor, ingrese un numero entero positivo")

def solicitar_entrada(mensaje, validacion=None, mensaje_error=None):
    """Solicita y valida entrada del usuario"""
    while True:
        try:
            valor = raw_input(mensaje)
            if not valor.strip():
                raise ValueError(u"El valor no puede estar vacio")
            if validacion:
                return validacion(valor)
            return valor
        except ValueError as e:
            print(u"Error: {}".format(mensaje_error if mensaje_error else str(e)))
            print(u"Por favor, intente nuevamente.")

def solicitar_opcion_menu(opciones, mensaje=u"Seleccione una opcion: "):
    """Solicita opción válida del menú"""
    while True:
        opcion = raw_input(mensaje)
        if opcion in opciones:
            return opcion
        print(u"Error: Opcion no valida")
        print(u"Opciones validas: {}".format(", ".join(opciones)))
        print(u"Por favor, intente nuevamente.") 