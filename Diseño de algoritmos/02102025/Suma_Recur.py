def numsSum(N):
    # Caso base de la recursión cuando N es menor que 10 (único dígito)
    if N < 10:
        return N
    else:
        return (N % 10) + numsSum(N // 10) # Suma el último dígito y llama recursivamente con el resto de los dígitos
# Solicitar al usuario que ingrese un número entero
num = int(input("Digite un número entero: "))
resultado = numsSum(num)
# Mostrar el resultado al usuario de manera clara
print(f"La suma de los dígitos de {num} es: {resultado}")