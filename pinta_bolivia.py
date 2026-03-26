import random
from agentes.Agente import Agente
from agentes.hill_climbing import hill_climbing
from agentes.simulated_annealing import simulated_annealing

class ProblemaColoreoBolivia:
   
    def __init__(self):
        self.departamentos = [
            'Pando', 'Beni', 'La Paz', 'Cochabamba', 'Santa Cruz', 
            'Oruro', 'Potosí', 'Chuquisaca', 'Tarija'
        ]
        self.colores = ['Azul', 'Rojo', 'Verde']
        
        # Diccionario de adyacencias (vecinos)
        self.vecinos = {
            'Pando': ['Beni', 'La Paz'],
            'Beni': ['Pando', 'La Paz', 'Cochabamba', 'Santa Cruz'],
            'La Paz': ['Pando', 'Beni', 'Cochabamba', 'Oruro'],
            'Cochabamba': ['La Paz', 'Beni', 'Santa Cruz', 'Chuquisaca', 'Potosí', 'Oruro'],
            'Santa Cruz': ['Beni', 'Cochabamba', 'Chuquisaca'],
            'Oruro': ['La Paz', 'Cochabamba', 'Potosí'],
            'Potosí': ['Oruro', 'Cochabamba', 'Chuquisaca', 'Tarija'],
            'Chuquisaca': ['Santa Cruz', 'Cochabamba', 'Potosí', 'Tarija'],
            'Tarija': ['Potosí', 'Chuquisaca']
        }

    def estado_inicial(self):
        
        return tuple(random.choice(self.colores) for _ in self.departamentos)

    def obtener_vecinos(self, estado):
       
        vecinos = []
        for i in range(len(self.departamentos)):
            color_actual = estado[i]
            for nuevo_color in self.colores:
                if nuevo_color != color_actual:
                    nuevo_estado = list(estado)
                    nuevo_estado[i] = nuevo_color
                    vecinos.append(tuple(nuevo_estado))
        return vecinos

    def valor(self, estado):
        
        conflictos = 0
        
        estado_dict = {self.departamentos[i]: estado[i] for i in range(len(self.departamentos))}
        
        for depto1, color1 in estado_dict.items():
            for depto2 in self.vecinos[depto1]:
                if color1 == estado_dict[depto2]:
                    conflictos += 1
        
        return -(conflictos // 2)

    def imprimir_estado(self, estado):
      
        print("\nColoreo de departamentos de Bolivia:")
        for i, depto in enumerate(self.departamentos):
            print(f" - {depto}: {estado[i]}")

def main():
    print("=== MAPA DE BOLIVIA (Coloreo) ===\n")
    problema = ProblemaColoreoBolivia()
    
    print("--- 1. Búsqueda con Hill Climbing ---")
    agente_hc = Agente(problema, hill_climbing)
    agente_hc.resolver()
    print("\n" + "="*50 + "\n")
    
    print("--- 2. Búsqueda con Simulated Annealing ---")
    agente_sa = Agente(problema, simulated_annealing)
    agente_sa.resolver()

if __name__ == "__main__":
    main()
