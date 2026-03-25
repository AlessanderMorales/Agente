from agentes.reglas_tictactoe import JUGADOR_X, JUGADOR_O, juego_terminado, puntaje_final
from agentes.AgenteJugador import AgenteJugador

def imprimir_tablero(tablero):
    simbolos = {0: ' ', 1: 'X', -1: 'O'}
    print(f"\n {simbolos[tablero[0]]} | {simbolos[tablero[1]]} | {simbolos[tablero[2]]} ")
    print("---+---+---")
    print(f" {simbolos[tablero[3]]} | {simbolos[tablero[4]]} | {simbolos[tablero[5]]} ")
    print("---+---+---")
    print(f" {simbolos[tablero[6]]} | {simbolos[tablero[7]]} | {simbolos[tablero[8]]} \n")

def jugar():
    # Estado inicial: tablero vacío (9 ceros)
    tablero = (0, 0, 0, 0, 0, 0, 0, 0, 0)
    
    # El humano jugará con X (JUGADOR_X) y el agente con O (JUGADOR_O)
    agente = AgenteJugador(jugador=JUGADOR_O, profundidad=9)
    
    print("=== TRES EN RAYA con Poda Alfa-Beta ===")
    print("Tú juegas con 'X' y la IA juega con 'O'.")
    print("Las posiciones van del 0 al 8, como se muestra a continuación:\n")
    print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 \n")
    
    turno_actual = JUGADOR_X # Las X empiezan
    
    while not juego_terminado(tablero):
        imprimir_tablero(tablero)
        
        if turno_actual == JUGADOR_X: # Turno del Humano
            while True:
                try:
                    movimiento = int(input("Ingresa tu jugada (0-8): "))
                    if 0 <= movimiento <= 8 and tablero[movimiento] == 0:
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
