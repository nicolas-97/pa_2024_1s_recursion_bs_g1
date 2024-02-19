#Natalia Osejo Hincapie
'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0: #Caso base
        return 1 
    return n*factorial(n-1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n <= 1: #Caso base
        return n
    return fibonacci(n-1) + fibonacci(n-2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n == 0: #Caso base
        return n
    return n + sum_of_numbers(n-1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n): 
    if n == 0: #Caso base
        return 1
    return a * power(a, n-1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if len(lst) == 1: #Caso base
        return lst[0]
    max_anterior = max_in_list(lst[:-1]) 
    return max_anterior if max_anterior > lst[-1] else lst[-1] #Se compara el valor maximo anterior con lst[-1]