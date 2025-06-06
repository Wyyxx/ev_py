# Diagramas del Sistema de Gestión de Pedidos

## 1. Diagrama de Clases

```mermaid
classDiagram
    class Producto {
        +str nombre
        +str tipo
        +float precio_unitario
        +TIPO_LIBRO: str
        +TIPO_ELECTRONICO: str
        +TIPO_ROPA: str
        +IMPUESTOS: dict
        +calcular_precio_con_impuesto()
        +__str__()
    }

    class Pedido {
        +str cliente
        +datetime fecha
        +list productos
        +agregar_producto(producto, cantidad)
        +calcular_total()
        +total_productos()
        +__str__()
    }

    class TiendaVirtual {
        +list pedidos
        +validar_tipo_producto(tipo)
        +crear_producto(nombre, tipo, precio)
        +crear_pedido()
        +ver_pedidos()
        +reporte_ventas()
    }

    class Utils {
        +guardar_pedidos(pedidos, archivo)
        +cargar_pedidos(archivo)
        +validar_numero(valor)
        +validar_cantidad(valor)
        +solicitar_entrada(mensaje, validacion, mensaje_error)
        +solicitar_opcion_menu(opciones, mensaje)
    }

    TiendaVirtual --> Pedido : gestiona
    Pedido --> Producto : contiene
    TiendaVirtual ..> Utils : usa
```

## 2. Diagrama de Flujo

```mermaid
flowchart TD
    A[Inicio] --> B[Cargar Pedidos Existentes]
    B --> C[Mostrar Menú Principal]
    C --> D{Selección Usuario}
    
    D -->|1| E[Crear Pedido]
    D -->|2| F[Ver Pedidos]
    D -->|3| G[Reporte Ventas]
    D -->|4| H[Salir]
    
    E --> E1[Ingresar Cliente]
    E1 --> E2[Agregar Productos]
    E2 --> E3{Más Productos?}
    E3 -->|Sí| E2
    E3 -->|No| E4[Guardar Pedido]
    E4 --> C
    
    F --> F1[Listar Pedidos]
    F1 --> C
    
    G --> G1[Calcular Totales]
    G1 --> G2[Mostrar Estadísticas]
    G2 --> C
    
    H --> I[Fin]
```

## Explicación de los Diagramas

### Diagrama de Clases
- **Producto**: Clase base que representa los productos con sus tipos e impuestos
  - Maneja tres tipos de productos: LIBRO, ELECTRONICO y ROPA
  - Calcula precios con impuestos según el tipo

- **Pedido**: Gestiona la información de un pedido y sus productos
  - Mantiene lista de productos y cantidades
  - Calcula totales y gestiona información del cliente

- **TiendaVirtual**: Clase principal que coordina todas las operaciones
  - Gestiona la creación y visualización de pedidos
  - Genera reportes de ventas

- **Utils**: Módulo con funciones de utilidad
  - Maneja persistencia de datos
  - Proporciona validaciones y entrada de usuario

### Diagrama de Flujo
1. **Inicio y Carga**
   - El programa inicia cargando pedidos existentes
   - Presenta menú principal

2. **Operaciones Principales**
   - Crear Pedido: Flujo de creación de nuevos pedidos
   - Ver Pedidos: Visualización de pedidos existentes
   - Reporte Ventas: Generación de estadísticas
   - Salir: Finalización del programa

3. **Ciclo de Vida**
   - Todas las operaciones regresan al menú principal
   - El programa continúa hasta que el usuario elige salir

## Características del Sistema

1. **Persistencia**
   - Almacenamiento en archivo de texto
   - Carga y guardado automático

2. **Validación**
   - Entrada de usuario validada
   - Manejo de errores robusto

3. **Reportes**
   - Totales de ventas
   - Estadísticas por tipo de producto
   - Pedido más grande

4. **Interfaz**
   - Menú basado en consola
   - Navegación intuitiva
   - Mensajes claros al usuario 