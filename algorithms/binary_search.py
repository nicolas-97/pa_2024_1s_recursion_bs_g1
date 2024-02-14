from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int, start=0, end=0):
    if start == 0 and end == 0:
        end = len(arr)
    
    mitad_arreglo = (start + end) // 2

    verificador=arr[promedioarr]

    if verificador==target:
        return 1
    elif target>verificador:
    
        if verificador==target: 
            return 1
        else: 
            binary_search ()
    else: 
        if  verificador==target: 
            return 1
        else: 
            binary_search()

    
    return 1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False
