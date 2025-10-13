import os
import sys
import random
from typing import List
from jugador import Jugador
from carta import Carta
from cargar_datos import cargar_cartas, cargar_multiplicadores, cargar_ias

def ejecucion():
    if len(sys.argv) != 3:
        print("Uso correcto: 'python {dificultad} {nombre_usuario}'")
        print("(Dificultades posibles: facil, normal, dificil)")
        sys.exit(1)
    dificultad = sys.argv[1]
    nombre_usuario = sys.argv[2]
    seleccion_inicial(dificultad, nombre_usuario)

def seleccion_inicial(dificultad, nombre_usuario):
    jugador = Jugador(nombre_usuario)

    path_cartas = os.path.join("data", "cartas.csv")
    pool_global: List[Carta] = cargar_cartas(path_cartas)
    random_n = random.randint(3, 5)
    random_cartas = random.sample(pool_global, random_n)
    cartas_seleccionadas: List[Carta] = []
    print("-" * 30)
    print("SELECCIÓN INICIAL".center(30, " "))
    print("-" * 30)
    index: int = 0
    while True:
        print()
        print(f"Cartas seleccionadas: ({len(cartas_seleccionadas)}) "
              f"{[carta.nombre for carta in cartas_seleccionadas]}")
        for i, carta in enumerate(random_cartas):
            print(f"[{i + 1}] {carta.nombre}")
        print(f"[{len(random_cartas) + 1}] Continuar al Menú Principal")
        index = int(input(f"Seleccione hasta {random_n} cartas para su mazo: "))
        #print("(Debe seleccionar al menos una carta)")
        if index == (len(random_cartas) + 1):
            break
        if index > (len(random_cartas) + 1) or index <= 0:
            print("Debe entregar un entero válido")
            continue
        cartas_seleccionadas.append(random_cartas[index - 1])
        random_cartas.pop(index - 1)

if __name__ == "__main__":
    ejecucion()