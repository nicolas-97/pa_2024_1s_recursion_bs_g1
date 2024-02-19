from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int,star =0, end=0):
    if len(arr)==0 or target not in arr:
        return -1

    if star == 0 and end == 0:
        end =len(arr)-1

    mitad =(star + end)//2

    if arr[mitad] == target:
        return mitad
    elif arr[mitad] > target:
        end =mitad -1
        return binary_search(arr,target,star,end)
    elif arr[mitad] < target:
        star =mitad +1
        return binary_search(arr,target,star,end)

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int, Fila=0):
    try:
        if target in matrix[Fila]:
            return True
    except IndexError:
        return False
    Fila += 1
    if Fila >= len(matrix):
        return False
    return binary_search_matrix(matrix, target, Fila)

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
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