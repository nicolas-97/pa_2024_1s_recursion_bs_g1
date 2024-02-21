from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    index_izquierdo=0
    index_derecho=len(arr)-1

    while index_izquierdo <= index_derecho:
        punto_medio = (index_izquierdo+index_derecho)//2 #Encuentra el valor medio de la lista

        if arr[punto_medio]==target:
            return punto_medio
        elif arr[punto_medio]<target:
            #return binary_search(list,int,index_izquierdo,punto_medio-1)
            index_izquierdo= punto_medio + 1
        else:
            #return binary_search(list,int,punto_medio+1,index_derecho)
            index_derecho= punto_medio - 1
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if len(matrix)>0:
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
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if not root:
        return False
    
    if root.val == target:
        return True
    
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
    return False
