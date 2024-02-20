from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    #Manejo de excepciones  en caso de que el arreglo esté vacío o si no se cumple la condición del Binary Search
    izq = 0 #La parte izquierda del arreglo
    der = len(arr)-1 #La parte derecha del arreglo 
    while izq<= der:
        mid =(izq + der)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            izq = mid +1
        else:
            der = mid -1
    return -1


'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    if not matrix:
        return False
    filas = len(matrix)
    columnas = len(matrix[0])

    fila_actual = 0
    columna_actual = columnas-1
    while fila_actual < filas-1 and columna_actual >=0:
        if  matrix[fila_actual][columna_actual]==target:
            return True
        elif matrix[fila_actual][columna_actual] < target:
            fila_actual += 1
        else:
            columna_actual -= 1
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
        return  binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)
