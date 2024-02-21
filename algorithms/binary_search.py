from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    arr.sort()
    if len(arr) == 0:
        return -1
    first = 0
    last = len(arr)-1
    while first <= last:
        center = (first+last) // 2


        if arr[center] == target:
            return center
        else:
            if target < arr[center]:
                last = center -1
            else:
                first = center+1


    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if len(matrix)==0:
        return False
   
    rows = len(matrix)
    columns = len(matrix[0])
    first = 0
    last = rows * columns
    while first < last :
        center = (first + last) // 2
        if matrix[center // columns] [center % columns] == target:
            return center
        elif matrix[center // columns][center % columns] < target:
            first = center + 1
        else:
            last = center

    return False
'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
   
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    elif root.val > target:
        return binary_search_tree(root.left, target)
