from agentes.Agente import Agente
from n_reinas import ProblemaNReinas
from agentes.hill_climbing import hill_climbing
from agentes.simulated_annealing import simulated_annealing

def main():
    N = 8
    print(f"=== Resolviendo problema de las {N}-Reinas con Búsqueda Local ===\n")
    problema = ProblemaNReinas(n=N)
    
    # Pruebas con Hill Climbing
    print("--- 1. Búsqueda con Hill Climbing (Ascenso de Colinas) ---")
    agente_hc = Agente(problema, hill_climbing)
    solucion_hc = agente_hc.resolver()
    print("\n" + "="*50 + "\n")
    
    # Pruebas con Simulated Annealing
    print("--- 2. Búsqueda con Simulated Annealing (Recocido Simulado) ---")
    agente_sa = Agente(problema, simulated_annealing)
    # Ejecutamos el agente (usando schedule de temperatura por defecto)
    solucion_sa = agente_sa.resolver()

if __name__ == "__main__":
    main()
