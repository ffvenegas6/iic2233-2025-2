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
            # Actualizamos y mostramos tableros resueltos
            self.dccasillas.tableros_resueltos = sum(
                1 for tablero in self.dccasillas.tableros if tablero.estado
            )
            print(f"Tableros resueltos: {self.dccasillas.tableros_resueltos}\n")
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
        # Revisamos si se cargaron tableros correctamente
        if self.dccasillas.tableros:
            # Seleccionamos el primer tablero
            self.dccasillas.abrir_tablero(0)
            # Pasamos al menú de acciones
            self.menu_acciones.mostrar_menu(self.dccasillas)
        else:
            print("No se pudo iniciar el juego. Intente nuevamente.")
            self.dccasillas = None
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

    def __init__(self) -> None:
        self.opciones: List[str] = [
            "Mostrar tablero",
            "Habilitar/deshabilitar casilla",
            "Verificar solución",
            "Encontrar solución",
            "Volver al menú de Juego"
        ]
        self.opcion_actual: int = -1


    def selector_opciones(self, dccasillas: DCCasillas=None) -> int:
        # Función para mostrar el menú de acciones
        print("\nDCCasillas")
        if not dccasillas:
            print("Usuario: UUU, Puntaje: PPP")
            print("Número de tablero: XXX de YYY")
            print("Movimientos tablero: ppp\n")
        else:
            print((f"Usuario: {dccasillas.usuario}, "
                   f"Puntaje: {dccasillas.puntaje}"))
            print(f"Número de tablero: {dccasillas.tablero_actual} de {dccasillas.num_tableros}")
            tablero: Tablero = dccasillas.tableros[dccasillas.tablero_actual]
            print(f"Movimientos tablero: {tablero.movimientos}\n")
        # Desplegamos opciones
        msg = mostrar_opciones("Menú de Acciones", self.opciones)
        opcion: int = int(input(msg))
        # Validamos opción
        while opcion < 1 or opcion > len(self.opciones):
            print("\nOpción inválida. Intente nuevamente.\n")
            opcion = int(input())
        return opcion

    def mostrar_menu(self, dccasillas: DCCasillas) -> None:
        # Mostramos en loop mientras usuario no seleccione última opción
        while self.opcion_actual != len(self.opciones) - 1:
            opcion = self.selector_opciones(dccasillas)
            self.opcion_actual = opcion - 1
            self.ejecutar_opcion(opcion, dccasillas)
        # Si selecciona última opción, reseteamos opción actual y volvemos
        self.opcion_actual = -1
        print("Volviendo al Menú de Juego!\n")

    def ejecutar_opcion(self, opcion:int, dccasillas: DCCasillas=None) -> None:
        print(f"\nOpción [{opcion}]: {self.opciones[self.opcion_actual]}\n")
        if opcion == 1:
            self.mostrar_tablero(dccasillas)
        elif opcion == 2:
            self.cambiar_casillas(dccasillas)
        elif opcion == 3:
            self.verificar_solucion(dccasillas)
        elif opcion == 4:
            self.encontrar_solucion(dccasillas)

    def mostrar_tablero(self, dccasillas: DCCasillas=None) -> None:
        tablero: Tablero = dccasillas.tableros[dccasillas.tablero_actual]
        tablero.mostrar_tablero()
        return

    def cambiar_casillas(self, dccasillas: DCCasillas=None) -> None:
        fila: int = int(input("Ingrese la fila de la casilla a modificar: "))
        columna: int = int(input("Ingrese la columna de la casilla a modificar: "))
        tablero_actual: int = dccasillas.tablero_actual
        success: bool = dccasillas.tableros[tablero_actual].modificar_casilla(fila, columna)
        if success:
            print("Casilla modificada exitosamente.")
            self.mostrar_tablero(dccasillas)
        else:
            print("Error al modificar la casilla. Verifique las coordenadas.")
        return

    def verificar_solucion(self, dccasillas: DCCasillas=None) -> int:
        success: bool = dccasillas.tableros[dccasillas.tablero_actual].validar()
        if success:
            print("La solución es válida.")
            movimientos_tablero = dccasillas.tableros[dccasillas.tablero_actual].movimientos
            dccasillas.puntaje += movimientos_tablero
            print(f"Sumando puntaje: {movimientos_tablero}")
            print(f"Nuevo puntaje: {dccasillas.puntaje}")
        else:
            print("La solución no es válida.")
        return

    def encontrar_solucion(self, dccasillas: DCCasillas=None) -> None:
        dccasillas.tableros[dccasillas.tablero_actual].encontrar_solucion()
        return

if __name__ == "__main__":
    menu = MenuJuego()
    menu.mostrar_menu()
