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
        cartas_defensa = [
            carta for carta in self.cartas if carta.tipo ["estructura", "mixta"]
        ]
        for carta in cartas_defensa:
            carta.recibir_danio(danio)
        