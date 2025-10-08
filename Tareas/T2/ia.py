

class IA():

    def __init__(
            self,
            nombre: str,
            vida_max: int,
            vida: int,
            ataque: int,
            mult_defensa: float,
            mult_ataque: float,
            prob_especial: float,
    ):
        self.nombre = nombre
        self.vida_max = vida_max
        self.__vida = vida
        self.ataque = ataque
        self.mult_defensa = mult_defensa
        self.mult_ataque = mult_ataque
        self.prob_especial = prob_especial

    @property
    def vida(self) -> int:
        return self.__vida
    
    @vida.setter
    def vida(self, nueva_vida: int):
        if nueva_vida < 0:
            self.__vida = 0
        elif nueva_vida > self.vida_max:
            self.__vida = self.vida_max
        else:
            self.__vida = nueva_vida

    def recibir_danio(self, danio: int) -> int:
        danio_recibido = int(danio * self.mult_defensa)
        self.vida -= danio_recibido
        print(f"{self.nombre} ha recibido {danio_recibido} de daño.")
        return danio_recibido
    
    def atacar(self, jugador) -> int:
        danio_realizado = int(self.ataque * self.mult_ataque)
        print(f"{self.nombre} ataca a {jugador.nombre} con {danio_realizado} de daño.")
        jugador.recibir_danio(danio_realizado)
        return danio_realizado

    def usar_habilidad_especial(self) -> None:
        """Este método se encarga de que la
        IA utilice su habilidad especial."""
        pass 

    def __str__(self) -> str:
        return f"{self.nombre} (IA): {self.vida}/{self.vida_max} HP"

