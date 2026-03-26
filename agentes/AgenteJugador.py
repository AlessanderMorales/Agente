import math
from agentes.reglas_tictactoe import JUGADOR_X, JUGADOR_O, movimientos_posibles
from agentes.poda_alpha_beta import poda_alfa_beta

class AgenteJugador:
    def __init__(self, jugador, profundidad=9):
        self.jugador = jugador
        self.profundidad = profundidad

    def obtener_mejor_movimiento(self, tablero):
        mejor_movimiento = None
        alpha = -math.inf
        beta = math.inf
        
        if self.jugador == JUGADOR_X:
            mejor_valor = -math.inf
            for hijo in movimientos_posibles(tablero):
                valor = poda_alfa_beta(hijo, self.profundidad - 1, alpha, beta, JUGADOR_O)
                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = hijo
                alpha = max(alpha, mejor_valor)
        else:
            mejor_valor = math.inf
            for hijo in movimientos_posibles(tablero):
                valor = poda_alfa_beta(hijo, self.profundidad - 1, alpha, beta, JUGADOR_X)
                if valor < mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = hijo
                beta = min(beta, mejor_valor)
                    
        return mejor_movimiento
