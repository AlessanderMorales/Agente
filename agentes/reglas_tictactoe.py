import math

JUGADOR_X = 1
JUGADOR_O = -1



def revisar_ganador(tablero):
    N = int(math.sqrt(len(tablero)))
    lineas = []
    for i in range(N):
        lineas.append([i * N + j for j in range(N)]) # Filas
        lineas.append([j * N + i for j in range(N)]) # Columnas
    lineas.append([i * N + i for i in range(N)])     # Diagonal principal
    lineas.append([i * N + (N - 1 - i) for i in range(N)]) # Diagonal secundaria

    for linea in lineas:
        primer_elemento = tablero[linea[0]]
        if primer_elemento != 0 and all(tablero[i] == primer_elemento for i in linea):
            return primer_elemento
    return 0

def juego_terminado(tablero):
    return revisar_ganador(tablero) != 0 or tablero.count(0) == 0

def puntaje_final(tablero):
    return revisar_ganador(tablero)

def movimientos_posibles(tablero):
    if juego_terminado(tablero):
        return []
        
    total = len(tablero)
    ceros = tablero.count(0)
    movimientos_hechos = total - ceros
    turno = JUGADOR_X if movimientos_hechos % 2 == 0 else JUGADOR_O
    
    hijos = []
    for i in range(total):
        if tablero[i] == 0:
            nuevo_estado = list(tablero)
            nuevo_estado[i] = turno
            hijos.append(tuple(nuevo_estado))
            
    return hijos

def evaluar_tablero(tablero):
    ganador = revisar_ganador(tablero)
    if ganador == JUGADOR_X:
        return 100000  # Ganada
    if ganador == JUGADOR_O:
        return -100000
    
    valor = 0
    N = int(math.sqrt(len(tablero)))
    lineas = []
    for i in range(N):
        lineas.append([i * N + j for j in range(N)])
        lineas.append([j * N + i for j in range(N)])
    lineas.append([i * N + i for i in range(N)])
    lineas.append([i * N + (N - 1 - i) for i in range(N)])

    for linea in lineas:
        fichas = [tablero[i] for i in linea]
        count_x = fichas.count(JUGADOR_X)
        count_o = fichas.count(JUGADOR_O)
        
        # Si la línea tiene X y no tiene O
        if count_x > 0 and count_o == 0:
            valor += 10 ** (count_x - 1)
        # Si la línea tiene O y no tiene X
        elif count_o > 0 and count_x == 0:
            valor -= 10 ** (count_o - 1)
            
    return valor
