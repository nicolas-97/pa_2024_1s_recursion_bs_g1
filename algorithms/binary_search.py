from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    inicio=0
    fin=len(arr)-1
    k=(inicio+fin)//2
    while inicio<=fin:
        if arr[k]==target:
            return k
        elif target<arr[k]:
            fin=k-1
        else:
            inicio=k+1
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    inicio=0
    fin=len(matrix)-1
    medio=(inicio+fin)//2
    fila=medio//len(matrix[0])
    columna=medio%len(matrix[0])
    while inicio<=fin:
        if matrix[fila][columna]==target:
            return True
        elif target<matrix[fila][columna]:
            fin=medio-1
        else:
            inicio=medio+1
    return False

    
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if target==root.val:
        return True
    elif target<root:
        binary_search_tree(root.left,target)
    else:
        binary_search_tree(root.rigt,target)
    return False
