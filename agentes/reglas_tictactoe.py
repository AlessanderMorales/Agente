import math

JUGADOR_X = 1
JUGADOR_O = -1



def revisar_ganador(tablero):
    lineas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for linea in lineas:
        if tablero[linea[0]] != 0 and tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]]:
            return tablero[linea[0]]
    return 0

def juego_terminado(tablero):
    return revisar_ganador(tablero) != 0 or tablero.count(0) == 0

def puntaje_final(tablero):
    return revisar_ganador(tablero)

def movimientos_posibles(tablero):
    if juego_terminado(tablero):
        return []
        
    turno = JUGADOR_X if tablero.count(0) % 2 != 0 else JUGADOR_O
    hijos = []
    
    for i in range(9):
        if tablero[i] == 0:
            nuevo_estado = list(tablero)
            nuevo_estado[i] = turno
            hijos.append(tuple(nuevo_estado))
            
    return hijos

def evaluar_tablero(tablero):
    ganador = revisar_ganador(tablero)
    if ganador == JUGADOR_X:
        return 1000  # Ganada
    if ganador == JUGADOR_O:
        return -1000
    
    # Heurística para "posibles ganadas"
    valor = 0
    lineas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for linea in lineas:
        fichas = [tablero[linea[0]], tablero[linea[1]], tablero[linea[2]]]
        
        # Posibles ganadas para JUGADOR_X (valor alto)
        if fichas.count(JUGADOR_X) == 2 and fichas.count(0) == 1:
            valor += 10
        elif fichas.count(JUGADOR_X) == 1 and fichas.count(0) == 2:
            valor += 1
            
        # Posibles ganadas para JUGADOR_O (valor alto negativo)
        if fichas.count(JUGADOR_O) == 2 and fichas.count(0) == 1:
            valor -= 10
        elif fichas.count(JUGADOR_O) == 1 and fichas.count(0) == 2:
            valor -= 1
            
    return valor
