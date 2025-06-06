Sistema de Gestion de Pedidos para Tienda Virtual
===============================================

Diseno General
-------------
El sistema esta disenado utilizando Programacion Orientada a Objetos (POO) y esta dividido en los siguientes modulos:

- models.py: Define las clases base (Producto y Pedido) con sus atributos y metodos
- utils.py: Contiene funciones de utilidad para persistencia de datos y validacion de entrada
- store.py: Implementa la logica principal del negocio en la clase TiendaVirtual
- main.py: Punto de entrada del programa y manejo de la interfaz de usuario

Caracteristicas Principales
-------------------------
1. Gestion de productos con tres tipos y sus impuestos:
   - LIBRO: 0% impuesto
   - ELECTRONICO: 16% impuesto
   - ROPA: 8% impuesto

2. Manejo de pedidos:
   - Creacion de pedidos con multiples productos
   - Calculo automatico de impuestos por tipo
   - Validacion de datos de entrada
   - Persistencia en archivo de texto

3. Reportes:
   - Lista detallada de pedidos
   - Reporte de ventas con totales y promedios
   - Estadisticas por tipo de producto

4. Interfaz de usuario:
   - Menu interactivo en consola
   - Validaciones en tiempo real
   - Mensajes de error descriptivos
   - Formato limpio y organizado

Suposiciones y Reglas
--------------------
1. Los precios se manejan como numeros flotantes con 2 decimales
2. Las fechas se almacenan en formato ISO (YYYY-MM-DD HH:MM:SS)
3. Los nombres de cliente no pueden estar vacios
4. Se usa Enter vacio para terminar de agregar productos
5. Todas las entradas se validan antes de procesarse
6. Los pedidos se guardan en formato de texto plano, un pedido por linea
7. Formato de almacenamiento:
   Cliente: [nombre] | Fecha: [fecha] | Productos: [cantidad]x [producto] [tipo] ($[precio]) | Total: $[total]

Instrucciones de Uso
-------------------
1. Asegurese de tener Python 2.7 instalado en su sistema
2. No se requieren librerias adicionales
3. Ejecute el programa:
   python main.py
4. Operaciones disponibles:
   - Crear nuevos pedidos
   - Ver lista de pedidos
   - Consultar reportes de ventas
   - Salir del programa

Los pedidos se guardan automaticamente en 'pedidos.txt' en el directorio del programa.

Compatibilidad y Requisitos
-------------------------
- Compatible con Python 2.7
- No usa sintaxis exclusiva de Python 3
- No requiere librerias externas
- Maneja codificacion UTF-8
- Funciona en Windows y Linux
- Codigo limpio y documentado
- Variables y mensajes sin acentos ni caracteres especiales 