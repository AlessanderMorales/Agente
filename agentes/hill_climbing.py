def hill_climbing(problema, **kwargs):
    """
    Algoritmo de Ascenso de Colinas (Hill Climbing).
    Se mueve siempre al vecino con mayor valor.
    Si no hay vecinos con mejor valor, retorna el estado actual (pico local).
    """
    actual = problema.estado_inicial()
    while True:
        vecinos = problema.obtener_vecinos(actual)
        if not vecinos:
            return actual
        
        mejor_vecino = None
        mejor_valor = problema.valor(actual)
        
        for vecino in vecinos:
            valor_vecino = problema.valor(vecino)
            # Maximizamos el valor de la función heurística
            if valor_vecino > mejor_valor:
                mejor_valor = valor_vecino
                mejor_vecino = vecino
        
        if mejor_vecino is None:
            # Ningún vecino mejoró el estado actual; hemos llegado a un máximo local
            return actual
            
        actual = mejor_vecino
