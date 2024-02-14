from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int, ini=0, fin=0):
    if fin==0:
        fin=len(arr)

    size = fin-ini
    if size <=1:
        if arr[0]==target:
            return 0
        else:
            return -1
    else:
        mitad = size//2 + ini
        if arr[mitad]==target:
            return mitad
        elif arr[mitad]>target:
            return binary_search(arr, target, ini, mitad)
        else:
            return binary_search(arr, target, mitad, fin)


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
