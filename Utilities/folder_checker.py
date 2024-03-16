import os

def listar_carpetas_en_directorio(ruta_directorio):
    # Inicializamos una lista vacía para almacenar las rutas completas de las carpetas
    lista_carpetas = []

    # Iteramos sobre las carpetas en el directorio y sus subdirectorios
    for raiz, directorios, archivos in os.walk(ruta_directorio):
        for directorio in directorios:
            # Agregamos la ruta completa de la carpeta a la lista
            ruta_completa = os.path.join(raiz, directorio)
            lista_carpetas.append(ruta_completa)

    return lista_carpetas

# Obtenemos la ruta del directorio donde se encuentra este archivo
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Obtenemos la lista de carpetas en el directorio actual y sus subdirectorios
carpetas = listar_carpetas_en_directorio(ruta_actual)

# Guardamos la lista de carpetas en un archivo llamado "checkfolders.txt"
with open("checkfolders.txt", "w") as archivo_salida:
    archivo_salida.write("--START--\n")
    for carpeta in carpetas:
        archivo_salida.write(carpeta + "\n")
    archivo_salida.write("--END--")

# Imprimimos un mensaje de éxito
print("Las rutas de las carpetas se han guardado en checkfolders.txt")
