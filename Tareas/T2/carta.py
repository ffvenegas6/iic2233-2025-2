class Carta():
    def __init__(
            self,
            nombre: str,
            vida_max: int,
            tipo: str,
            mult_defensa: float,
            precio: int,
            prob_especial: float,
            habilidad_especial: str
    ):
        self.nombre = nombre
        self.vida_max = vida_max
        self.__vida = vida_max
        self.tipo = tipo
        self.mult_defensa = mult_defensa
        self.precio = precio
        self.prob_especial = prob_especial
        self.habilidad_especial = habilidad_especial

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

    def recibir_danio(self, danio_ia: int) -> int:
        danio_recibido = int(danio_ia * self.mult_defensa)
        self.vida -= danio_recibido
        print(f"{self.nombre} ha recibido {danio_recibido} de daño.")
        print(f"Le queda {self.vida} / {self.vida_max} HP")
        return danio_recibido

    def usar_habilidad_especial(self) -> None:
        """Este método se encarga de que la
        carta utilice su habilidad especial."""
        pass 

    def __str__(self) -> str:
        return (f"{self.nombre} ({self.tipo}): {self.vida}/{self.vida_max} HP\n"
                f"Habilidad especial: {self.habilidad_especial}")


class CartaTropa(Carta):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ataque: int = 0
        self.mult_ataque: float = 0.0

    def atacar(self, ia) -> int:
        danio_realizado = int(self.ataque * self.mult_ataque)
        print(f"{self.nombre} ataca a {ia.nombre} con {danio_realizado} de daño.")
        ia.recibir_danio(danio_realizado, self.tipo)
        return danio_realizado

    def usar_habilidad_especial(self) -> None:
        """Implementar la habilidad especial de la tropa."""
        pass


class CartaEstructura(Carta):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def usar_habilidad_especial(self):
        """Implementar la habilidad especial de la tropa."""
        pass


class CartaMixta(CartaTropa, CartaEstructura):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def usar_habilidad_especial(self):
        """Implementar la habilidad especial de la tropa."""
        pass