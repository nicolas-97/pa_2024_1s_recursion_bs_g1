from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    l, h=0, len(arr)-1
    while l <= h:
        mitad=(h+l)//2
        if arr[mitad]==target:
            return mitad
        elif arr[mitad]<target:
            l=mitad+1
        else:
            h=mitad-1
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    for row in matrix:
        if target in row:
            return True
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    elif root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)

