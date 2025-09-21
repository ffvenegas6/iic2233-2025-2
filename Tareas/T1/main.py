import sys
from dccasillas import DCCasillas
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

        msg = mostrar_opciones("Menú de Juego", self.opciones)
        opcion: int = int(input(msg))
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
        # # Intentamos cargar la configuracion indicada
        # carga_correcta: bool = False
        # while not carga_correcta:
        # Pedimos el archivo de configuración
        config: str = input("Ingrese el nombre del archivo de configuración: ")
        # try:
        # Creamos nueva instancia de DCCasillas
        self.dccasillas = DCCasillas(usuario, config)
        # Seleccionamos el primer tablero
        self.dccasillas.abrir_tablero(0)
        # Pasamos al menú de acciones
        self.menu_acciones.selector_opciones(self.dccasillas)
        # carga_correcta = True
        # except Exception as e:
        #     print(f"Error al cargar archivo de configuración: {e}")
    
    def continuar_juego(self) -> None:
        if not self.dccasillas:
            print("No hay juego en curso. Inicie un nuevo juego primero.")
            return
        # Pedimos mantener tablero actual o cambiar
        mantener: str = input(f"¿Desea cambiar el tablero actual [{self.dccasillas.tablero_actual}]? (y/n): ")
        if mantener.lower() == 'y':
            tablero: int = int(input("Ingrese el número de tablero a abrir: "))
            self.dccasillas.abrir_tablero(tablero)
            # Pasamos al menú de acciones
            self.menu_acciones.selector_opciones(self.dccasillas)
        elif mantener.lower() == 'n':
            # Pasamos al menú de acciones
            print("Menú de acciones (pendiente de implementar)")
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

    def selector_opciones(self, dccasillas: None) -> int:
        # Función para mostrar el menú de acciones
        print("\nDCCasillas")
        if not dccasillas:
            print("Usuario: UUU, Puntaje: PPP")
            print("Número de tablero: XXX de YYY")
            print("Movimientos tablero: ppp\n")
        else:
            print((f"Usuario: {dccasillas.usuario}, "
                   f"Puntaje: {dccasillas.puntaje}"))
            print(f"Número de tablero: {dccasillas.tablero_actual} de {len(dccasillas.tableros)}")
            tablero = dccasillas.tableros[dccasillas.tablero_actual]
            print(f"Movimientos tablero: {tablero.movimientos}\n")

        msg = mostrar_opciones("Menú de Acciones", self.opciones)

        # Pedimos opción
        opcion: int = int(input(msg))
        # Revisamos que sea válida
        while opcion < 1 or opcion > len(self.opciones):
            print("\nOpción inválida. Intente nuevamente.\n")
            opcion = int(input())
        return opcion

if __name__ == "__main__":
    menu = MenuJuego()
    menu.mostrar_menu()
