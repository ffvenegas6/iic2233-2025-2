import sys
from dccasillas import DCCasillas
from tablero import Tablero
from typing import List

def mostrar_opciones(encabezado: str, opciones: List[str]) -> str:
    print("*" * 3 + f" {encabezado} " + "*" * 3 + "\n")
    for i in range(len(opciones)):
        print(f"[{i + 1}] {opciones[i]}")
    msg = ("\nIndique su opción "
            f"({', '.join(str(i + 1) for i in range(len(opciones)))}): ")
    return msg

class MenuJuego:

    def __init__(self) -> None:
        self.dccasillas: DCCasillas = None
        self.opciones: List[str] = [
            "Iniciar juego",
            "Continuar juego",
            "Guardar estado de juego",
            "Recuperar estado de juego",
            "Salir del programa"
        ]
        self.opcion_actual: int = -1
        self.menu_acciones = MenuAcciones()
        
    def selector_opciones(self) -> int:
        print("\n¡Bienvenido a DCCasillas!\n")
        if not self.dccasillas:
            print("Usuario: UUU, Puntaje: PPP")
            print("Tableros resueltos: TTT\n")
        else:
            print((f"Usuario: {self.dccasillas.usuario}, "
                   f"Puntaje: {self.dccasillas.puntaje}"))
            print("Tableros resueltos: TTT\n")
        # Desplegamos opciones
        msg = mostrar_opciones("Menú de Juego", self.opciones)
        opcion: int = int(input(msg))
        # Validamos opción
        while opcion < 1 or opcion > len(self.opciones):
            print("\nOpción inválida. Intente nuevamente.\n")
            opcion = int(input())
        return opcion

    def ejecutar_opcion(self, opcion:int) -> None:
        print(f"\nOpción [{opcion}]: {self.opciones[self.opcion_actual]}\n")
        if opcion == 1:
            self.iniciar_juego()
        elif opcion == 2:
            self.continuar_juego()
        elif opcion == 3:
            self.guardar_juego()
        elif opcion == 4:
            self.recuperar_estado()

    def mostrar_menu(self) -> None:
        # Mostramos en loop mientras usuario no seleccione última opción
        while self.opcion_actual != len(self.opciones) - 1:
            opcion = self.selector_opciones()
            self.opcion_actual = opcion - 1
            self.ejecutar_opcion(opcion)
        # Si selecciona última opción, salimos
        print("Saliendo del programa. ¡Hasta luego!\n")
        sys.exit(0)

    def iniciar_juego(self) -> None:
        # Si no hay usuario, pedimos uno
        if not self.dccasillas:
            usuario: str = input("Ingrese su nombre de usuario: ")
        # Si ya había, le damos la opción de cambiarlo
        else:
            usuario: str = input("Ingrese su nuevo nombre de usuario (si desea cambiarlo): ")
        # Pedimos el archivo de configuración
        config: str = input("Ingrese el nombre del archivo de configuración: ")
        # Creamos nueva instancia de DCCasillas
        self.dccasillas = DCCasillas(usuario, config)
        # Seleccionamos el primer tablero
        self.dccasillas.abrir_tablero(0)
        # Pasamos al menú de acciones
        self.menu_acciones.mostrar_menu(self.dccasillas)
        return

    def continuar_juego(self) -> None:
        if not self.dccasillas:
            print("No hay juego en curso. Inicie un nuevo juego primero.")
            return
        # Pedimos mantener tablero actual o cambiar
        cambiar: str = input(f"¿Desea cambiar el tablero actual [{self.dccasillas.tablero_actual}]? (y/n): ")
        if cambiar.lower() == 'y':
            tablero: int = int(input("Ingrese el número de tablero a abrir: "))
            self.dccasillas.abrir_tablero(tablero)
            # Pasamos al menú de acciones
            self.menu_acciones.mostrar_menu(self.dccasillas)
        elif cambiar.lower() == 'n':
            # Pasamos al menú de acciones
            self.menu_acciones.mostrar_menu(self.dccasillas)
        else:
            print("Opción inválida. Regresando al menú principal.")
        return
            
    def guardar_juego(self) -> None:
        if not self.dccasillas:
            print("No hay juego en curso. Inicie un nuevo juego primero.")
            return
        else:
            print("Guardando estado de juego...")
            success: bool = self.dccasillas.guardar_estado()
            if success:
                print("Estado de juego guardado exitosamente.")
            else:
                print("Error al guardar el estado de juego.")
            return

    def recuperar_estado(self) -> None:
        if not self.dccasillas:
            print("No hay juego en curso. Inicie un nuevo juego primero.")
            return
        else:
            print("Recuperando estado de juego...")
            success: bool = self.dccasillas.recuperar_estado()
            if success:
                print("Estado de juego recuperado exitosamente.")
            else:
                print("Error al recuperar el estado de juego.")
            return


