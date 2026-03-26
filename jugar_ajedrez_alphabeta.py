import chess
import math

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 100
}

def evaluar_tablero(board: chess.Board):
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -99990  # Blancas reciben mate -> Negras ganan (valor muy negativo)
        else:
            return 99990   # Negras reciben mate -> Blancas ganan (valor muy positivo)
            
    if board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_fivefold_repetition():
        return 0
        
    evaluation = 0
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece is not None:
            val = PIECE_VALUES.get(piece.piece_type, 0)
            if piece.color == chess.WHITE:
                evaluation += val
            else:
                evaluation -= val
                
    return evaluation

def minimax_alphabeta(board: chess.Board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluar_tablero(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def obtener_mejor_movimiento(board: chess.Board, depth, is_white):
    mejor_movimiento = None
    if is_white:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alphabeta(board, depth - 1, -math.inf, math.inf, False)
            board.pop()
            # Si encontramos un mate inminente o mejor evaluación
            if eval > max_eval:
                max_eval = eval
                mejor_movimiento = move
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax_alphabeta(board, depth - 1, -math.inf, math.inf, True)
            board.pop()
            # Buscamos minimizar
            if eval < min_eval:
                min_eval = eval
                mejor_movimiento = move
                
    return mejor_movimiento

def jugar():
    board = chess.Board()
    print("=== AJEDREZ con Poda Alfa-Beta ===")
    print("Reglas y comandos:")
    print("1. Juegas con las BLANCAS (mayúsculas). La IA juega con las NEGRAS (minúsculas).")
    print("2. Debes ingresar tus movimientos usando el formato UCI (Universal Chess Interface).")
    print("   El formato consiste en la coordenada de origen y la de destino.")
    print("   - Ejemplo: Mover un peón de e2 a e4 -> e2e4")
    print("   - Ejemplo: Mover el caballo de g1 a f3 -> g1f3")
    print("   - Ejemplo: Enroque corto (rey e1 a g1) -> e1g1")
    print("\nCoordenadas del tablero (referencia inicial):")
    print("  a b c d e f g h")
    print("8 r n b q k b n r 8")
    print("7 p p p p p p p p 7")
    print("6 . . . . . . . . 6")
    print("5 . . . . . . . . 5")
    print("4 . . . . . . . . 4")
    print("3 . . . . . . . . 3")
    print("2 P P P P P P P P 2")
    print("1 R N B Q K B N R 1")
    print("  a b c d e f g h")
    print("\n¡Que empiece el juego!")
    
    profundidad = 3 # Un valor mayor hará que tarde mucho la IA en Python
    
    while not board.is_game_over():
        print("\n" + str(board) + "\n")
        
        if board.turn == chess.WHITE: # Turno del humano
            while True:
                movimiento_uci = input("Tu turno (Blancas). Ingresa movimiento UCI: ").strip()
                try:
                    move = chess.Move.from_uci(movimiento_uci)
                    if move in board.legal_moves:
                        board.push(move)
                        break
                    else:
                        print("Movimiento ilegal. Intenta de nuevo.")
                except ValueError:
                    print("Formato inválido. Usa formato UCI (ej. e2e4).")
        else: # Turno de la IA
            print(f"La IA (Negras) está pensando... (profundidad={profundidad})")
            mejor_mov = obtener_mejor_movimiento(board, profundidad, is_white=False)
            if mejor_mov:
                print(f"La IA juega: {mejor_mov.uci()}")
                board.push(mejor_mov)
            else:
                print("La IA no ha encontrado jugada válida.")
                break
                
    print("\nJuego terminado.")
    print(board)
    print("Resultado final:", board.result())

if __name__ == "__main__":
    try:
        jugar()
    except KeyboardInterrupt:
        print("\nJuego interrumpido por el usuario. ¡Hasta la próxima!")
