import math
from agentes.reglas_tictactoe_4x4x4 import JUGADOR_X, JUGADOR_O, movimientos_posibles, juego_terminado, evaluar_tablero

def poda_alfa_beta_4x4x4(tablero, profundidad, alpha, beta, jugador):
    if profundidad == 0 or juego_terminado(tablero):
        return evaluar_tablero(tablero)
        
    hijos = movimientos_posibles(tablero)
    
    # Ordenamiento de movimientos (Move Ordering) para maximizar la poda.
    # Como evaluar 64 hijos puede ser costoso, ordenar ayuda a encontrar la mejor rama antes.
    hijos.sort(key=evaluar_tablero, reverse=(jugador == JUGADOR_X))
    
    if jugador == JUGADOR_X:
        maxEval = -math.inf
        for hijo in hijos:
            ev = poda_alfa_beta_4x4x4(hijo, profundidad - 1, alpha, beta, JUGADOR_O)
            maxEval = max(maxEval, ev)
            alpha = max(alpha, ev)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for hijo in hijos:
            ev = poda_alfa_beta_4x4x4(hijo, profundidad - 1, alpha, beta, JUGADOR_X)
            minEval = min(minEval, ev)
            beta = min(beta, ev)
            if beta <= alpha:
                break
        return minEval
