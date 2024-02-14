'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    
    if n==0:
        return n
    elif n==1:
        return 1
        return fibonacci(n-1) + fibonacci(n-2)
    
    return n

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    return n

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    return a + n

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    return lst

print(factorial(3))