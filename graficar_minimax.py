import sys
import subprocess

# Auto-instalar dependencias si faltan
def instalar_dependencias():
    try:
        import networkx
        import matplotlib.pyplot as plt
    except ImportError:
        print("Instalando networkx y matplotlib...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "networkx", "matplotlib", "--quiet"])

instalar_dependencias()

import networkx as nx
import matplotlib.pyplot as plt
from agentes.reglas_tictactoe import movimientos_posibles, juego_terminado, puntaje_final, JUGADOR_X, JUGADOR_O
from agentes.minimax import minimax

def turno_actual(tablero):
    return JUGADOR_X if tablero.count(0) % 2 != 0 else JUGADOR_O


def estado_a_string(tablero, valor_minimax=None):
    simbolos = {0: ' ', 1: 'X', -1: 'O'}
    fila1 = f"{simbolos[tablero[0]]}|{simbolos[tablero[1]]}|{simbolos[tablero[2]]}"
    fila2 = f"{simbolos[tablero[3]]}|{simbolos[tablero[4]]}|{simbolos[tablero[5]]}"
    fila3 = f"{simbolos[tablero[6]]}|{simbolos[tablero[7]]}|{simbolos[tablero[8]]}"
    tablero = f"{fila1}\n-----\n{fila2}\n-----\n{fila3}"
    if valor_minimax is not None:
        return f"{tablero}\nV={valor_minimax}"
    return tablero

def construir_arbol(estado_inicial):
    G = nx.DiGraph()
    visitados = set()
    cola = [estado_inicial]
    valor_inicial = minimax(estado_inicial, turno_actual(estado_inicial))
    G.add_node(estado_inicial, label=estado_a_string(estado_inicial, valor_inicial), valor=valor_inicial)
    
    while cola:
        estado_actual = cola.pop(0)

        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)

        if not juego_terminado(estado_actual):
            for hijo in movimientos_posibles(estado_actual):
                if hijo not in G:
                    valor_hijo = minimax(hijo, turno_actual(hijo))
                    G.add_node(hijo, label=estado_a_string(hijo, valor_hijo), valor=valor_hijo)
                G.add_edge(estado_actual, hijo)
                cola.append(hijo)

    return G


def mostrar_grafo(G):
    pos = nx.spring_layout(G, seed=42) # para intentar que se vea ordenado
    
    # Dibujar usando matplotlib
    plt.figure(figsize=(12, 8))
    
    # Obtener etiquetas
    labels = nx.get_node_attributes(G, 'label')
    
    # Colorear nodos según valor Minimax y terminal
    color_map = []
    for node in G:
        valor = G.nodes[node].get('valor')
        if juego_terminado(node):
            if puntaje_final(node) == 1:
                color_map.append('lightgreen') # Gana X
            elif puntaje_final(node) == -1:
                color_map.append('lightcoral') # Gana O
            else:
                color_map.append('lightgrey')   # Empate
        elif valor == 1:
            color_map.append('deepskyblue')   # buena para JUGADOR_X
        elif valor == -1:
            color_map.append('orange')       # buena para JUGADOR_O
        else:
            color_map.append('lightblue')
            
    nx.draw(G, pos, labels=labels, node_color=color_map, with_labels=True, 
            node_size=3000, font_size=8, font_family='monospace', 
            arrows=True, arrowsize=20, node_shape='s')
            
    # Título y leyenda simples
    plt.title("Grafo de Estados del Tres en Raya (Minimax)")
    plt.axis("off") # apagar los ejes
    
    print("Mostrando el grafo en una ventana... ¡Ciérrala para continuar!")
    plt.show()

if __name__ == "__main__":
    # Escogemos un tablero inicial casi terminado para que el grafo no sea gigantesco
    # X empieza, X e O han jugado varias veces.
    # Tablero inicial de prueba:
    # X | O | X
    # O | X |  
    # O |   |  
    estado_prueba = (
        1, -1, 1,
       -1,  1, 0,
       -1,  0, 0
    )
    
    print("Construyendo el árbol de decisiones...")
    grafo = construir_arbol(estado_prueba)
    print(f"Grafo construido con {grafo.number_of_nodes()} nodos y {grafo.number_of_edges()} aristas.")
    
    mostrar_grafo(grafo)
