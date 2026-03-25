import math
from agentes.reglas_tictactoe import JUGADOR_X, JUGADOR_O, movimientos_posibles, juego_terminado, evaluar_tablero

def poda_alfa_beta(tablero, profundidad, alpha, beta, jugador):
    if profundidad == 0 or juego_terminado(tablero):
        return evaluar_tablero(tablero)
        
    # Ordenar los hijos para maximizar la poda (move ordering)
    # JUGADOR_X intentará revisar estados con alto valor primero, JUGADOR_O con bajo valor primero
    hijos = movimientos_posibles(tablero)
    hijos.sort(key=evaluar_tablero, reverse=(jugador == JUGADOR_X))
    
    if jugador == JUGADOR_X:
        maxEval = -math.inf
        for hijo in hijos:
            ev = poda_alfa_beta(hijo, profundidad - 1, alpha, beta, JUGADOR_O)
            maxEval = max(maxEval, ev)
            alpha = max(alpha, ev)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = math.inf
        for hijo in hijos:
            ev = poda_alfa_beta(hijo, profundidad - 1, alpha, beta, JUGADOR_X)
            minEval = min(minEval, ev)
            beta = min(beta, ev)
            if beta <= alpha:
                break
        return minEval
