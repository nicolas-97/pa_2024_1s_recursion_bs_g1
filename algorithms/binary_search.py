from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    izquierda, derecha = 0, len(arr) - 1

    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2

        if arr[mitad] == target:
            return mitad
        elif arr[mitad] < target:
            izquierda = mitad + 1
        else:
            derecha = mitad - 1
    
    return -1
# arr = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(arr, 5))
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    FILAS, COLUMNAS = len(matrix), len(matrix[0])

    principio, final = 0, FILAS -1
    while principio <= final:
        fila = (principio + final) // 2
        if target > matrix[fila][-1]:
            principio = fila + 1
        elif target < matrix[fila][0]:
            final = fila -1
        else:
            break 
    
    if not (principio <= final):
        return False
    fila = (principio + final) // 2
    izquierda, derecha = 0, COLUMNAS -1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        if target > matrix[fila][mitad]:
            izquierda = mitad + 1
        elif target < matrix[fila][mitad]:
            derecha = mitad -1
        else:
            return True
    return False

# matrix = [
#             [1, 3, 5],
#             [7, 9, 11],
#             [13, 15, 17]
#         ]
# print(binary_search_matrix(matrix, 5))
   

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int)-> bool:

    if root is None:
        return False
    elif root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
    
def test_binary_search_tree_present(self):
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(17)

    print(binary_search_tree(root, 5))