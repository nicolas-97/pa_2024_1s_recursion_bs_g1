'''
    Implementa una función recursiva para calcular el factorial de un número entero positivo
'''
def factorial(n):
    if (n==0 or n==1):
        return 1
    if (n==2):
        return 2
    if(n>2):
        n=n*factorial(n-1)
    return n

'''
    Implementa una función recursiva para calcular el término n-ésimo de la secuencia de Fibonacci.
'''
def fibonacci(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    if(n>1):
        n=fibonacci(n-2)+fibonacci(n-1)
    return n
    

'''
    Implementa una función recursiva para calcular la suma de los primeros n números enteros.
'''
def sum_of_numbers(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    if(n>1):
        n=n+sum_of_numbers(n-1)
    return n
     

'''
    Implementa una función recursiva para calcular a^n (a elevado a la potencia n).
'''
def power(a, n):
    if (n==0):
        return 1
    if (n==1):
        return a
    if (n>1):
        potencia=n-1
        c=a*power(a,potencia)
    return c

'''
    Implementa una función recursiva para encontrar el máximo elemento en una lista de enteros.
'''
def max_in_list(lst):
    if(len(lst)==1):
        return lst[0]

    if(lst[0]>lst[1]):
        mayor=lst[0]
        lst.remove(lst[1])
    elif(lst[1]>lst[0]):
        mayor=lst[1]
        lst.remove(lst[0])
    elif(lst[0]==lst[1]):
        mayor=lst[1]
        lst.remove(lst[0])
    if(len(lst)>1):
        mayor=max_in_list(lst)
    
    return mayor

