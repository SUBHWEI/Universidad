# Suma Recursiva de Dígitos

Este proyecto contiene un script en Python que calcula la suma de los dígitos de un número entero utilizando recursión.

## Descripción

El programa solicita al usuario que ingrese un número entero y calcula la suma de sus dígitos de manera recursiva. Por ejemplo, para el número 123, la suma sería 1 + 2 + 3 = 6.

## Archivos

- `Suma_Recur.py`: Script principal que implementa la función recursiva y la interfaz de usuario.

## Cómo ejecutar

1. Asegúrate de tener Python instalado en tu sistema (versión 3.x recomendada).
2. Ejecuta el script desde la línea de comandos:

   ```
   python Suma_Recur.py
   ```

3. Ingresa un número entero cuando se te solicite.
4. El programa mostrará la suma de los dígitos.

## Ejemplo

```
Digite un número entero: 12345
La suma de los dígitos de 12345 es: 15
```

## Funcionamiento

La función `numsSum(N)` utiliza recursión para sumar los dígitos:
- Caso base: Si N < 10, retorna N (único dígito).
- Caso recursivo: Suma el último dígito (N % 10) con la suma del resto de los dígitos (numsSum(N // 10)).
