import os
from entities import Item, Usuario
from typing import List
from utils.pretty_print import print_usuario, print_canasta, print_items

def cargar_items() -> list:
    # path_items = os.path.join("utils", "items.dcc")
    path = "utils/items.dcc"
    with open(path, "r") as file:
        lines: list = file.readlines()
    items: List[Item] = []
    for line in lines:
        item_data: list = line.strip().split(",")
        items.append(
            Item(
                nombre=item_data[0],
                precio=int(item_data[1]),
                puntos=int(item_data[2])
            )
        )
    return items

def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    usuario = Usuario(esta_subscrito=tiene_suscripcion)
    print_usuario(usuario) 
    return usuario

if __name__ == "__main__":
    # 1) Crear usuario (puede ser con o sin suscripcion)
    usuario = crear_usuario(tiene_suscripcion=True)
    # 2) Cargar los items
    items = cargar_items()
    # 3) Imprimir todos los items usando los módulos de pretty_print
    print_items(items)
    # 4) Agregar todos los items a la canasta del usuario
    for item in items:
        usuario.agregar_item(item)
    # 5) Imprimir la canasta del usuario usando los módulos de pretty_print
    print_canasta(usuario)
    # 6) Generar la compra desde el usuario
    usuario.comprar()
    # 7) Imprimir el usuario usando los módulos de pretty_print
    print_usuario(usuario)