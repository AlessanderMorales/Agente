class Agente:
    def __init__(self, problema, algoritmo_busqueda):
        self.problema = problema
        self.algoritmo_busqueda = algoritmo_busqueda
        
    def resolver(self, verbose=True, **kwargs):
        
        estado_final = self.algoritmo_busqueda(self.problema, **kwargs)
        costo = -self.problema.valor(estado_final)
        
        if verbose:
            print(f"Estado final encontrado: {estado_final}")
            print(f"Costo / Conflictos del estado: {costo}")
            if costo == 0:
                print("¡Solución óptima encontrada!")
            else:
                print("Se llegó a un máximo/mínimo local (Solución no óptima).")
                
            if hasattr(self.problema, 'imprimir_estado'):
                self.problema.imprimir_estado(estado_final)
            
        return estado_final
