class TorreHanoi:
    def __init__(self, discos):
        self.torre_A = []  # Torre inicial
        self.torre_B = []  # Torre auxiliar
        self.torre_C = []  # Torre final
        for i in range(discos, 0, -1):
            self.torre_A.append(i)
        self.discos = discos
        self.movimientos = 0
    def mostrar_torres(self):
        print(f"A: {self.torre_A}")
        print(f"B: {self.torre_B}")
        print(f"C: {self.torre_C}")
        print(f"Movimientos: {self.movimientos}")
        print("-" * 20)
    def es_movimiento_valido(self, origen, destino):
        if not origen:
            return False
        if not destino or destino[-1] > origen[-1]:
            return True
        return False
    def mover_disco(self, origen, destino):
        if not self.es_movimiento_valido(origen, destino):
            return False
        disco = origen.pop()
        destino.append(disco)
        self.movimientos += 1
        return True
    def get_torre(self, nombre):
        if nombre == 'A':
            return self.torre_A
        elif nombre == 'B':
            return self.torre_B
        elif nombre == 'C':
            return self.torre_C
    def resolver_recursivo(self, n, from_rod, to_rod, aux_rod):
        if n == 1:
            self.mover_disco(self.get_torre(from_rod), self.get_torre(to_rod))
            self.mostrar_torres()
            return
        self.resolver_recursivo(n-1, from_rod, aux_rod, to_rod)
        self.mover_disco(self.get_torre(from_rod), self.get_torre(to_rod))
        self.mostrar_torres()
        self.resolver_recursivo(n-1, aux_rod, to_rod, from_rod)
    def resolver(self):
        self.resolver_recursivo(self.discos, 'A', 'C', 'B')
    def verificar_victoria(self):
        return len(self.torre_C) == self.discos and self.torre_C == list(range(1, self.discos + 1))
def main():
    print("=== TORRE DE HANOI ===")
    try:
        discos = int(input("Número de discos (3-5 recomendado): "))
        if discos < 1 or discos > 8:
            print("Usa entre 1 y 8 discos")
            return
    except:
        print("Número inválido")
        return
    juego = TorreHanoi(discos)
    print(f"\nResolviendo {discos} discos...")
    juego.mostrar_torres()
    juego.resolver()
    if juego.verificar_victoria():
        print(f"\n¡COMPLETADO! Movimientos: {juego.movimientos}")
        print(f"Óptimo: {(2 ** discos) - 1}")
    else:
        print("Error en la resolución")
if __name__ == "__main__":
    main()