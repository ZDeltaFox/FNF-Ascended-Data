import os

def listar_archivos_en_directorio(ruta_directorio):
    # Inicializamos una lista vacía para almacenar las rutas completas de los archivos
    lista_archivos = []

    # Iteramos sobre los archivos en el directorio y sus subdirectorios
    for raiz, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            # Agregamos la ruta completa del archivo a la lista
            ruta_completa = os.path.join(raiz, archivo)
            lista_archivos.append(ruta_completa)

    return lista_archivos

# Obtenemos la ruta del directorio donde se encuentra este archivo
ruta_actual = os.path.dirname(os.path.abspath(__file__))

# Obtenemos la lista de archivos en el directorio actual y sus subdirectorios
archivos = listar_archivos_en_directorio(ruta_actual)

# Guardamos la lista de archivos en un archivo llamado "checkfiles.txt"
with open("checkfiles.txt", "w") as archivo_salida:
    archivo_salida.write("--START--\n")
    for archivo in archivos:
        archivo_salida.write(archivo + "\n")
    archivo_salida.write("--END--")

# Imprimimos un mensaje de éxito
print("Los nombres de los archivos se han guardado en checkfiles.txt")
