from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    minimum, maximum = 0, len(arr) - 1
    while minimum <= maximum:
        middle = (maximum + minimum) // 2
        if arr[middle] < target:
            minimum = middle + 1
        elif arr[middle] > target:
            maximum = middle - 1
        else:
            return middle
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix or not matrix[0]:
        return False
    rows, columns = len(matrix), len(matrix[0])
    minimum, maximum = 0, rows * columns - 1
    while minimum <= maximum:
        middle = minimum + (maximum - minimum) // 2
        middle_value = matrix[middle // columns][middle % columns]
        if middle_value == target:
            return middle // columns, middle % columns
        elif middle_value < target:
            minimum = middle + 1
        else:
            maximum = middle - 1
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    
    if root.val == target:
        return True
    elif target < root.val:
        return binary_search_tree(root.left, target)
    else:
        return binary_search_tree(root.right, target)
