from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arreglo: list, target: int,inicio =0, final=0):
    if len(arreglo)==0 or target not in arreglo:
        return -1

    if inicio == 0 and final == 0:
        final =len(arreglo)-1

    mitad =(inicio + final)//2

    if arreglo[mitad] == target:
        return mitad
    elif arreglo[mitad] > target:
        final =mitad -1
        return binary_search(arreglo,target,inicio,final)
    elif arreglo[mitad] < target:
        inicio =mitad +1
        return binary_search(arreglo,target,inicio,final)

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int, fila=0):
    try:
        if target in matrix[fila]:
            return True
    except IndexError:
        return False
    fila += 1
    if fila >= len(matrix):
        return False
    return binary_search_matrix(matrix, target, fila)

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elemento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False

    if target < root.val:
        if root.left is None:
            return False
        else:
            return binary_search_tree(root.left, target)
    elif target > root.val:
        if root.right is None:
            return False
        else: 
            return binary_search_tree(root.right, target)
    else:
        return True