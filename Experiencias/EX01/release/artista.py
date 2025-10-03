from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_TRAP_CHILENO ,
                        AFINIDAD_STAFF_TRAP_CHILENO , AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_TRAP_CHILENO ,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        # COMPLETAR
        return self._afinidad_con_publico

    @property
    def afinidad_con_staff(self):
        # COMPLETAR
        return self._afinidad_con_staff

    @afinidad_con_staff.setter
    def afinidad_con_staff(self, valor):
        if valor < AFINIDAD_MIN:
            self._afinidad_con_staff = AFINIDAD_MIN
        elif valor > AFINIDAD_MAX:
            self._afinidad_con_staff = AFINIDAD_MAX
        else:
            self._afinidad_con_staff = valor
    
    @afinidad_con_publico.setter
    def afinidad_con_publico(self, valor):
        if valor < AFINIDAD_MIN:
            self._afinidad_con_publico = AFINIDAD_MIN
        elif valor > AFINIDAD_MAX:
            self._afinidad_con_publico = AFINIDAD_MAX
        else:
            self._afinidad_con_publico = valor

    @property
    def animo(self):
        # COMPLETAR
        return (self.afinidad_con_publico + self.afinidad_con_staff) * 0.5

    def recibir_suministros(self, suministro):
        # COMPLETAR
        valor = suministro.valor_de_satisfaccion
        self.afinidad_con_staff += valor
        if valor > 0:
            print(f"{self.nombre} recibió un {suministro.nombre} a tiempo!")
            print(f"Su afinidad con el staff aumentó en {valor} puntos.")
        else:
            print(f"{self.nombre} recibió {suministro.nombre} en malas condiciones")
            print(f"Su afinidad con el staff disminuyó en {valor} puntos.")

    def cantar_hit(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_HIT
        print(f"{self.nombre} está tocando su hit: {self.hit_del_momento}!")
        print(f"Su afinidad con el público aumentó en {AFINIDAD_HIT} puntos.")

    def __str__(self):
        # COMPLETAR
        return f"{self.nombre}"

class ArtistaPop(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.accion = "Cambio de vestuario"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_POP
        self._afinidad_con_staff = AFINIDAD_STAFF_POP

    def ejecutar_accion(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_ACCION_POP
        print(f"{self.nombre} hará un {self.accion}")

    @property
    def animo(self):
        # COMPLETAR
        valor_animo = super().animo
        if valor_animo < 10:
            print(f"ArtistaPop peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo


class ArtistaRock(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.accion = "Solo de guitarra"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_ROCK
        self._afinidad_con_staff = AFINIDAD_STAFF_ROCK

    def ejecutar_accion(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_ACCION_ROCK
        print(f"{self.nombre} hará un {self.accion}")
    
    @property
    def animo(self):
        # COMPLETAR
        valor_animo = super().animo
        if valor_animo < 5:
            print(f"ArtistaRock peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo


class ArtistaTrapChileno(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.accion = "Malianteo"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_TRAP_CHILENO
        self._afinidad_con_staff = AFINIDAD_STAFF_TRAP_CHILENO

    def ejecutar_accion(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_ACCION_TRAP_CHILENO
        print(f"{self.nombre} hará un {self.accion}")

    @property
    def animo(self):
        # COMPLETAR
        valor_animo = super().animo
        if valor_animo < 20:
            print(f"ArtistaTrapChileno peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo


class ArtistaReggaeton(Artista):
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        super().__init__(*args, **kwargs)
        self.accion = "Perrear"
        self._afinidad_con_publico = AFINIDAD_PUBLICO_REG
        self._afinidad_con_staff = AFINIDAD_STAFF_REG

    def ejecutar_accion(self):
        # COMPLETAR
        self.afinidad_con_publico += AFINIDAD_ACCION_REG
        print(f"{self.nombre} hará un {self.accion}")

    @property
    def animo(self):
        # COMPLETAR
        valor_animo = super().animo
        if valor_animo < 2:
            print(f"ArtistaReggaeton peligrando en el concierto. Animo: {valor_animo}")
        return valor_animo
