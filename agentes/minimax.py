import math
from agentes.reglas_tictactoe import JUGADOR_X, JUGADOR_O, movimientos_posibles, juego_terminado, puntaje_final

def minimax(tablero, jugador):
    if juego_terminado(tablero):
        return puntaje_final(tablero)
    
    if jugador == JUGADOR_X:
        return valor_max(tablero)
    
    if jugador == JUGADOR_O:
        return valor_min(tablero)

def valor_max(tablero):
    v = -math.inf
    
    for hijo in movimientos_posibles(tablero):
        v = max(v, minimax(hijo, JUGADOR_O))
        
    return v

def valor_min(tablero):
    v = math.inf
    
    for hijo in movimientos_posibles(tablero):
        v = min(v, minimax(hijo, JUGADOR_X))
        
    return v
