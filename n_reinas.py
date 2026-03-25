import random

class ProblemaNReinas:
    def __init__(self, n=8):
        self.n = n

    def estado_inicial(self):
        return tuple(random.randint(0, self.n - 1) for _ in range(self.n))

    def obtener_vecinos(self, estado):
        vecinos = []
        for fila in range(self.n):
            for col in range(self.n):
                if estado[fila] != col:
                    vecino = list(estado)
                    vecino[fila] = col
                    vecinos.append(tuple(vecino))
        return vecinos

    def valor(self, estado):
        ataques = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if estado[i] == estado[j] or abs(estado[i] - estado[j]) == j - i:
                    ataques += 1
        return -ataques

    def imprimir_estado(self, estado):
        n = len(estado)
        print("-" * (n * 2 + 1))
        for fila in range(n):
            fila_str = "|"
            for col in range(n):
                if estado[fila] == col:
                    fila_str += "Q|"
                else:
                    fila_str += ".|"
            print(fila_str)
            print("-" * (n * 2 + 1))
