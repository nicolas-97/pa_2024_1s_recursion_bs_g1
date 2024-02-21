from models.tree_node import TreeNode
'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1 

    return -1  

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    return False
def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  

    while row < rows and col >= 0:
        current_value = matrix[row][col]

        if current_value == target:
            return True  
        elif current_value < target:
            row += 1 
        else:
            col -= 1  
    return False 

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binary_search_tree(root: TreeNode, target: int) -> bool:
    if not root:
        return False  

    if root.value == target:
        return True  

    if target < root.value:
        return binary_search_tree(root.left, target)  
    else:
        return binary_search_tree(root.right, target) 

