from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y 
    retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    def aux_binary_search(arr, target, inicio, fin):
        if inicio <= fin:
            puntero = (inicio + fin)//2

            if arr[puntero]==target:
                return puntero
            elif target < arr[puntero]:
                return aux_binary_search(arr,target,inicio,puntero-1)
            else:
                return aux_binary_search(arr,target,puntero +1 ,fin)
        else:
            return -1
        
    return aux_binary_search(arr,target,0,len(arr)-1)

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de 
    enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix, target):
    # Inicializar índices para recorrer la matriz
    fila_actual = 0
    col_actual = len(matrix[0]) - 1  # Empezar desde la última columna

    while fila_actual < len(matrix) and col_actual >= 0:
        # Elemento actual en la matriz
        elemento_actual = matrix[fila_actual][col_actual]

        if elemento_actual == target:
            return True
        elif elemento_actual > target:
            # Si el elemento actual es mayor, movemos a la fila anterior
            col_actual -= 1
        else:
            # Si el elemento actual es menor, movemos a la siguiente fila
            fila_actual += 1

    # Si no se encuentra el elemento en la matriz
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra 
    el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if not root:
       return False
    if root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left ,target)