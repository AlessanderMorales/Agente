import pygame
import sys
from agentes.reglas_tictactoe_4x4x4 import JUGADOR_X, JUGADOR_O, juego_terminado, puntaje_final
from agentes.AgenteJugador_4x4x4 import AgenteJugador4x4x4

# Configuración Pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe 3D (4x4x4) con IA Alfa-Beta")

# Colores
BG_COLOR = (30, 30, 30)
GRID_COLOR = (200, 200, 200)
TEXT_COLOR = (255, 255, 255)
X_COLOR = (255, 100, 100)
O_COLOR = (100, 100, 255)

# Fuentes
font = pygame.font.SysFont('Arial', 40, bold=True)
small_font = pygame.font.SysFont('Arial', 24)
info_font = pygame.font.SysFont('Arial', 32, bold=True)

# Parámetros visuales
QUAD_SIZE = 400
BOARD_SIZE = 300
CELL_SIZE = BOARD_SIZE // 4
PADDING = (QUAD_SIZE - BOARD_SIZE) // 2

def draw_board(tablero, turno_actual, jugando, mensaje_fin):
    screen.fill(BG_COLOR)
    
    # Dibujar los 4 cuadrantes (Z = 0, 1, 2, 3)
    for z in range(4):
        # Determinar posición del cuadrante en 2x2
        col = z % 2
        row = z // 2
        q_x = col * QUAD_SIZE
        q_y = row * QUAD_SIZE
        
        # Etiqueta Z
        label = small_font.render(f"Capa Z = {z}", True, TEXT_COLOR)
        screen.blit(label, (q_x + QUAD_SIZE // 2 - label.get_width() // 2, q_y + 10))
        
        # Inicio del tablero en este cuadrante
        board_start_x = q_x + PADDING
        board_start_y = q_y + PADDING
        
        # Dibujar celdas
        for y in range(4):
            for x in range(4):
                rect = pygame.Rect(board_start_x + x * CELL_SIZE, board_start_y + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRID_COLOR, rect, 2)
                
                # Dibujar ficha X u O
                idx = z * 16 + y * 4 + x
                ficha = tablero[idx]
                if ficha == JUGADOR_X:
                    text = font.render('X', True, X_COLOR)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)
                elif ficha == JUGADOR_O:
                    text = font.render('O', True, O_COLOR)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    # Dibujar mensaje inferior
    if jugando:
        txt = "Tu turno (X)" if turno_actual == JUGADOR_X else "Pensando... (O)"
        color = X_COLOR if turno_actual == JUGADOR_X else O_COLOR
    else:
        txt = mensaje_fin
        color = (255, 255, 0)
        
    msg_surface = info_font.render(txt, True, color)
    screen.blit(msg_surface, (WIDTH // 2 - msg_surface.get_width() // 2, HEIGHT - 50))

    pygame.display.flip()

def get_clicked_cell(pos):
    mx, my = pos
    col = mx // QUAD_SIZE
    row = my // QUAD_SIZE
    z = row * 2 + col
    
    q_x = col * QUAD_SIZE
    q_y = row * QUAD_SIZE
    board_start_x = q_x + PADDING
    board_start_y = q_y + PADDING
    
    if board_start_x <= mx <= board_start_x + BOARD_SIZE and board_start_y <= my <= board_start_y + BOARD_SIZE:
        x = (mx - board_start_x) // CELL_SIZE
        y = (my - board_start_y) // CELL_SIZE
        if 0 <= x < 4 and 0 <= y < 4:
            return z * 16 + y * 4 + x
            
    return None

def main():
    tablero = tuple([0] * 64)
    turno_actual = JUGADOR_X
    jugando = True
    mensaje_fin = ""
    agente = AgenteJugador4x4x4(jugador=JUGADOR_O, profundidad=2)
    
    clock = pygame.time.Clock()
    
    # Dibujo inicial
    draw_board(tablero, turno_actual, jugando, mensaje_fin)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Interacción Humano
            if event.type == pygame.MOUSEBUTTONDOWN and jugando and turno_actual == JUGADOR_X:
                celda = get_clicked_cell(event.pos)
                if celda is not None and tablero[celda] == 0:
                    nuevo_estado = list(tablero)
                    nuevo_estado[celda] = JUGADOR_X
                    tablero = tuple(nuevo_estado)
                    turno_actual = JUGADOR_O
                    
                    # Verificar si ganó
                    if juego_terminado(tablero):
                        jugando = False
                        ganador = puntaje_final(tablero)
                        if ganador == JUGADOR_X:
                            mensaje_fin = "¡Ganaste!"
                        elif ganador == JUGADOR_O:
                            mensaje_fin = "¡La IA ganó!"
                        else:
                            mensaje_fin = "¡Empate!"
                            
                    # Dibujar inmediatamente para actualizar "Pensando..."
                    draw_board(tablero, turno_actual, jugando, mensaje_fin)
                        
        # Turno de la IA
        if jugando and turno_actual == JUGADOR_O:
            # Dibujamos antes para asegurar que dice "Pensando..."
            draw_board(tablero, turno_actual, jugando, mensaje_fin)
            pygame.event.pump() # Mantener eventos procesándose para que la ventana no se cuelgue momentáneamente
            
            mejor_estado = agente.obtener_mejor_movimiento(tablero)
            if mejor_estado:
                tablero = mejor_estado
            turno_actual = JUGADOR_X
            
            # Verificar ganar
            if juego_terminado(tablero):
                jugando = False
                ganador = puntaje_final(tablero)
                if ganador == JUGADOR_X:
                    mensaje_fin = "¡Ganaste!"
                elif ganador == JUGADOR_O:
                    mensaje_fin = "¡La IA (Alfa-Beta) ganó!"
                else:
                    mensaje_fin = "¡Es un empate!"
                    
            draw_board(tablero, turno_actual, jugando, mensaje_fin)
            
        clock.tick(30)

if __name__ == "__main__":
    main()
