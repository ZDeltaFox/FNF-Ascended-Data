import os

def listar_carpetas(directory_route):
    folder_list = []

    for root, directorys, files in os.walk(directory_route):
        for directory in directorys:
            full_route = os.path.join(root, directory)
            folder_list.append(full_route)

    return folder_list

current_route = os.path.dirname(os.path.abspath(__file__))

folders = listar_carpetas(current_route)

with open("checkfolders.txt", "w") as output_file:
    output_file.write("--START--\n")
    for folder in folders:
        output_file.write(folder + "\n")
    output_file.write("--END--")

print("Rutas guardadas en checkfolders.txt")
