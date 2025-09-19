import sys
from dccasillas import DCCasillas
from typing import List

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
        
    def selector_opciones(self) -> int:
        print("\n¡Bienvenido a DCCasillas!\n")
        if not self.dccasillas:
            print("Usuario: UUU, Puntaje: PPP")
            print("Tableros resueltos: TTT\n")
        else:
            print((f"Usuario: {self.dccasillas.usuario}, "
                   f"Puntaje: {self.dccasillas.puntaje}"))
            print("Tableros resueltos: TTT\n")

        print("*" * 3 + " Menú de Juego " + "*" * 3 + "\n")
        for i in range(len(self.opciones)):
            print(f"[{i + 1}] {self.opciones[i]}")

        msg = ("\nIndique su opción "
              f"({', '.join(str(i + 1) for i in range(len(self.opciones)))}): ")
        
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
        # TODO: menú de acciones
        print("Menú de acciones (pendiente de implementar)")
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
            # TODO: menú de acciones
            print("Menú de acciones (pendiente de implementar)")
        elif mantener.lower() == 'n':
            # Pasamos al menú de acciones
            print("Menú de acciones (pendiente de implementar)")
        else:
            print("Opción inválida. Regresando al menú principal.")
            


if __name__ == "__main__":
    menu = MenuJuego()
    menu.mostrar_menu()
