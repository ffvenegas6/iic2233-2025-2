import os
import sys
import random
from typing import List
from jugador import Jugador
from ia import IA
from carta import Carta
from dccartas import DCCartas
from cargar_datos import cargar_cartas, cargar_multiplicadores, cargar_ias
from constants import (
    DINERO_INICIAL
)

def ejecucion():
    if len(sys.argv) != 3:
        print("Uso correcto: 'python {dificultad} {nombre_usuario}'")
        print("(Dificultades posibles: facil, normal, dificil)")
        sys.exit(1)
    dificultad = sys.argv[1]
    nombre_usuario = sys.argv[2]
    seleccion_inicial(dificultad, nombre_usuario)

def seleccion_inicial(dificultad, nombre_usuario):
    # Cargar cartas y seleccionar aleatoriamente entre 3 y 5
    path_cartas = os.path.join("data", "cartas.csv")
    pool_global: List[Carta] = cargar_cartas(path_cartas)
    random_n = random.randint(3, 5)
    random_cartas = random.sample(pool_global, random_n)

    # Selección de cartas por parte del usuario
    cartas_seleccionadas: List[Carta] = []
    print("-" * 30)
    print("SELECCIÓN INICIAL".center(30, " "))
    print("-" * 30)
    while True:
        print()
        print(f"Cartas seleccionadas: ({len(cartas_seleccionadas)}) "
              f"{[carta.nombre for carta in cartas_seleccionadas]}")
        for i, carta in enumerate(random_cartas):
            print(f"[{i + 1}] {carta.nombre}")
        print(f"[{len(random_cartas) + 1}] Continuar al Menú Principal")
        
        index = input(f"Seleccione hasta {random_n} cartas para su mazo: ")
        # Chequeo que ingrese un número
        if not index.isdigit():
            print("Seleccione una opción válida!")
        # Si elige la última opción (avanzar al menú principal)
        elif int(index) == (len(random_cartas) + 1):
            # Si no ha seleccionado cartas, seguimos en el loop
            if not cartas_seleccionadas:
                print("Debes seleccionar al menos una carta")
                continue
            # Si ha seleccionado cartas, salimos del loop
            break
        # Si elige una carta válida, la agrega a las seleccionada
        elif 0 < int(index) < (len(random_cartas) + 1):
            cartas_seleccionadas.append(random_cartas[int(index) - 1])
            random_cartas.pop(int(index) - 1)
        else:
            print("Seleccione una opción válida!")

    jugador = Jugador(nombre_usuario)
    jugador.cartas = cartas_seleccionadas 
    # jugador.coleccion = cartas_seleccionadas 
    jugador.oro = DINERO_INICIAL 

    path_mult = os.path.join("data", "multiplicadores.csv")
    mult_dict = cargar_multiplicadores(path_mult)
    path_ias = os.path.join("data", f"ias_{dificultad}.csv")
    ias: List[IA] = cargar_ias(path_ias, mult_dict)
    dccartas = DCCartas(jugador, ias, pool_global)
    menu_principal(dccartas)

def menu_principal(dccartas):
    while dccartas.funcionando:
        print()
        print("-" * 30)
        print("MENÚ PRINCIPAL".center(30, " "))
        print("-" * 30)
        print(f"Dinero disponible: {dccartas.jugador.oro}G")
        print(f"Ronda actual: {dccartas.ronda}")
        print(f"IA Enemiga: {dccartas.ia_actual.nombre if dccartas.ia_actual else 'Ninguna'}")
        print()
        print("[1] Entrar en combate")
        print("[2] Inventario (gestionar mazo)")
        print("[3] Tienda")
        print("[4] Ver información de mis cartas")
        print("[5] Espiar a la IA")
        print("[0] Salir del juego")
        print()
        index = input("Indique su opción: ")

        if index == "0":
            print("Hasta pronto!")
            sys.exit(0)
        elif index == "1":
            print("Combate")
        elif index == "2":
            menu_inventario(dccartas)
        elif index == "3":
            print("Tienda")
        elif index == "4":
            print("-" * 20)
            for index, carta in enumerate(dccartas.jugador.cartas):
                print(f"[{index + 1}] {carta}")
                print("-" * 20)
        elif index == "5":
            print(f"Espiando a {dccartas.ia_actual.nombre}...")
            print(dccartas.ia_actual)
        else:
            print("Seleccione una opción válida!")

