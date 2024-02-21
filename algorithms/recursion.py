'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):    
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
   

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
   if n <2:
     return n
   return fibonacci(n-1) + fibonacci(n-2)


'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    while n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)
     



'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
      return a * power(a, n - 1)

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    while len(lst) == 1:
        return lst[0]
    else:
        max_sb = max_in_list(lst[1:])
        return lst[0] if lst[0] > max_sb else max_sb
    return list 