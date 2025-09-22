# 🗼 Torre de Hanoi

Una implementación completa del clásico juego de la **Torre de Hanoi** en Python, con modos de juego automático e interactivo.

## 📋 Descripción

El juego de la Torre de Hanoi es un rompecabezas matemático que consiste en mover una pila de discos de diferentes tamaños de una torre a otra, siguiendo estas reglas:
- Solo se puede mover un disco a la vez
- Nunca se puede colocar un disco más grande sobre uno más pequeño
- Se utilizan tres torres para el movimiento

Esta implementación incluye:
- ✅ Resolución automática usando algoritmo iterativo
- ✅ Modo de juego manual interactivo
- ✅ Algoritmo de ordenamiento Bubble Sort integrado
- ✅ Validación de movimientos
- ✅ Interfaz de consola intuitiva

## 🚀 Características

### 🎮 Modos de Juego
- **Resolución Automática**: El programa resuelve el puzzle automáticamente mostrando cada paso
- **Juego Manual**: Juega tú mismo moviendo los discos paso a paso

### 🛠️ Funcionalidades Técnicas
- Implementación iterativa (sin recursividad)
- Algoritmo Bubble Sort para verificación de victoria
- Validación de movimientos según las reglas del juego
- Contador de movimientos
- Verificación automática de victoria

### 📊 Información del Juego
- Soporte para 1-8 discos
- Cálculo de movimientos óptimos (2^n - 1)
- Visualización del estado de las torres en tiempo real

## 📦 Requisitos

- Python 3.x
- No requiere dependencias externas

## 🎯 Instalación y Uso

### 1. Clonar o descargar el proyecto
```bash
# Si tienes git instalado
git clone [url-del-repositorio]
cd torre-hanoi

# O simplemente descarga el archivo torre_hanoi.py
```

### 2. Ejecutar el programa
```bash
python torre_hanoi.py
```

## 🎲 Cómo Jugar

### Modo Automático
1. Ejecuta el programa
2. Ingresa el número de discos (recomendado: 3-5)
3. Selecciona la opción 1 (Resolver automáticamente)
4. Observa cómo se resuelve el puzzle paso a paso

### Modo Manual
1. Ejecuta el programa
2. Ingresa el número de discos
3. Selecciona la opción 2 (Jugar manualmente)
4. Ingresa movimientos en formato `A-B` (origen-destino)
5. Gana cuando todos los discos estén en la torre C ordenados

### Formato de Movimientos
```
A-B  (mueve disco de torre A a torre B)
B-C  (mueve disco de torre B a torre C)
C-A  (mueve disco de torre C a torre A)
```

## 📖 Ejemplo de Uso

```bash
=== TORRE DE HANOI ===
Número de discos (3-5 recomendado): 3

1. Resolver automáticamente
2. Jugar manualmente
Elige (1 o 2): 1

Resolviendo 3 discos...
A: [3, 2, 1]
B: []
C: []
Movimientos: 0
--------------------
A: [3, 2]
B: []
C: [1]
Movimientos: 1
--------------------
A: [3]
B: [2]
C: [1]
Movimientos: 2
--------------------
A: [3]
B: [2, 1]
C: []
Movimientos: 3
--------------------
A: []
B: [2, 1]
C: [3]
Movimientos: 4
--------------------
A: [1]
B: [2]
C: [3]
Movimientos: 5
--------------------
A: [1]
B: []
C: [3, 2]
Movimientos: 6
--------------------
A: []
B: []
C: [3, 2, 1]
Movimientos: 7

¡COMPLETADO! Movimientos: 7
Óptimo: 7
```

## 🏗️ Estructura del Código

### Clase `TorreHanoi`
- `__init__(discos)`: Inicializa el juego
- `bubble_sort(lista)`: Ordena lista usando Bubble Sort
- `mostrar_torres()`: Muestra estado actual del juego
- `es_movimiento_valido()`: Valida si un movimiento es legal
- `mover_disco()`: Ejecuta el movimiento de un disco
- `resolver()`: Resuelve automáticamente usando algoritmo iterativo
- `verificar_victoria()`: Verifica si el juego está completo
- `jugar_manual()`: Maneja el modo de juego interactivo

### Función `main()`
- Maneja la interfaz principal del programa
- Gestiona la entrada del usuario
- Controla el flujo del juego

## 🧮 Información Técnica

### Algoritmo de Resolución
- **Método**: Iterativo (usa pila para simular recursividad)
- **Complejidad**: O(2^n) donde n es el número de discos
- **Movimientos óptimos**: 2^n - 1

### Algoritmo Bubble Sort
- Implementado para verificar orden de discos
- Complejidad: O(n²) en peor caso
- Usado en la verificación de victoria

## 🎯 Consejos para Jugar

1. **Principiantes**: Empieza con 3 discos para entender las reglas
2. **Intermedio**: Prueba con 4-5 discos para mayor desafío
3. **Experto**: Intenta resolver 6-8 discos manualmente
4. **Recuerda**: Siempre mueve el disco más pequeño disponible primero

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Puedes:
- Reportar bugs
- Sugerir mejoras
- Agregar nuevas funcionalidades
- Mejorar la documentación

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT.

## 👨‍💻 Autor

**Julian Andres Correa**
- Estudiante de Diseño de Algoritmos
- Especializado en implementación de algoritmos clásicos

---

*¡Diviértete resolviendo el puzzle de la Torre de Hanoi! 🗼✨*
