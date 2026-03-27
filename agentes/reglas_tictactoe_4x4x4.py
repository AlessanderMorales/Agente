JUGADOR_X = 1
JUGADOR_O = -1

# Generamos las 76 líneas ganadoras para un tablero 4x4x4
LINEAS_GANADORAS = []

# 1. 16 Pilares Z (X, Y constantes, Z varía)
for x in range(4):
    for y in range(4):
        LINEAS_GANADORAS.append(tuple(z * 16 + y * 4 + x for z in range(4)))

# 2. 16 Filas en X (Y, Z constantes, X varía)
for y in range(4):
    for z in range(4):
        LINEAS_GANADORAS.append(tuple(z * 16 + y * 4 + x for x in range(4)))

# 3. 16 Columnas en Y (X, Z constantes, Y varía)
for x in range(4):
    for z in range(4):
        LINEAS_GANADORAS.append(tuple(z * 16 + y * 4 + x for y in range(4)))

# 4. 8 Diagonales 2D en planos XY (Z constante)
for z in range(4):
    LINEAS_GANADORAS.append(tuple(z * 16 + i * 4 + i for i in range(4)))
    LINEAS_GANADORAS.append(tuple(z * 16 + i * 4 + (3 - i) for i in range(4)))

# 5. 8 Diagonales 2D en planos XZ (Y constante)
for y in range(4):
    LINEAS_GANADORAS.append(tuple(i * 16 + y * 4 + i for i in range(4)))
    LINEAS_GANADORAS.append(tuple((3 - i) * 16 + y * 4 + i for i in range(4)))

# 6. 8 Diagonales 2D en planos YZ (X constante)
for x in range(4):
    LINEAS_GANADORAS.append(tuple(i * 16 + i * 4 + x for i in range(4)))
    LINEAS_GANADORAS.append(tuple((3 - i) * 16 + i * 4 + x for i in range(4)))

# 7. 4 Diagonales 3D principales
LINEAS_GANADORAS.append(tuple(i * 16 + i * 4 + i for i in range(4)))
LINEAS_GANADORAS.append(tuple(i * 16 + i * 4 + (3 - i) for i in range(4)))
LINEAS_GANADORAS.append(tuple(i * 16 + (3 - i) * 4 + i for i in range(4)))
LINEAS_GANADORAS.append(tuple(i * 16 + (3 - i) * 4 + (3 - i) for i in range(4)))

def revisar_ganador(tablero):
    for linea in LINEAS_GANADORAS:
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
        
    total = len(tablero) # 64
    ceros = tablero.count(0)
    movimientos_hechos = total - ceros
    turno = JUGADOR_X if movimientos_hechos % 2 == 0 else JUGADOR_O
    
    hijos = []
    # Genera los hijos
    for i in range(total):
        if tablero[i] == 0:
            nuevo_estado = list(tablero)
            nuevo_estado[i] = turno
            hijos.append(tuple(nuevo_estado))
            
    return hijos

def evaluar_tablero(tablero):
    ganador = revisar_ganador(tablero)
    if ganador == JUGADOR_X:
        return 10000000  # Máxima puntuación
    if ganador == JUGADOR_O:
        return -10000000
    
    valor = 0
    for linea in LINEAS_GANADORAS:
        fichas = [tablero[i] for i in linea]
        count_x = fichas.count(JUGADOR_X)
        count_o = fichas.count(JUGADOR_O)
        
        # Si la línea tiene X y no tiene O (potencial para X)
        if count_x > 0 and count_o == 0:
            if count_x == 1:
                valor += 1
            elif count_x == 2:
                valor += 10
            elif count_x == 3:
                valor += 1000
        # Si la línea tiene O y no tiene X (potencial para O)
        elif count_o > 0 and count_x == 0:
            if count_o == 1:
                valor -= 1
            elif count_o == 2:
                valor -= 10
            elif count_o == 3:
                valor -= 1000
            
    return valor
