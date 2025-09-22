# JUEGO DE LA TORRE DE HANOI
# Implementación iterativa sin recursividad
# Incluye algoritmo de ordenamiento Bubble Sort

class TorreHanoi:
    """Clase principal del juego de la Torre de Hanoi"""

    def __init__(self, discos):
        """Inicializa el juego con el número de discos especificado"""
        # Crear las tres torres como listas
        self.torre_A = []  # Torre inicial
        self.torre_B = []  # Torre auxiliar
        self.torre_C = []  # Torre final

        # Colocar discos en torre A (del más grande al más pequeño)
        for i in range(discos, 0, -1):
            self.torre_A.append(i)

        # Variables de control
        self.discos = discos
        self.movimientos = 0

    def bubble_sort(self, lista):
        """Algoritmo de ordenamiento Bubble Sort"""
        # Copiar lista para no modificar la original
        ordenada = lista.copy()
        n = len(ordenada)

        # Recorrer todos los elementos
        for i in range(n):
            # Los últimos i elementos ya están ordenados
            for j in range(0, n - i - 1):
                # Si el elemento actual es mayor que el siguiente, intercambiar
                if ordenada[j] > ordenada[j + 1]:
                    ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

        return ordenada

    def mostrar_torres(self):
        """Muestra el estado actual de las torres"""
        print(f"A: {self.torre_A}")
        print(f"B: {self.torre_B}")
        print(f"C: {self.torre_C}")
        print(f"Movimientos: {self.movimientos}")
        print("-" * 20)

    def es_movimiento_valido(self, origen, destino):
        """Verifica si un movimiento es válido"""
        # No se puede mover si la torre origen está vacía
        if not origen:
            return False

        # Se puede mover si la torre destino está vacía
        # o si el disco superior de destino es mayor que el de origen
        if not destino or destino[-1] > origen[-1]:
            return True

        return False

    def mover_disco(self, origen, destino):
        """Realiza el movimiento de un disco entre torres"""
        # Verificar si el movimiento es válido
        if not self.es_movimiento_valido(origen, destino):
            return False

        # Mover el disco
        disco = origen.pop()
        destino.append(disco)
        self.movimientos += 1
        return True

    def resolver(self):
        """Resuelve el problema de forma iterativa"""
        # Calcular movimientos necesarios (2^n - 1)
        total_movimientos = (2 ** self.discos) - 1

        # Usar una pila para simular recursividad
        pila = []
        pila.append((self.discos, 'A', 'C', 'B'))  # (discos, origen, destino, auxiliar)

        # Procesar hasta completar o llegar al límite
        while pila and self.movimientos < total_movimientos:
            # Obtener el estado actual
            n, origen, destino, auxiliar = pila.pop()

            if n == 1:
                # Mover disco individual
                if origen == 'A' and destino == 'C':
                    self.mover_disco(self.torre_A, self.torre_C)
                elif origen == 'A' and destino == 'B':
                    self.mover_disco(self.torre_A, self.torre_B)
                elif origen == 'B' and destino == 'C':
                    self.mover_disco(self.torre_B, self.torre_C)
                elif origen == 'B' and destino == 'A':
                    self.mover_disco(self.torre_B, self.torre_A)
                elif origen == 'C' and destino == 'A':
                    self.mover_disco(self.torre_C, self.torre_A)
                elif origen == 'C' and destino == 'B':
                    self.mover_disco(self.torre_C, self.torre_B)

                self.mostrar_torres()
            else:
                # Agregar subproblemas a la pila (orden inverso)
                pila.append((n-1, auxiliar, destino, origen))  # Mover n-1 del auxiliar al destino
                pila.append((1, origen, destino, auxiliar))    # Mover disco n del origen al destino
                pila.append((n-1, origen, auxiliar, destino))  # Mover n-1 del origen al auxiliar

    def verificar_victoria(self):
        """Verifica si el juego está completo"""
        # La torre C debe tener todos los discos ordenados
        if len(self.torre_C) != self.discos:
            return False

        # Verificar orden usando bubble sort
        orden_esperado = list(range(1, self.discos + 1))
        return self.bubble_sort(self.torre_C) == orden_esperado

    def jugar_manual(self):
        """Modo de juego manual"""
        print("TORRE DE HANOI - MODO MANUAL")
        print("Reglas: Mueve un disco a la vez, nunca uno grande sobre uno pequeño")
        print("Formato: origen-destino (ej: A-B)")
        print()

        self.mostrar_torres()

        while not self.verificar_victoria():
            try:
                # Obtener movimiento del usuario
                mov = input("Movimiento: ").upper().strip()

                if len(mov) != 3 or mov[1] != '-':
                    print("Formato inválido. Usa A-B")
                    continue

                orig, dest = mov[0], mov[2]

                if orig not in 'ABC' or dest not in 'ABC' or orig == dest:
                    print("Torres inválidas. Usa A, B o C")
                    continue

                # Realizar movimiento según las torres
                if orig == 'A' and dest == 'B':
                    if self.mover_disco(self.torre_A, self.torre_B):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")
                elif orig == 'A' and dest == 'C':
                    if self.mover_disco(self.torre_A, self.torre_C):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")
                elif orig == 'B' and dest == 'A':
                    if self.mover_disco(self.torre_B, self.torre_A):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")
                elif orig == 'B' and dest == 'C':
                    if self.mover_disco(self.torre_B, self.torre_C):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")
                elif orig == 'C' and dest == 'A':
                    if self.mover_disco(self.torre_C, self.torre_A):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")
                elif orig == 'C' and dest == 'B':
                    if self.mover_disco(self.torre_C, self.torre_B):
                        self.mostrar_torres()
                    else:
                        print("Movimiento inválido")

            except KeyboardInterrupt:
                print("\nJuego interrumpido")
                break
            except:
                print("Error. Intenta de nuevo")

        if self.verificar_victoria():
            print(f"¡GANASTE! Completado en {self.movimientos} movimientos")
            print(f"Movimientos óptimos: {(2 ** self.discos) - 1}")


def main():
    """Función principal del programa"""
    print("=== TORRE DE HANOI ===")

    # Obtener número de discos
    try:
        discos = int(input("Número de discos (3-5 recomendado): "))
        if discos < 1 or discos > 8:
            print("Usa entre 1 y 8 discos")
            return
    except:
        print("Número inválido")
        return

    # Crear juego
    juego = TorreHanoi(discos)

    # Menú de opciones
    print("\n1. Resolver automáticamente")
    print("2. Jugar manualmente")

    try:
        opcion = input("Elige (1 o 2): ").strip()

        if opcion == "1":
            print(f"\nResolviendo {discos} discos...")
            juego.mostrar_torres()
            juego.resolver()

            if juego.verificar_victoria():
                print(f"\n¡COMPLETADO! Movimientos: {juego.movimientos}")
                print(f"Óptimo: {(2 ** discos) - 1}")
            else:
                print("Error en la resolución")

        elif opcion == "2":
            juego.jugar_manual()

        else:
            print("Opción inválida")

    except KeyboardInterrupt:
        print("\nPrograma terminado")
    except:
        print("Error inesperado")


# Ejecutar programa
if __name__ == "__main__":
    main()
