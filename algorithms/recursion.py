'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(valor):
    if valor == 0 :
        return 1
    elif valor == 1:
        return valor
    else:
        return valor*factorial(valor-1)

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(valor):
    if valor <= 1:
        return valor
    else:
        return fibonacci(valor-1) + fibonacci(valor-2)

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(valor):
    if valor ==0:
        return 0
    return valor + sum_of_numbers(valor-1)

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(numero, potencia):
    if potencia == 1:
        return numero
    elif potencia == 0:
        return 1  
    else:
        return numero * power(numero, potencia-1)


'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo_elemento = max_in_list(lista[1:])
        if lista[0] > maximo_elemento:
            return lista[0]
        else:
            return maximo_elemento