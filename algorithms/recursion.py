'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n>1:
        return n*factorial(n-1)
    else:
        return 1
    

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n==0:
        return 0
    if n>1:
        return fibonacci(n-2) + fibonacci(n-1)
    else:
        return 1

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n>1:
        return n+sum_of_numbers(n-1)
    else:
        return n

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        return a*power(a, n-1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    length=len(lst)
    if length==0:
        return 0
    elif length==1:
        return lst[0]
    else:
        if max_in_list(lst[length-1])>max_in_list(lst[length-2]):
            return lst[length-1]
        else:
            return lst[length-2]
        
print(max_in_list([1, 2, 3, 4, 5]))