import os
import json
import sys
import codecs
from datetime import datetime
from models import Producto, Pedido

# Configurar la codificacion para la salida en Python 2
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # Configurar la salida estandar para UTF-8
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

def guardar_pedidos(pedidos, archivo="pedidos.txt"):
    """
    Guarda la lista de pedidos en un archivo de texto, un pedido por linea
    
    Args:
        pedidos (list): Lista de pedidos a guardar
        archivo (str): Ruta del archivo donde guardar los pedidos
    """
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
            
            # Escribir el pedido en una sola linea
            f.write("Cliente: {} | Fecha: {} | Productos: {} | Total: ${:.2f}\n".format(
                pedido.cliente,
                pedido.fecha.strftime("%Y-%m-%d %H:%M:%S"),
                " + ".join(productos_str),
                pedido.calcular_total()
            ))

def cargar_pedidos(archivo="pedidos.txt"):
    """
    Carga la lista de pedidos desde un archivo de texto
    
    Args:
        archivo (str): Ruta del archivo de pedidos
        
    Returns:
        list: Lista de objetos Pedido
    """
    pedidos = []
    if not os.path.exists(archivo):
        return pedidos

    try:
        with open(archivo, 'r') as f:
            for linea in f:
                try:
                    # Dividir la línea en secciones
                    secciones = linea.strip().split(" | ")
                    if len(secciones) != 4:
                        continue
                    
                    # Procesar cliente
                    cliente = secciones[0].replace("Cliente: ", "").strip()
                    pedido = Pedido(cliente)
                    
                    # Procesar fecha
                    fecha_str = secciones[1].replace("Fecha: ", "").strip()
                    pedido.fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                    
                    # Procesar productos
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
    """
    Valida que un valor sea un numero valido
    
    Args:
        valor (str): El valor a validar
        
    Returns:
        float: El numero convertido si es valido
        
    Raises:
        ValueError: Si el valor no es un numero valido
    """
    try:
        numero = float(valor)
        if numero <= 0:
            raise ValueError(u"El numero debe ser mayor que cero")
        return numero
    except ValueError:
        raise ValueError(u"Por favor, ingrese un numero valido")

def validar_cantidad(valor):
    """
    Valida que un valor sea una cantidad valida (entero positivo)
    
    Args:
        valor (str): El valor a validar
        
    Returns:
        int: La cantidad convertida si es valida
        
    Raises:
        ValueError: Si el valor no es una cantidad valida
    """
    try:
        cantidad = int(valor)
        if cantidad <= 0:
            raise ValueError(u"La cantidad debe ser mayor que cero")
        return cantidad
    except ValueError:
        raise ValueError(u"Por favor, ingrese un numero entero positivo")

def solicitar_entrada(mensaje, validacion=None, mensaje_error=None):
    """
    Solicita entrada al usuario hasta que sea valida
    
    Args:
        mensaje (str): Mensaje para solicitar la entrada
        validacion (callable): Funcion de validacion a aplicar (opcional)
        mensaje_error (str): Mensaje de error personalizado (opcional)
        
    Returns:
        El valor validado
    """
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
    """
    Solicita una opcion de menu hasta que sea valida
    
    Args:
        opciones (list): Lista de opciones validas
        mensaje (str): Mensaje para solicitar la entrada
        
    Returns:
        str: La opcion seleccionada
    """
    while True:
        opcion = raw_input(mensaje)
        if opcion in opciones:
            return opcion
        print(u"Error: Opcion no valida")
        print(u"Opciones validas: {}".format(", ".join(opciones)))
        print(u"Por favor, intente nuevamente.") 