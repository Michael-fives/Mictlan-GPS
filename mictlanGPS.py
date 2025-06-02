from mictlanGrafo import grafo
import os

def bfs(start, end):
    from collections import deque

    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()

        if current == end:
            # Reconstruir la ruta
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        # Explorar vecinos
        for neighbor in ordenar_vecinos(current, grafo[current]['vecinos']):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None  # Si no se encuentra ruta

def es_movimiento_recto(actual, vecino):
    # Recto si fila o columna es igual
    return actual[0] == vecino[0] or actual[1] == vecino[1]

def ordenar_vecinos(actual, vecinos):
    rectos = [v for v in vecinos if es_movimiento_recto(actual, v)]
    diagonales = [v for v in vecinos if not es_movimiento_recto(actual, v)]
    return rectos + diagonales  # Primero los rectos

def nombre_existe(grafo, name): # Verifica si el nombre ya existe en el grafo
    for nodo, data in grafo.items():
        if name in data['personas']:
            return True
    return False

def main():
    if __name__ == "__main__":
        selection = 0
        start = None
        # Menu principal del sistema de navegación del cementerio Mictlán Guadalajara Zona Metropolitana
        print("Bienvenido al sistema de navegación del cementerio Mictlán Guadalajara Zona Metropolitana")
        while True:
            selection = input("Por favor, elige una opción:\n"
                "1. Encontrar a un familiar\n"
                "2. Visitar a un familiar\n"
                "9. Agregar familiar (administrador)\n"
                "3. Salir\n"
                "Presiona Enter para continuar...\n")
            
            if selection == "1":
                family_member = input("Por favor, ingresa el nombre del familiar a buscar: ")
                if family_member.strip():
                    finded = False
                    for node, data in grafo.items():
                        if family_member in data['personas']:
                            finded = True
                            ruta_mapa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mictlanMapeado.txt')
                            with open(ruta_mapa, 'r') as file:
                                map = [line.strip().split() for line in file.readlines()]

                            # Marcar la ubicación del familiar con 'X'
                            x, y = node
                            map[x][y] = 'X'

                            # Imprimir el mapa
                            print(f"\n{family_member} fue encontrado. Ubicación marcada con 'X':")
                            for row in map:
                                print(' '.join(row))
                            break

                    if not finded:
                        print(f"{family_member} no fue encontrado. Intenta con otro nombre.")
                else:
                    print("El nombre no puede estar vacío. Por favor, intenta de nuevo.")


            elif selection == "2":
                entry = "Ninguna"
                familiar = "Ninguno"

                print("Por favor, rellena los campos antes de realizar la busqueda:\n")
                while True:
                    # Selección de entrada del cementerio y familiar a visitar para enrutar
                    selection_2 = input(
                        f"1. Entrada del cementerio: '{entry}'\n"
                        f"2. Familiar a visitar: '{familiar}'\n"
                        "3. Enrutar\n"
                        "4. Salir\n"
                        "Presiona Enter para continuar...\n")
                    
                    if selection_2 == "1":
                        while True:
                            # Selección de entrada del cementerio
                            selection_entry = input("Por favor, elige una entrada:\n"
                                "1. Entrada Norte\n"
                                "2. Entrada Sur\n"
                                "3. Entrada Este\n"
                                "4. Entrada Sureste\n"
                                "5. Entrada Oeste\n"
                                "Presiona Enter para continuar...\n")
                            
                            if selection_entry == "1":
                                entry = "Entrada Norte"
                                start = (0, 10)
                                break

                            elif selection_entry == "2":
                                entry = "Entrada Sur"
                                start = (20, 10)
                                break

                            elif selection_entry == "3":
                                entry = "Entrada Este"
                                start = (2, 45)
                                break

                            elif selection_entry == "4":
                                entry = "Entrada Sureste"
                                start = (10, 32)
                                break

                            elif selection_entry == "5":
                                entry = "Entrada Oeste"
                                start = (10, 0)
                                break
                        
                            else:
                                print("Entrada no válida. Por favor, elige una opción del 1 al 5.")

                    elif selection_2 == "2":
                        while True:
                            # Selección de familiar a visitar
                            family_member = input("Por favor, ingresa el nombre del familiar a visitar: ")
                            if family_member.strip():
                                finded = False
                                for node, data in grafo.items():
                                    if family_member in data['personas']:
                                        print(f"{family_member} fue encontrado.")
                                        familiar = family_member
                                        end = node
                                        finded = True
                                        break

                                if finded:
                                    break
                                else:
                                    print(f"{family_member} no fue encontrado. Intenta con otro nombre.")
                            else:
                                print("El nombre no puede estar vacío. Por favor, intenta de nuevo.")

                    elif selection_2 == "3":
                        if entry == "Ninguna" or familiar == "Ninguno":
                            print("Por favor, completa todos los campos antes de buscar.")
                        else:
                            print(f"Buscando ruta desde {entry} para visitar a {family_member}...")
                            route = bfs(start, end)
                            if route:
                                # Leer el mapa desde el archivo
                                ruta_mapa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mictlanMapeado.txt')
                                with open(ruta_mapa, 'r') as file:
                                    map = [line.strip().split() for line in file.readlines()]
                                
                                # Marcar la ruta en el mapa
                                for i, coord in enumerate(route):
                                    x, y = coord
                                    if i == 0:  # Entrada
                                        map[x][y] = 'E'
                                    elif i == len(route) - 1:  # Destino
                                        map[x][y] = 'X'
                                    else:  # Ruta
                                        map[x][y] = 'R'
                                
                                # Imprimir el mapa modificado
                                print("\nMapa de ruta:")
                                for row in map:
                                    print(' '.join(row))
                                break
                            else:
                                print("No se encontró una ruta válida para visitar al familiar.")

                    elif selection_2 == "4":
                        print("Regresando al menú principal...")
                        break

                    else:  
                        print("Selección no válida. Por favor, elige una opción del 1 al 4.")

            elif selection == "3":
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            elif selection == "9":
                ubication = None
                name = None
                while True:
                    # Selección de agregar familiar para administrador
                    selection_3 = input("Por favor, elige una opción:\n"
                        f"1. Nombre del familiar: '{name}'\n"
                        f"2. Ubicación del familiar: '{ubication}'\n"
                        "3. Agregar familiar\n"
                        "4. Salir\n"
                        "Presiona Enter para continuar...\n")
                    
                    if selection_3 == "1": # Establecer nombre del familiar
                        name = input("Por favor, ingresa el nombre del familiar: ")
                        if not name.strip():
                            print("El nombre no puede estar vacío. Por favor, intenta de nuevo.")
                        else:
                            print(f"Nombre del familiar establecido como: {name}")

                    elif selection_3 == "2": # Establecer ubicación del familiar
                        ubication = None
                        x = input("Por favor, ingresa la coordenada X de la ubicación del familiar: ")
                        if not x.strip():
                            print("La coordenada X no puede estar vacía. Por favor, intenta de nuevo.")
                            continue
                        y = input("Por favor, ingresa la coordenada Y de la ubicación del familiar: ")
                        if not y.strip():
                            print("La coordenada Y no puede estar vacía. Por favor, intenta de nuevo.")
                            continue
                        ubication = (int(x), int(y))
                        
                        # Validar ubicación
                        if ubication == (0, 10) or ubication == (20, 10) or ubication == (2, 45) or ubication == (10, 32) or ubication == (10, 0):
                                print("No se puede agregar un familiar en una entrada del cementerio. Por favor, elige una ubicación válida dentro del cementerio.")
                        else:
                            if ubication in grafo:
                                print(f"Ubicación del familiar establecida como: {ubication}")
                            else:
                                print(f"La ubicación {ubication} no es válida. Por favor, intenta de nuevo.")
                                ubication = None

                    elif selection_3 == "3": # Agregar familiar
                        if name and ubication:
                            if nombre_existe(grafo, name):
                                print(f"El familiar {name} ya existe en el sistema. Por favor, intenta con otro nombre.")
                            else:
                                if ubication in grafo:
                                    if len(grafo[ubication]['personas']) > 4:
                                        print(f"La ubicación {ubication} ya tiene 4 familiares. No se puede agregar más.")
                                    else:
                                        grafo[ubication]['personas'].append(name)
                                        print(f"Familiar {name} agregado en la ubicación {ubication}.")

                                        # GUARDAR CAMBIOS EN mictlanGrafo.py
                                        import pprint
                                        # Ruta absoluta al directorio del script actual
                                        script_dir = os.path.dirname(os.path.abspath(__file__))

                                        # Ruta completa del archivo a sobrescribir
                                        file_graph = os.path.join(script_dir, "mictlanGrafo.py")
                                        with open(file_graph, "w", encoding="utf-8") as file:
                                            file.write("grafo = ")
                                            texto_grafo = pprint.pformat(grafo, indent=4, width=250)
                                            file.write(texto_grafo)
                                            file.write("\n")
                                else:
                                    print(f"La ubicación {ubication} no es válida. Por favor, intenta de nuevo.")
                        else:
                            print("Por favor, completa todos los campos antes de agregar un familiar.")
                    
                    elif selection_3 == "4":
                        print("Regresando al menú principal...")
                        break
                            
if __name__ == "__main__":
    main()        