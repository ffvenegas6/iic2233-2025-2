from typing import List
from carta import Carta
import random

class Jugador:

    def __init__(self, nombre):
        self.nombre: str = nombre
        self.__cartas: List[Carta] = []
        self.coleccion: List[Carta] = []
        self.oro: int = 0

    @property
    def vivo(self) -> bool:
        for carta in self.cartas:
            if carta.vida > 0:
                return True
        return False

    @property
    def velocidad(self):
        return round(random.uniform(0.0, 1.0), 1) 

    @property
    def cartas(self):
        return self.__cartas
    
    @cartas.setter
    def cartas(self, nuevas_cartas: List[Carta]) -> bool:
        if len(nuevas_cartas) <= 5:
            self.__cartas.extend(nuevas_cartas)
            return True
        else:
            print("El límite de cartas en el mazo es de 5.")
            return False

    def agregar_carta(self, carta: Carta) -> bool:
        if len(self.__cartas) < 5:
            self.__cartas.append(carta)
            return True
        else:
            print("El límite de cartas en el mazo es de 5.")
            return False

    def atacar(self, ia):
        cartas_ataque = [
            carta for carta in self.cartas if carta.tipo in ["tropa", "mixta"]
        ]
        for carta in cartas_ataque:
            carta.atacar(ia)
            # carta.usar_habilidad_especial()
    
    def recibir_danio(self, danio, mult_dict):
        cartas_tropa = [
            carta for carta in self.cartas if carta.tipo == "tropa"
        ]
        cartas_defensa = [
            carta for carta in self.cartas if carta.tipo in ["estructura", "mixta"]
        ]
        
        # Cada carta de ataque recibe todo el daño si no hay cartas de defensa
        if not cartas_defensa:
            print("El jugador no tiene cartas de defensa. Cartas de ataque reciben todo el daño.")
            for carta in cartas_tropa:
                mult_ataque_ia = mult_dict.get(carta.tipo).get("mult_ataque")
                danio_recibido = int(danio * mult_ataque_ia)
                print(f"{carta.nombre} ha recibido {danio} de daño.")
                print(f"Para {carta.tipo}, el multiplicador de ataque de la IA es {mult_ataque_ia}.")
                carta.recibir_danio(danio_ia=danio_recibido)
        
        else:
            print("El jugador tiene cartas de defensa. Distribuyendo daño entre cartas de defensa.")
            for carta in cartas_defensa:
                mult_ataque_ia = mult_dict.get(carta.tipo).get("mult_ataque")
                danio_recibido = int(danio * mult_ataque_ia)
                danio_ef = danio_recibido / len(cartas_defensa)
                print(f"{carta.nombre} ha recibido {danio} de daño.")
                print(f"Para {carta.tipo}, el multiplicador de ataque de la IA es {mult_ataque_ia}.")
                print(f"Distribuyendo el daño, se recibe: {danio_ef}.")
                carta.recibir_danio(danio_ef)
