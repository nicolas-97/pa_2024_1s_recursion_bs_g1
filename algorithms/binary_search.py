from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    start = 0
    end = len(arr) - 1
    while (start <= end):
        k = (start + end)//2
        if target == arr[k]:
            return k
        elif target < arr[k]:
            end = k - 1
        elif target > arr[k]:
            start = k + 1
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    row_size = len(matrix)
    if row_size == 0:
        return False
    column_size = len(matrix[0])
    start = 0
    end = (row_size * column_size)-1
    k = (start + end)//2
    while (start <= end):
        row = k // row_size
        column = k % column_size
        if target == matrix[row][column]:
            return True
        elif target < matrix[row][column]:
            k -= 1
            end = k
        else:
            k += 1
            start = k
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root == None:
        return False
    left_exists = root.left != None
    right_exists = root.right != None
    if target < root.val:
        if left_exists:
            return binary_search_tree(root.left,target)
        else:
            return False
    elif target > root.val:
        if right_exists:
            return binary_search_tree(root.right,target)
        else:
            return False
    return True
