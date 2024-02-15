'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
       if n == 1 or n == 0:
           return n
       return n + sum_of_numbers(n-1)
    
'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    return a * power(a, n-1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if len(lst) == 1:
        return lst[0]
    if lst[0] > lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)
    return max_in_list(lst)