class MenuAcciones:

    def __init__(self, dccasillas: DCCasillas) -> None:
        self.dccasillas = dccasillas
        self.opciones: List[str] = [
            "Mostrar tablero",
            "Habilitar/deshabilitar casilla",
            "Verificar solución",
            "Encontrar solución",
            "Volver al menú de Juego"
        ]
        self.opcion_actual: int = -1
        self.usuario: str = None
        self.puntaje: int = 0
        self.tablero_actual: int = None
        self.tableros: List = None
        self.tablero: Tablero = None

    def actualizar_dccasillas(self, dccasillas: DCCasillas) -> None:
        self.dccasillas: DCCasillas = dccasillas
        self.usuario: str = dccasillas.usuario
        self.puntaje: int = dccasillas.puntaje
        self.tablero_actual: int = dccasillas.tablero_actual
        self.tableros: List = dccasillas.tableros
        self.tablero: Tablero = dccasillas.tableros[dccasillas.tablero_actual]

    def selector_opciones(self) -> int:
        # Función para mostrar el menú de acciones
        print("\nDCCasillas")
        if not self.dccasillas:
            print("Usuario: UUU, Puntaje: PPP")
            print("Número de tablero: XXX de YYY")
            print("Movimientos tablero: ppp\n")
        else:
            print((f"Usuario: {self.usuario}, "
                   f"Puntaje: {self.puntaje}"))
            print(f"Número de tablero: {self.tablero_actual} de {len(self.tableros)}")
            print(f"Movimientos tablero: {self.tablero.movimientos}\n")
        # Desplegamos opciones
        msg = mostrar_opciones("Menú de Acciones", self.opciones)
        opcion: int = int(input(msg))
        # Validamos opción
        while opcion < 1 or opcion > len(self.opciones):
            print("\nOpción inválida. Intente nuevamente.\n")
            opcion = int(input())
        return opcion

    def mostrar_menu(self, dccasillas: DCCasillas) -> None:
        # Actualizamos dccasillas
        self.actualizar_dccasillas(dccasillas)
        # Mostramos en loop mientras usuario no seleccione última opción
        while self.opcion_actual != len(self.opciones) - 1:
            opcion = self.selector_opciones()
            self.opcion_actual = opcion - 1
            self.ejecutar_opcion(opcion)
        # Si selecciona última opción, salimos
        print("Volviendo al Menú de Juego!\n")

    def ejecutar_opcion(self, opcion:int) -> None:
        print(f"\nOpción [{opcion}]: {self.opciones[self.opcion_actual]}\n")
        if opcion == 1:
            self.mostrar_tablero()
        elif opcion == 2:
            self.cambiar_casillas()
        elif opcion == 3:
            self.verificar_solucion()
        elif opcion == 4:
            self.encontrar_solucion()

    def mostrar_tablero(self) -> None:
        self.tablero.mostrar_tablero()
        return
    
    def cambiar_casillas(self) -> None:
        fila: int = int(input("Ingrese la fila de la casilla a modificar: "))
        columna: int = int(input("Ingrese la columna de la casilla a modificar: "))
        success: bool = self.tablero.modificar_casilla(fila, columna)
        if success:
            print("Casilla modificada exitosamente.")
            self.mostrar_tablero()
        else:
            print("Error al modificar la casilla. Verifique las coordenadas.")
        return

    def verificar_solucion(self) -> int:
        success: bool = self.tablero.validar()
        if success:
            print("La solución es válida.")
        else:
            print("La solución no es válida.")
        return
    
    def encontrar_solucion(self) -> None:
        self.tablero.encontrar_solucion()
        return

if __name__ == "__main__":
    menu = MenuJuego()
    menu.mostrar_menu()
