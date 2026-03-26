import math
import random

def simulated_annealing(problema, plan_temperatura=None, **kwargs):
    """
    Algoritmo de Recocido Simulado (Simulated Annealing).
    Acepta estados peores probabilísticamente para escapar de óptimos locales.
    La probabilidad disminuye con la 'temperatura'.
    """
    actual = problema.estado_inicial()
    
    # Schedule por defecto: T = 1000 * (0.95 ^ t) reduciendo temperatura lentamente
    if plan_temperatura is None:
        plan_temperatura = lambda t: 1000 * (0.95 ** t) if t < 10000 else 0
        
    t = 0
    while True:
        T = plan_temperatura(t)
        if T == 0:
            # La temperatura llegó a 0, termina el proceso
            return actual
            
        vecinos = problema.obtener_vecinos(actual)
        if not vecinos:
            return actual
            
        # Elegir un vecino aleatoriamente
        siguiente = random.choice(vecinos)
        
        # Diferencia del valor (∆E)
        delta_e = problema.valor(siguiente) - problema.valor(actual)
        
        if delta_e > 0:
            # Si el vecino es mejor, lo aceptamos
            actual = siguiente
        else:
            # Si el vecino es peor, lo aceptamos con una probabilidad e^(∆E / T)
            probabilidad_aceptacion = math.exp(delta_e / T)
            if random.random() < probabilidad_aceptacion:
                actual = siguiente
                
        t += 1
