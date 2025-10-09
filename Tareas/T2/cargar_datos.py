from carta import CartaTropa, CartaEstructura

def cargar_carta(archivo_cartas):
    lista_cartas = []
    with open(archivo_cartas, "r", encoding="utf-8") as datos_cartas:
        for carta in datos_cartas:
            carta = carta.split(",")
            if carta[1] == "tropa":
                instancia_carta = CartaTropa(
                    nombre=carta[0],
                    tipo=carta[1],
                    vida_max=carta[2],
                    mult_defensa=carta[3],
                    precio=carta[4],
                    prob_especial=carta[5],
                    ataque=carta[6],
                    mult_ataque=carta[7],
                    habilidad_especial=carta[8],
                )
            elif carta[1] == "estructura":
                instancia_carta = CartaEstructura(
                    nombre=carta[0],
                    tipo=carta[1],
                    vida_max=carta[2],
                    mult_defensa=carta[3],
                    precio=carta[4],
                    prob_especial=carta[5],
                    habilidad_especial=carta[8],
                )               
            lista_cartas.append(instancia_carta)
    return lista_cartas