def menu_inventario(dccartas):
    while True:
        print()
        print("-" * 30)
        print("INVENTARIO".center(30, " "))
        print("-" * 30)
        print(f"Mazo:")
        print("-" * 20)
        for i, carta in enumerate(dccartas.jugador.cartas):
            print(f"[{i + 1}] {carta.nombre}")
        print("-" * 20)
        print(f"Colección:")
        for i, carta in enumerate(dccartas.jugador.coleccion):
            print(f"[{i + 1}] {carta.nombre}")
        print()
        print("[1] Pasar cartas al mazo desde colección")
        print("[2] Reordenar mazo")
        print("[3] Sacar cartas del mazo a colección")
        print("[0] Volver al Menú Principal\n")
        print()
        index = input("Indique su opción: ")

        if index == "0":
            return
        elif index == "1":
            print("Pasar cartas de colección al mazo")
            menu_agregar_cartas(dccartas)
        elif index == "2":
            print("Reordenar mazo")
        elif index == "3":
            menu_sacar_cartas(dccartas)
        else:
            print("Seleccione una opción válida!")

def menu_sacar_cartas(dccartas):
    while True:
        if len(dccartas.jugador.cartas) == 1:
            print("Debes tener al menos una carta en el mazo.")
            return
        print("-" * 30)
        print("Sacar cartas del mazo a colección".center(30, " "))
        print("-" * 30)
        print()
        # print(f"Cartas a sacar: ({len(cartas_seleccionadas)}) "
        #     f"{[carta.nombre for carta in cartas_seleccionadas]}")
        for i, carta in enumerate(dccartas.jugador.cartas):
            print(f"[{i + 1}] {carta.nombre}")
        print("[0] Volver al Menú Inventario\n")

        index = input(f"Seleccione el índice de la carta a sacar del mazo: ")
        # Chequeo que ingrese un número
        if not index.isdigit():
            print("Seleccione una opción válida!")
        # Si elige la última opción (avanzar al menú principal)
        elif int(index) == 0:
            print("Volviendo al Menú Inventario...")
            return
        # Si elige una carta válida, la agrega a las seleccionada
        elif 0 < int(index) < len(dccartas.jugador.cartas) + 1:
            dccartas.jugador.coleccion.append(dccartas.jugador.cartas.pop(int(index) - 1))
        else:
            print("Seleccione una opción válida!")

def menu_agregar_cartas(dccartas):
    while True: 
        if len(dccartas.jugador.coleccion) == 0:
            print("Debes tener al menos una carta en la colección.")
            return
        print("-" * 30)
        print("Agregar cartas al mazo desde colección".center(30, " "))
        print("-" * 30)
        print()
        # print(f"Cartas a sacar: ({len(cartas_seleccionadas)}) "
        #     f"{[carta.nombre for carta in cartas_seleccionadas]}")
        for i, carta in enumerate(dccartas.jugador.coleccion):
            print(f"[{i + 1}] {carta.nombre}")
        print("[0] Volver al Menú Inventario\n")

        index = input(f"Seleccione el índice de la carta a agregar al mazo: ")
        # Chequeo que ingrese un número
        if not index.isdigit():
            print("Seleccione una opción válida!")
        # Si elige la última opción (avanzar al menú principal)
        elif int(index) == 0:
            print("Volviendo al Menú Inventario...")
            return
        # Si elige una carta válida, la agrega a las seleccionada
        elif 0 < int(index) < len(dccartas.jugador.coleccion) + 1:
            # Chequeo que no exceda el límite de cartas en el mazo
            success = dccartas.jugador.agregar_carta(
                dccartas.jugador.coleccion[int(index) - 1]
            )
            # Si no excede, la agrega al mazo y la saca de la colección
            if success:
                dccartas.jugador.coleccion.pop(int(index) - 1)
        else:
            print("Seleccione una opción válida!")

if __name__ == "__main__":
    ejecucion()