'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n == 0:
        return n
    return n + sum_of_numbers(n-1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n == 0:
        return 1
    return a * pow(a, n-1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if not lst:  # Si la lista está vacía, retorna None
        return None
    elif len(lst) == 1:  # Si la lista tiene un solo elemento, ese es el máximo
        return lst[0]
    else:
        max_anterior = max_in_list(lst[1:])  # para encontrar el máximo en el resto de la lista
        return lst[0] if lst[0] > max_anterior else max_anterior