import sys
import codecs
from store import TiendaVirtual
from utils import solicitar_opcion_menu

# Configurar la codificacion para la salida en Python 2
if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    # Configurar la salida estandar para UTF-8
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

def mostrar_menu():
    """Muestra el menu principal"""
    print(u"\n\n")
    print(u"Sistema de Gestion de Pedidos")
    print(u"=" * 30)
    print(u"\n1. Crear nuevo pedido")
    print(u"2. Ver pedidos")
    print(u"3. Reporte de ventas")
    print(u"4. Salir")
    print(u"\n")
    return solicitar_opcion_menu(["1", "2", "3", "4"])

def main():
    """Funcion principal del programa"""
    try:
        tienda = TiendaVirtual()
        
        while True:
            try:
                opcion = mostrar_menu()
                
                if opcion == "1":
                    tienda.crear_pedido()
                elif opcion == "2":
                    tienda.ver_pedidos()
                elif opcion == "3":
                    tienda.reporte_ventas()
                elif opcion == "4":
                    print(u"\n\nGracias por usar el sistema!")
                    break
            except ValueError as e:
                print(u"\n\nError de validacion: {}".format(str(e)))
                print(u"Por favor, intente nuevamente.")
            except Exception as e:
                print(u"\n\nError inesperado: {}".format(str(e)))
                print(u"Por favor, intente nuevamente.")
                
    except KeyboardInterrupt:
        print(u"\n\nPrograma interrumpido por el usuario.")
    except Exception as e:
        print(u"\n\nError critico: {}".format(str(e)))
        print(u"El programa se cerrara.")
        sys.exit(1)

if __name__ == "__main__":
    main() 