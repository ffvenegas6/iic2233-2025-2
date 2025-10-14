from collections import defaultdict
from carta import CartaTropa, CartaEstructura
from ia import IA
import csv


def cargar_cartas(archivo_cartas):
    lista_cartas = []
    with open(archivo_cartas, "r", encoding="utf-8") as f:
        datos_cartas = csv.reader(f)
        next(datos_cartas)  # Saltar encabezado
        for carta in datos_cartas:
            # carta = carta.split(",")
            if carta[1] in ["tipo", "mixta"]:
                continue
            if carta[1] == "tropa":
                instancia_carta = CartaTropa(
                    nombre=carta[0],
                    tipo=carta[1],
                    vida_max=int(carta[2]),
                    mult_defensa=float(carta[3]),
                    precio=int(carta[4]),
                    prob_especial=float(carta[5]),
                    habilidad_especial=carta[8],
                )
                instancia_carta.ataque=int(carta[6]),
                instancia_carta.mult_ataque=float(carta[7]),
            elif carta[1] == "estructura":
                instancia_carta = CartaEstructura(
                    nombre=carta[0],
                    tipo=carta[1],
                    vida_max=int(carta[2]),
                    mult_defensa=float(carta[3]),
                    precio=int(carta[4]),
                    prob_especial=float(carta[5]),
                    habilidad_especial=carta[8],
                )               
            lista_cartas.append(instancia_carta)
    return lista_cartas


def cargar_multiplicadores(archivo_mult):
    mult_dict = defaultdict(dict)
    with open(archivo_mult, "r", encoding="utf-8") as datos_mult:
        contador = 0
        for ia in datos_mult:
            # Saltamos encabezado
            if contador == 0:
                contador += 1
                continue
            ia = ia.strip().split(",")
            nombre = ia[0]
            carta_tipo = ia[1]  # "tropa" o "estructura"
            mult_ataque = float(ia[2])
            mult_defensa = float(ia[3])
            mult_dict[nombre][carta_tipo] = {
                "mult_ataque": mult_ataque,
                "mult_defensa": mult_defensa,
            }
            contador += 1
    return mult_dict


def cargar_ias(archivo_ias, mult_dict):
    lista_ias = []
    with open(archivo_ias, "r", newline="", encoding="utf-8") as f:
        datos_ias = csv.DictReader(f)
        for ia in datos_ias:
            nombre = ia["nombre"]
            mult_dict = mult_dict.get(nombre)
            instancia_ia = IA(
                nombre=nombre,
                vida_max=int(ia["vida_maxima"]),
                ataque=int(ia["ataque"]),
                descripcion=ia["descripcion"],
                mult_dict=mult_dict,
                prob_especial=float(ia["probabilidad_especial"]),
                velocidad=float(ia["velocidad"]),
            )
            lista_ias.append(instancia_ia)
    return lista_ias