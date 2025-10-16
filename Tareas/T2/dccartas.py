from constants import ORO_POR_RONDA, ORO_POR_VICTORIA

class DCCartas():
    
    def __init__(self, jugador, ias, pool_cartas):
        self.jugador = jugador
        self.ias = ias
        self.pool_cartas = pool_cartas
        self.ronda = 1
        self.ia_actual = ias.pop(0) if ias else None

    @property
    def funcionando(self):
        return self.jugador.vivo and self.ia_actual is not None

    def combate(self):
        print(f"--- Ronda {self.ronda} ---\n")
    
        # Determinar orden de ataque
        primer_atacante, segundo_atacante = self._determinar_orden_ataque()
    
        # Realizar primer ataque
        hay_contraataque = self._ejecutar_ataque(primer_atacante, segundo_atacante)
        
        # Chequear si no continua el juego (murió quien recibe el ataque)
        if not hay_contraataque:
            return  # El juego terminó tras el primer ataque

        # Si no murió, el segundo ataca
        continua_juego = self._ejecutar_ataque(segundo_atacante, primer_atacante)
    
        if not continua_juego:
            return  # El juego terminó tras el segundo ataque (murió jugador o todas las IAs)

        self.ronda += 1
        self.jugador.oro += ORO_POR_RONDA

    def _determinar_orden_ataque(self):
        """Determina quién ataca primero basado en velocidad"""
        print("Determinando orden de ataque...")
        print(f"Velocidad {self.jugador.nombre}: {self.jugador.velocidad}")
        print(f"Velocidad {self.ia_actual.nombre}: {self.ia_actual.velocidad}")
        if self.jugador.velocidad >= self.ia_actual.velocidad:
            print(f"{self.jugador.nombre} ataca primero\n")
            return self.jugador, self.ia_actual
        else:
            print(f"{self.ia_actual.nombre} ataca primero\n")
            return self.ia_actual, self.jugador

    def _ejecutar_ataque(self, atacante, objetivo) -> bool:
        """Ejecuta un ataque y retorna True si el juego debe continuar"""
        atacante.atacar(objetivo)

        # Si el objetivo es jugador, verificar si sigue vivo 
        if isinstance(objetivo, type(self.jugador)) and not objetivo.vivo:
            print(f"{objetivo.nombre} ha sido derrotado.")
            return False
        
        # Si el objetivo es IA, verificar si sigue con vida
        if isinstance(objetivo, type(self.ia_actual)) and objetivo.vida <= 0:
            print(f"{objetivo.nombre} ha sido derrotada.")
            # Procesar premio y cargar siguiente IA si hay
            return self._procesar_victoria()
        
        return True

    def _procesar_victoria(self):
        """Maneja la lógica cuando una IA es derrotada"""
        if self.ias:
            self.ia_actual = self.ias.pop(0)
            self.jugador.oro += ORO_POR_VICTORIA
            print(f"{self.jugador.nombre} ha ganado el combate y obtiene {ORO_POR_VICTORIA}G")
            return True
        else:
            print(f"{self.jugador.nombre} ha ganado el juego!")
            self.jugador.oro += ORO_POR_VICTORIA
            self.ia_actual = None
            return False