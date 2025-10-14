

class DCCartas():
    
    def __init__(self, jugador, ias, pool_cartas):
        self.jugador = jugador
        self.ias = ias
        self.pool_cartas = pool_cartas
        self.ronda = 1
        self.ia_actual = ias.pop(0) if ias else None

    @property
    def funcionando(self):
        # Itera cartas del jugador para ver si está
        jugador_muerto = True
        for carta in self.jugador.cartas:
            if carta.vida > 0:
                jugador_muerto = False
                break
        return not jugador_muerto and self.ia_actual is not None