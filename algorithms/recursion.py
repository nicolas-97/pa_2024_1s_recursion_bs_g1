# Función recursiva para calcular el factorial de un número entero positivo
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# Función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Función recursiva para calcular la suma de los primeros n números enteros
def sum_of_numbers(n):
    return n * (n + 1) // 2

# Función recursiva para calcular a^n (a elevado a la potencia n)
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_power = power(a, n // 2)
        return half_power * half_power
    else:
        return a * power(a, n - 1)

# Función recursiva para encontrar el máximo elemento en una lista de enteros
def max_in_list(lst):
    if len(lst) == 1:
        return lst [0]
    else:
        return max(lst[0],max_in_list(lst[1:]))
