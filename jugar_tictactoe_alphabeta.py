import math
from agentes.reglas_tictactoe import JUGADOR_X, JUGADOR_O, juego_terminado, puntaje_final
from agentes.AgenteJugador import AgenteJugador

def imprimir_tablero(tablero):
    N = int(math.sqrt(len(tablero)))
    simbolos = {0: ' ', 1: 'X', -1: 'O'}
    print("\n")
    for i in range(N):
        fila = [f" {simbolos[tablero[i*N + j]]} " for j in range(N)]
        print("|".join(fila))
        if i < N - 1:
            print("---" + ("+---" * (N - 1)))
    print("\n")

def jugar():
    print("=== TRES EN RAYA con Poda Alfa-Beta ===")
    while True:
        try:
            N = int(input("Ingresa el tamaño del tablero N (ej. 3 para 3x3, 4 para 4x4): "))
            if N >= 3:
                break
            else:
                print("El tamaño debe ser al menos 3.")
        except ValueError:
            print("Entrada inválida. Ingresa un número.")
            
    # Estado inicial: tablero vacío (N*N ceros)
    tablero = tuple([0] * (N * N))
    
    profundidad = 9 if N == 3 else (4 if N == 4 else 3)
    
    # El humano jugará con X (JUGADOR_X) y el agente con O (JUGADOR_O)
    agente = AgenteJugador(jugador=JUGADOR_O, profundidad=profundidad)
    
    print("\nTú juegas con 'X' y la IA juega con 'O'.")
    print(f"Las posiciones van del 0 al {N*N - 1}, como se muestra a continuación:\n")
    
    for i in range(N):
        fila = [f"{i*N+j:2d}" for j in range(N)]
        print(" | ".join(fila))
        if i < N - 1:
            print("---+" * (N - 1) + "---")
    print("\n")
    
    turno_actual = JUGADOR_X # Las X empiezan
    
    while not juego_terminado(tablero):
        imprimir_tablero(tablero)
        
        if turno_actual == JUGADOR_X: # Turno del Humano
            while True:
                try:
                    movimiento = int(input(f"Ingresa tu jugada (0-{len(tablero)-1}): "))
                    if 0 <= movimiento < len(tablero) and tablero[movimiento] == 0:
                        nuevo_estado = list(tablero)
                        nuevo_estado[movimiento] = JUGADOR_X
                        tablero = tuple(nuevo_estado)
                        break
                    else:
                        print("Movimiento inválido o casilla ocupada. Intenta de nuevo.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
            turno_actual = JUGADOR_O
            
        else: # Turno de la IA (Alfa-Beta)
            print("La IA está pensando su movimiento con Poda Alfa-Beta...")
            mejor_estado = agente.obtener_mejor_movimiento(tablero)
            if mejor_estado:
                tablero = mejor_estado
            turno_actual = JUGADOR_X

    imprimir_tablero(tablero)
    ganador = puntaje_final(tablero)
    if ganador == JUGADOR_X:
        print("¡Felicidades! Has ganado.")
    elif ganador == JUGADOR_O:
        print("La IA (Poda Alfa-Beta) ha ganado. ¡Mejor suerte la próxima vez!")
    else:
        print("¡Es un empate!")

if __name__ == "__main__":
    try:
        jugar()
    except KeyboardInterrupt:
        print("\nJuego terminado.")
