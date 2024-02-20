from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    if not arr:
        return -1
    mitad=(len(arr)-1)//2
    if arr[mitad]==target:
        return mitad
    
    elif arr[mitad] < target and mitad + 1 < len(arr):
        return mitad + 1 + binary_search(arr[mitad+1:], target)

    
    else:
        return binary_search(arr[:mitad], target)
    
    
        
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix:
        return False
    filas, columnas = len(matrix), len(matrix[0])
    inicio, final = 0, filas*columnas - 1

    mitad= inicio-final//2
        



'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    pass
