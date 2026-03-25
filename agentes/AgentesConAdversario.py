import math

MAX = 1
MIN = -1

def MiniMax(estado, jugador):
    if es_terminal(estado):
        return utilidad(estado)
    
    if jugador == MAX:
        return valorMax(estado)
    
    if jugador == MIN:
        return valorMin(estado)

def valorMax(estado):
    v = -math.inf
    
    for hijo in sucesores(estado):
        v = max(v, MiniMax(hijo, MIN))
        
    return v

def valorMin(estado):
    v = math.inf
    
    for hijo in sucesores(estado):
        v = min(v, MiniMax(hijo, MAX))
        
    return v

def revisar_ganador(estado):
    lineas = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for linea in lineas:
        if estado[linea[0]] != 0 and estado[linea[0]] == estado[linea[1]] == estado[linea[2]]:
            return estado[linea[0]]
    return 0

def es_terminal(estado):
    return revisar_ganador(estado) != 0 or estado.count(0) == 0

def utilidad(estado):
    return revisar_ganador(estado)

def sucesores(estado):
    if es_terminal(estado):
        return []
        
    turno = MAX if estado.count(0) % 2 != 0 else MIN
    hijos = []
    
    for i in range(9):
        if estado[i] == 0:
            nuevo_estado = list(estado)
            nuevo_estado[i] = turno
            hijos.append(tuple(nuevo_estado))
            
    return hijos
