class Carta():
    def __init__(
            self,
            nombre: str,
            vida_max: int,
            vida: int,
            tipo: str,
            mult_defensa: float,
            precio: int,
            prob_especial: float,
    ):
        self.nombre = nombre
        self.vida_max = vida_max
        self.__vida = vida
        self.tipo = tipo
        self.mult_defensa = mult_defensa
        self.precio = precio
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

    def recibir_danio(self, danio_ia: int) -> int:
        danio_recibido = int(danio_ia * self.mult_defensa)
        self.vida -= danio_recibido
        return danio_recibido

    def usar_habilidad_especial(self) -> None:
        """Este método se encarga de que la
        carta utilice su habilidad especial."""
        pass 

    def __str__(self) -> str:
        return f"{self.nombre} ({self.tipo}): {self.vida}/{self.vida_max} HP"

class CartaTropa(Carta):
    def __init__(
            self,
            nombre: str,
            vida_max: int,
            vida: int,
            tipo: str,
            mult_defensa: float,
            precio: int,
            prob_especial: float,
            ataque: int,
            mult_ataque: float,
    ):
        super().__init__(nombre, vida_max, vida, tipo, mult_defensa, precio, prob_especial)
        self.ataque = ataque
        self.mult_ataque = mult_ataque

    def atacar(self, ia) -> int:
        danio_realizado = int(self.ataque * self.mult_ataque)
        ia.recibir_danio(danio_realizado)
        return danio_realizado

    def usar_habilidad_especial(self) -> None:
        """Implementar la habilidad especial de la tropa."""
        pass

class CartaEstructura(Carta):

    def __init__(
            self,
            nombre: str,
            vida_max: int,
            vida: int,
            tipo: str,
            mult_defensa: float,
            precio: int,
            prob_especial: float,
            ataque: int,
            mult_ataque: float,
    ):
        super().__init__(nombre, vida_max, vida, tipo, mult_defensa, precio, prob_especial)

    def usar_habilidad_especial(self):
        """Implementar la habilidad especial de la tropa."""
        pass

class CartaMixta(CartaTropa, CartaEstructura):
    def __init__(
            self,
            nombre: str,
            vida_max: int,
            vida: int,
            tipo: str,
            mult_defensa: float,
            precio: int,
            prob_especial: float,
            ataque: int,
            mult_ataque: float,
    ):
        super().__init__(
            nombre, vida_max, vida, tipo, mult_defensa,
            precio, prob_especial, ataque, mult_ataque
        )

    def usar_habilidad_especial(self):
        """Implementar la habilidad especial de la tropa."""
        pass