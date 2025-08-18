import sys
from dccasillas import DCCasillas
from tablero import Tablero
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

    def iniciar_juego(self) -> None:
        while self.opcion_actual != len(self.opciones) - 1:
            opcion = self.selector_opciones()
            self.opcion_actual = opcion - 1
            self.ejecutar_opcion(opcion)
        print("Saliendo del programa. ¡Hasta luego!\n")
        sys.exit(0)

if __name__ == "__main__":
    menu = MenuJuego()
    menu.iniciar_juego()
