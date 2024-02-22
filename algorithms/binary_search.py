from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix, target):

    if len(matrix)>0:
        fila_actual = 0
        col_actual = len(matrix[0]) - 1  

        while fila_actual < len(matrix) and col_actual >= 0:
            elemento_actual = matrix[fila_actual][col_actual]
            if elemento_actual == target:
                return True
            elif elemento_actual > target:
                col_actual -= 1
            else:
                fila_actual += 1

    return False
'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
class TreeNode:
    def init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_search_tree(root: TreeNode, target: int) -> bool:
    if not root:
        return False

    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
