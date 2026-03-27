import math
from agentes.reglas_tictactoe_4x4x4 import JUGADOR_X, JUGADOR_O, juego_terminado, puntaje_final
from agentes.AgenteJugador_4x4x4 import AgenteJugador4x4x4

def imprimir_tablero_3d(tablero):
    simbolos = {0: '.', 1: 'X', -1: 'O'}
    print("\n" + "="*40)
    print("        TABLERO 3D (4x4x4)")
    print("="*40)
    
    for z in range(4):
        print(f"\nCapa Z = {z}:")
        for y in range(4):
            fila = [f" {simbolos[tablero[z*16 + y*4 + x]]} " for x in range(4)]
            print("|".join(fila))
            if y < 3:
                print("---" + ("+---" * 3))
    print("\n" + "="*40 + "\n")

def jugar():
    print("=== TRES EN RAYA 3D (4x4x4) con Poda Alfa-Beta ===")
            
    # Estado inicial: tablero vacío (64 ceros).
    tablero = tuple([0] * 64)
    
    # 4x4x4 tiene factor de ramificación alto, profundidad 2 recomendada para jugabilidad sin extrema lentitud.
    profundidad = 2
    
    # El humano jugará con X (JUGADOR_X) y el agente con O (JUGADOR_O)
    agente = AgenteJugador4x4x4(jugador=JUGADOR_O, profundidad=profundidad)
    
    print("\nTú juegas con 'X' y la IA juega con 'O'.")
    print("Las posiciones van del 0 al 63, correspondiendo a Z*16 + Y*4 + X.\n")
    
    for z in range(4):
        print(f"Capa Z = {z}:")
        for y in range(4):
            fila = [f"{z*16 + y*4 + x:2d}" for x in range(4)]
            print(" | ".join(fila))
            if y < 3:
                print("---+" * 3 + "---")
        print()
    print("\n")
    
    turno_actual = JUGADOR_X # Las X empiezan
    
    while not juego_terminado(tablero):
        imprimir_tablero_3d(tablero)
        
        if turno_actual == JUGADOR_X: # Turno del Humano
            while True:
                try:
                    movimiento = int(input("Ingresa tu jugada (0-63): "))
                    if 0 <= movimiento < 64 and tablero[movimiento] == 0:
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
            print("La IA está pensando su movimiento con Poda Alfa-Beta (Profundidad 2)...")
            mejor_estado = agente.obtener_mejor_movimiento(tablero)
            if mejor_estado:
                tablero = mejor_estado
            turno_actual = JUGADOR_X

    imprimir_tablero_3d(tablero)
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
