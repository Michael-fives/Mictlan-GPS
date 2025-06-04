# Se crea el código lector del mapeado para crear el grafo del cementerio
def read_map(filename):
    """
    Lee un archivo de texto que contiene una matriz de adyacencia binaria.

    Parámetros:
    - filename (str): Ruta del archivo que contiene la matriz del cementerio.

    Retorna:
    - list of list of int: Matriz de adyacencia leída desde el archivo.
    """
    adjacency = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            adjacency.append(row)
    return adjacency


def obtain_neighbors(adjacency, row, col):
    """
    Obtiene los vecinos válidos (adyacentes) de una celda específica en una matriz.

    Parámetros:
    - adjacency (list of list of int): Matriz que representa el mapa.
    - row (int): Fila de la celda actual.
    - col (int): Columna de la celda actual.

    Retorna:
    - list of tuple: Lista de coordenadas (fila, columna) de los vecinos disponibles.
    """
    neighbors = []
    rows = len(adjacency)
    cols = len(adjacency[0]) if rows > 0 else 0
    movements = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    for dr, dc in movements:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and adjacency[new_row][new_col] == 1:
            neighbors.append((new_row, new_col))
    return neighbors

def create_adjacency_list(adjacency):
    """
    Convierte una matriz de adyacencia en una lista de adyacencia basada en coordenadas.

    Parámetros:
    - adjacency (list of list of int): Matriz que representa el mapa.

    Retorna:
    - dict: Diccionario con claves como tuplas (fila, columna) y valores como listas de vecinos.
    """
    adjacency_list = {}
    for row in range(len(adjacency)):
        for col in range(len(adjacency[0])):
            if adjacency[row][col] == 1:
                neighbors = obtain_neighbors(adjacency, row, col)
                adjacency_list[(row, col)] = neighbors
    return adjacency_list

def save_adjacency_list(adjacency_list, filename):
    """
    Guarda la lista de adyacencia en un archivo .py como estructura de diccionario de Python.

    Parámetros:
    - adjacency_list (dict): Diccionario con nodos y vecinos.
    - filename (str): Ruta del archivo de salida.
    """
    with open(filename, 'w') as file:
        file.write("grafo = {\n")
        for vertex, neighbors in adjacency_list.items():
            neighbors_str = ', '.join(f"{neighbor}" for neighbor in neighbors)
            # personas vacío por ahora
            file.write(f"    {vertex}: {{'vecinos': [{neighbors_str}], 'personas': []}},\n")
        file.write("}\n")

if __name__ == "__main__":
    input_filename = 'mictlanMapeado.txt'
    output_filename = 'mictlanGrafo.py'
    
    print(f"Reading map from {input_filename}...")
    adjacency = read_map(input_filename)
    print("Creating adjacency list...")
    adjacency_list = create_adjacency_list(adjacency)
    print("Saving adjacency list to file...")
    save_adjacency_list(adjacency_list, output_filename)
    print(f"Adjacency list saved to {output_filename}")