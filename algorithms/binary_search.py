from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    low, high = 0, len(arr) - 1
    if  high >= low:
        mid = (high + low) // 2
        if  arr[mid] == target:
            return mid 
        elif arr[mid] > target:
            return binary_search(arr[:mid], target)
        else:
            return 1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    '''low = 0
    rows = len(matrix) # Filas de la matriz
    cols = len(matrix[0]) #Columnas de la matriz
    high = cols * rows - 1
    
    while low <= high:
        mid = (low + high) // 2
        '''
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False
