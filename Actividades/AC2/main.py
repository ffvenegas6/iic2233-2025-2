import collections
from os.path import join
from utilidades import Anime  # IMPORTANT: Debes utilizar esta nametupled


#####################################
#       Parte I - Cargar datos      #
#####################################
def cargar_animes(ruta_archivo: str) -> list:
    # TODO: Completar
    # Leer archivo con encoding utf-8
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    # Listado de animes a retornar
    animes = []
    # Chequeamos que el archivo no esté vacío
    if lineas:
        for linea in lineas:
            # Limpiamos línea y separamos por comas
            datos = linea.strip().split(",")
            # Creamos instancia de Anime
            anime = Anime(
                nombre=str(datos[0]),
                capitulos=int(datos[1]),
                puntaje=int(datos[2]),
                estreno=int(datos[3]),
                estudio=str(datos[4]),
                generos=set(str(genero) for genero in datos[5].split(";")),
            )
            # Agregamos anime a la lista
            animes.append(anime)
    # Retornamos la lista de animes
    return animes


#####################################
#        Parte II - Consultas       #
#####################################
def animes_por_estreno(animes: list) -> dict:
    # TODO: Completar
    # Creamos diccionario a rellenar
    dict_estrenos = {}
    # Iteramos sobre la lista de animes
    if animes:
        for anime in animes:
            # Si el año de estreno no está en el diccionario, lo agregamos
            if anime.estreno not in dict_estrenos:
                dict_estrenos[anime.estreno] = [anime.nombre]
            else:
                dict_estrenos[anime.estreno].append(anime.nombre)
    return dict_estrenos


def descartar_animes(generos_descartados: set, animes: list) -> list:
    # TODO: Completar
    # animes a mantener
    animes_filtrados = []
    # Iteramos sobre la lista de animes
    if animes:
        for anime in animes:
            # Si no hay intersección entre los géneros del anime y los géneros descartados, lo mantenemos
            if not (anime.generos & generos_descartados):
                animes_filtrados.append(anime.nombre)
    return animes_filtrados


def resumen_animes_por_ver(*animes: Anime) -> dict:
    # TODO: Completar
    if animes:
        return {
            "puntaje promedio": round(sum(anime.puntaje for anime in animes) / len(animes), 1),
            "capitulos total": sum(anime.capitulos for anime in animes),
            "generos": set().union(*(anime.generos for anime in animes)),
        }
    else:
        return {
            "puntaje promedio": 0.0,
            "capitulos total": 0,
            "generos": set(),
        }


def estudios_con_genero(genero: str, **estudios: dict) -> list:
    # TODO: Completar
    estudios_list = []
    # Iteramos sobre los estudios y sus animes
    if estudios:
        for estudio, animes in estudios.items():
            # Si algún anime del estudio tiene el género buscado, agregamos el estudio a la lista
            if any(genero in anime.generos for anime in animes):
                estudios_list.append(estudio)
    return estudios_list


if __name__ == "__main__":
    #####################################
    #       Parte I - Cargar datos      #
    #####################################
    animes = cargar_animes(join("data", "ejemplo.chan"))
    indice = 0
    for anime in animes:
        print(f"{indice} - {anime}")
        indice += 1

    #####################################
    #        Parte II - Consultas       #
    #####################################
    # Solo se usará los 2 animes del enunciado.
    datos = [
        Anime(
            nombre="Hunter x Hunter",
            capitulos=62,
            puntaje=9,
            estreno=1999,
            estudio="Nippon Animation",
            generos={"Aventura", "Comedia", "Shonen", "Acción"},
        ),
        Anime(
            nombre="Sakura Card Captor",
            capitulos=70,
            puntaje=10,
            estreno=1998,
            estudio="Madhouse",
            generos={"Shoujo", "Comedia", "Romance", "Acción"},
        ),
    ]

    # animes_por_estreno
    estrenos = animes_por_estreno(datos)
    print(estrenos)

    # descartar_animes
    animes = descartar_animes({"Comedia", "Horror"}, datos)
    print(animes)

    # resumen_animes_por_ver
    resumen = resumen_animes_por_ver(datos[0], datos[1])
    print(resumen)

    # estudios_con_genero
    estudios = estudios_con_genero(
        "Shonen",
        Nippon_Animation=[datos[0]],
        Madhouse=[datos[1]],
    )
    print(estudios)
