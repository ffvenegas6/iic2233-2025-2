from typing import List
from carta import Carta

class Jugador:

    def __init__(self, nombre):
        self.nombre: str = nombre
        self.cartas: List[Carta] = []
        self.coleccion: List[Carta] = []
        self.oro: int = 0

    def atacar(self, ia):
        cartas_ataque = [
            carta for carta in self.cartas if carta.tipo in ["tropa", "mixta"]
        ]
        for carta in cartas_ataque:
            carta.atacar(ia)
            carta.usar_habilidad_especial()
    
    def recibir_danio(self, danio):
        cartas_tropa = [
            carta for carta in self.cartas if carta.tipo == "tropa"
        ]
        # cartas_estructura = [
        #     carta for carta in self.cartas if carta.tipo == "estructura"
        # ]
        # cartas_mixta = [
        #     carta for carta in self.cartas if carta.tipo == "mixta"
        # ]
        cartas_defensa = [
            carta for carta in self.cartas if carta.tipo in ["estructura", "mixta"]
        ]
        
        # Cartas ataque reciben todo el daño si no hay defensa
        # if not cartas_estructura and not cartas_mixta:
        if not cartas_defensa:
            for carta in cartas_tropa:
                carta.recibir_danio(danio)
        
        else:
            # danio_ef = danio / (len(cartas_estructura) + len(cartas_mixta))
            danio_ef = danio / len(cartas_defensa)
            for carta in cartas_defensa:
                carta.recibir_danio(danio_ef)
