

class IA():

    def __init__(
            self,
            nombre: str,
            vida_max: int,
            ataque: int,
            descripcion: str,
            mult_dict: dict,
            prob_especial: float,
            velocidad: float,
    ):
        self.nombre = nombre
        self.vida_max = vida_max
        self.__vida = vida_max
        self.ataque = ataque
        self.descripcion = descripcion
        self.mult_dict = mult_dict 
        self.prob_especial = prob_especial
        self.velocidad = velocidad

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

    def recibir_danio(self, danio: int, tipo: str) -> int:
        mult_defensa = self.mult_dict.get(tipo).get("mult_defensa")
        danio_recibido = int(danio * mult_defensa)
        self.vida -= danio_recibido
        print(f"Para {tipo}, el multiplicador de defensa de {self.nombre} es {mult_defensa}.")
        return danio_recibido
    
    def atacar(self, jugador) -> int:
        danio_realizado = self.ataque
        print(f"{self.nombre} ataca a {jugador.nombre} con {danio_realizado} de daño.")
        jugador.recibir_danio(danio_realizado, self.mult_dict)
        return danio_realizado

    def usar_habilidad_especial(self) -> None:
        """Este método se encarga de que la
        IA utilice su habilidad especial."""
        pass 

    def __str__(self) -> str:
        return f"{self.nombre} (IA): {self.vida}/{self.vida_max} HP"

