from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    inferior = 0
    superior = len(arr)
    medio = (inferior+superior)//2
    while (inferior <= superior and medio != len(arr)):
        if (arr[medio]==target): #Verificar si target esta en 'medio'
            return medio
        elif (target<arr[medio]): #Verificar en que mitad se encuentra target
            superior = medio-1 #Se modifican extremos para volver a hacer la partición
        else:
            inferior = medio+1
            medio = (inferior+superior)//2 #Se vuelve a calcular el punto medio
    return -1 #Retornar en caso de no encontrar target

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    for fila in range(len(matrix)): #Se revisa cada fila en matrix 
        ubicacion = binary_search(matrix[fila], target) #Verificar si target esta dentro de alguna fila de matrix
        if ubicacion != -1:
            return True
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root == None: #Caso base
        return False 
    elif root.val == target: #Verificar si el valor actual es igual a target
        return True
    elif root.val > target: #Los arboles tiene a la derecha mayores e izquierda menores
        return binary_search_tree(root.left, target)
    else:
        return binary_search_tree(root.right, target)


