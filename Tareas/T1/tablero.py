from __future__ import annotations
import os
from typing import List, Union
from visualizador import imprimir_tablero

class Tablero:

    def __init__(self) -> None:
        self.tablero: List[List[str]] = []
        self.movimientos: int = 0
        self.estado: bool = False
        
        # # atributos extras
        # self.casillas: List[List[bool]] = []  # Estado de casillas
        self.num_fil: int = None  # Número de filas
        self.num_col: int = None  # Número de columnas

    def cargar_tablero(self, archivo:str) -> None:
        path = os.path.join("config", archivo) 
        with open(path, 'r', encoding="utf-8") as file:
            # Obtenemos numero de filas y columnas
            encabezado: List[str] = file.readline().strip().split(' ')
            self.num_fil: int = int(encabezado[0])
            self.num_col: int = int(encabezado[1])
            # Inicializamos todas las casillas como habilitadas
            self.casillas = [
                [True for _ in range(self.num_col)] for _ in range(self.num_fil)
            ]
            # print(self.casillas)

            # Obtenemos el contenido del tablero
            lineas: List[str] = file.readlines()
            for linea in lineas:
                # Añadimos contenido de la fila al tablero
                fila: List[str] = linea.strip().split(' ')
                self.tablero.append(fila)

    def mostrar_tablero(self) -> None:
        imprimir_tablero(self.tablero)

    def modificar_casilla(self, fila:int, columna:int) -> bool:
        # Obtenemos el contenido de la casilla
        try:
            casilla = self.tablero[fila][columna]
            # Si la casilla está vacía, no se puede modificar
            if casilla == ".":
                print("No se puede modificar una casilla vacía.")
                return False
            # Si está deshabilitada, la habilitamos
            if "X" in casilla:
                print("Habilitando casilla...")
                self.tablero[fila][columna] = casilla.replace("X", "")
            # Si está habilitada, la deshabilitamos
            else:
                print("Deshabilitando casilla...")
                self.tablero[fila][columna] = "X" + casilla
            self.movimientos += 1
            # True si se realiza la acción
            return True
        # False si entregamos una posición inválida
        except IndexError:
            print("Posición fuera de rango.")
            return False
        # False si entregamos indices str y no int
        except TypeError:
            print("Fila y columna deben ser enteros.")
            return False

    def validar(self) -> bool:
        # Validamos filas
        if not self._validar_fila(self.tablero):
            return False
        # Transponemos el tablero para validar columnas como filas
        columnas: List[List[str]] = [
            [fila[i] for fila in self.tablero] for i in range(len(self.tablero[0]))
        ]
        if not self._validar_fila(columnas):
            return False
        self.estado = True
        return True

    def encontrar_solucion(self) -> Tablero:
        pass

    def _validar_fila(self, tablero: List[List[str]]) -> bool:
        # Iterar sobre cada fila del tablero, excepto la última
        for fila in tablero[:-1]:
            # Sumamos los valores de las casillas habilitadas y no vacías excepto la última
            suma_fila: int = sum(int(casilla) for casilla in fila[:-1] if casilla != "." and "X" not in casilla)
            # Obtenemos el valor objetivo de la última casilla habilitada
            objetivo_fila: str = fila[-1]
            # Verificamos si la suma coincide con el objetivo
            if objetivo_fila == ".":
                continue
            if suma_fila != int(objetivo_fila):
                return False
        return True

if __name__ == "__main__":
    tablero = Tablero()
    tablero.cargar_tablero("tab2.txt")
    tablero.mostrar_tablero()

