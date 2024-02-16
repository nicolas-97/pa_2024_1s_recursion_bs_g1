'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if n == 0:
        return 1

    return n*(factorial(n-1))

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1

    return fibonacci2part(0,1,n-1)
    

def fibonacci2part(i,f,n):
    if n==0:
        return f
    
    i,f=f,f+i
    
    return fibonacci2part(i,f,n-1)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if n == 0:
        return 0

    return n + sum_of_numbers(n-1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):

    if n== 0:
        return 1
    if n== 1:
        return a

    return a * power(a,n-1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    size = len(lst)

    if size == 1:
        return lst[0]
    elif lst[0]>lst[1]:
        lst.pop(1)
    else:
        lst.pop(0)

    return max_in_list(lst)

