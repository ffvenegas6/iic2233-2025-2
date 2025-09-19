import os
from tablero import Tablero
from typing import List
from io import StringIO

class DCCasillas:

    def __init__(self, usuario:str, config:str) -> None:
        self.usuario: str = usuario
        self.puntaje: int = 0
        self.tablero_actual: int = None
        self.tableros: List[Tablero] = self.cargar_tableros(config)

    def abrir_tablero(self, num_tablero:int) -> None:
        try:
            tablero_objetivo = self.tableros[num_tablero]
        except IndexError:
            print(f"Tablero {num_tablero} fuera de rango.")
            # self.tablero_actual = None
        except TypeError:
            print("Número de tablero debe ser un entero.")
            # self.tablero_actual = None
        self.tablero_actual = num_tablero

    def guardar_estado(self) -> bool: 
        try:    
            path = os.path.join("data", f"{self.usuario}.txt")
            with open(path, 'w', encoding="utf-8") as file:
                file.write(f"{len(self.tableros)}\n")
                for tablero in self.tableros:
                    file.write(f"{tablero.movimientos}\n")
                    file.write(f"{tablero.num_fil} {tablero.num_col}\n")
                    for fila in tablero.tablero:
                        file.write(" ".join(fila) + "\n")
            return True
        except FileNotFoundError as e:
            print(f"Error: No se encontró el archivo o directorio - {e}")
            return False
        except IOError as e:
            print(f"Error: Error de entrada/salida - {e}")
            return False

    def recuperar_estado(self) -> bool:
        try:    
            path = os.path.join("data", f"{self.usuario}.txt")
            with open(path, 'r', encoding="utf-8") as file:
                # 1ra linea: número de tableros
                num_tab: int = int(file.readline().strip())
                self.tableros = []
                print(f"Recuperando {num_tab} tableros...")
                for i in range(num_tab):
                    # print(f"Tablero {i + 1}:")
                    tablero = Tablero()
                    # 1ra linea: movimientos
                    tablero.movimientos = int(file.readline().strip())
                    # print(f"Movimientos: {tablero.movimientos}")
                    # 2da linea: número de filas y columnas
                    encabezado: List[str] = file.readline().strip().split(' ')
                    num_fil: int = int(encabezado[0])
                    num_col: int = int(encabezado[1])
                    # print(f"Número de filas: {num_fil}, Número de columnas: {num_col}")
                    # Contenido del tablero
                    contenido_tablero = f"{num_fil} {num_col}\n"
                    # Leer las siguientes líneas del tablero
                    for _ in range(num_fil + 1): # +1 para incluir la fila objetivo
                        contenido_tablero += file.readline()
                
                    # Crear un archivo temporal en el directorio config/
                    temp_filename = f"temp_tablero_{i}.txt"
                    temp_path = os.path.join("config", temp_filename)
                    with open(temp_path, 'w', encoding="utf-8") as temp_file:
                        temp_file.write(contenido_tablero)

                    # Cargar el tablero usando cargar_tablero()
                    tablero.cargar_tablero(temp_filename)

                    # Eliminar el archivo temporal después de cargarlo
                    os.remove(temp_path)

                    # Agregar el tablero a la lista
                    self.tableros.append(tablero)
            return True
        except FileNotFoundError as e:
            print(f"Error: No se encontró el archivo o directorio - {e}")
            return False

    # Funciones extras
    def cargar_tableros(self, config_path: str) -> List[Tablero]:
        """Carga los tableros desde el archivo de configuración."""
        tableros: List[Tablero] = []
        path = os.path.join("config", config_path)
        try:
            with open(path, 'r', encoding="utf-8") as file:
                encabezado: List[str] = file.readline().strip().split(' ')
                num_tableros: int = int(encabezado[0])
                nombre_tableros: List[str] = file.readlines()
                for nombre in nombre_tableros:
                    # Cargar cada tablero
                    tablero = Tablero()
                    tablero.cargar_tablero(nombre.strip())
                    tableros.append(tablero)
            return tableros
        except FileNotFoundError as e:
            print(f"Error: No se encontró el archivo o directorio - {e}")
        except IOError as e:
            print(f"Error: Error de entrada/salida - {e}")
        except ValueError as e:
            print(f"Error: Formato de archivo inválido - {e}")
        

# if __name__ == "__main__":
#     # Ejemplo de uso
#     dccasillas = DCCasillas("usuario1", "config.txt")
#     dccasillas.abrir_tablero(4)
#     if dccasillas.tablero_actual:
#         dccasillas.tableros[dccasillas.tablero_actual].mostrar_tablero()
#         dccasillas.tableros[dccasillas.tablero_actual].modificar_casilla(2, 3)
#         dccasillas.tableros[dccasillas.tablero_actual].modificar_casilla(2, 3)
#         dccasillas.tableros[dccasillas.tablero_actual].mostrar_tablero()
#     # dccasillas.guardar_estado()
#     dccasillas.recuperar_estado()
#     dccasillas.tableros[dccasillas.tablero_actual].mostrar_tablero()
#     # dccasillas.tablero_actual.mostrar_tablero()