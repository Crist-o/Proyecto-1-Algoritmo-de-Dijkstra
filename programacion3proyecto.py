"""
Nombre completo: Cristopher Altamirano Hernandez 
Titulo: Proyecto del algoritmo de Dijkstra con Programacion Orientada a Objetos
Fecha: 14/10/2026
Materia: Programacion 3
Profesor: Diego Alberto Ayala Vazquez

Descripcion: Este proyecto implementa el algoritmo de Dijkstra
utilizando programación orientada a objetos en Python.
Se representa un grafo ponderado mediante una lista de adyacencia 
y se permite calcular la distancia mínima y la ruta óptima entre dos nodos especificados.
El ejemplo de uso simula una red de transporte, mostrando cómo encontrar la ruta más corta
desde un nodo de origen hasta un nodo de destino.

"""

import heapq

class Graph:
    """
    Clase para representar un grafo ponderado mediante lista de adyacencia.
    Soporta grafos dirigidos y no dirigidos.
    """
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}

    def add_node(self, node):
        """Añade un nodo al grafo si no existe."""
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        """
        Añade una arista ponderada entre el nodo 'u' y el nodo 'v'.
        """
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def dijkstra(self, start_node, target_node):
        """
        Calcula la distancia mínima y la ruta óptima entre start_node y target_node.
        Retorna una tupla: (costo_total, [secuencia_de_nodos])
        """
        # Validación de existencia de nodos
        if start_node not in self.adj_list or target_node not in self.adj_list:
            return float('inf'), []

        # Distancias iniciales a infinito y registro de nodos previos
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0
        previous_nodes = {node: None for node in self.adj_list}

        # Cola de prioridad (min-heap): guarda tuplas de la forma (distancia_acumulada, nodo)
        pq = [(0, start_node)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            # Si encontramos una distancia mayor a la ya registrada, omitimos
            if current_distance > distances[current_node]:
                continue

            # Si alcanzamos el destino, podemos finalizar el procesamiento
            if current_node == target_node:
                break

            # Relajación de aristas contiguas
            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstrucción de la ruta desde el destino hacia el origen
        path = []
        curr = target_node
        while curr is not None:
            path.append(curr)
            curr = previous_nodes[curr]
        path.reverse()

        # Si el nodo inicial no es la cabeza de la ruta, no existe camino
        if not path or path[0] != start_node:
            return float('inf'), []

        return distances[target_node], path


# ==========================================
# Ejemplo de uso: Red de Transporte / Enrutamiento
# ==========================================
if __name__ == "__main__":
    red_transporte = Graph(directed=False)

    # Definición de conexiones y costos (pesos)
    red_transporte.add_edge('Origen', 'A', 4)
    red_transporte.add_edge('Origen', 'B', 2)
    red_transporte.add_edge('A', 'B', 1)
    red_transporte.add_edge('A', 'C', 5)
    red_transporte.add_edge('B', 'C', 8)
    red_transporte.add_edge('B', 'D', 10)
    red_transporte.add_edge('C', 'D', 2)
    red_transporte.add_edge('C', 'Destino', 6)
    red_transporte.add_edge('D', 'Destino', 3)

    origen = 'Origen'
    destino = 'Destino'

    costo_total, ruta = red_transporte.dijkstra(origen, destino)

    print(f"--- RESULTADOS DE ENRUTAMIENTO ---")
    print(f"Nodo Origen : {origen}")
    print(f"Nodo Destino: {destino}")
    print(f"Costo/Distancia Total Mínima: {costo_total}")
    print(f"Ruta óptima: {' -> '.join(ruta)}")