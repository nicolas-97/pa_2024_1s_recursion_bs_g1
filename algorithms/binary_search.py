# No me sirvio el import del modulo :(
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    min,max = 0, len(arr) - 1
    # El ciclo acaba cuando la lista contiene 1 solo elemento: el target
    while min <= max:
        # Cada vuelta del ciclo actualiza la mitad del arreglo
        mid = (max + min) // 2
        # Sí el target es más grande que la mitad del arreglo, 
        # se modifica el minimo del arreglo a la mitad actual
        if arr[mid] < target:
            min = mid + 1
        # Sí el target es mas pequeño que la mitad del arreglo, 
        # se modifica el maximo del arreglo a la mitad actual
        elif arr[mid] > target:
            max = mid - 1
        # El target esta en "mid", por lo que devuelve la posición
        else:
            return mid
    # Retorna -1 si el valor no se encuentra en la lista 
    return -1
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    # Verificar que la matris no tenga una lista vacia o que no este en formato matris
    if not matrix or not matrix[0]:
        return False
    # Obtiene el número de filas y columnas de la matriz
    filas, columnas = len(matrix), len(matrix[0])
    # Inicializa los índices minimos y maximos
    min, max = 0, filas * columnas - 1
    # El ciclo acaba cuando la lista contiene 1 solo elemento: el target
    while min <= max:
        # Calcula el índice medio de la matriz
        mid = min + (max - min) // 2
        # Obtiene el valor en la posición correspondiente al índice medio
        mid_val = matrix[mid // columnas][mid % columnas]
        # Comprueba si el valor en el índice medio es igual al objetivo
        if mid_val == target:
            return mid // columnas, mid % columnas
        # Si el valor en el índice medio es menor que el objetivo, ajusta el índice izquierdo
        elif mid_val < target:
            min = mid + 1
        # Si el valor en el índice medio es mayor que el objetivo, ajusta el índice derecho
        else:
            max = mid - 1
    return False
'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    # Evalua que sea un arbol 
    if not root:
        return False
    # Si encuentra el valor, devuelve True
    if root.val == target:
        return True
    # Si el valor es menor que el objetivo, accede a el hijo del nodo derecho 
    elif root.val < target:
        return binary_search_tree(root.right, target) 
    # Si el valor es mayor que el objetivo, accede a el hijo del nodo izquierdo
    else:
        return binary_search_tree(root.left, target)