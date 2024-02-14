from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int, ini=0, fin=0):
    if fin==0: #Si es la primera vez que entra en la funcion
        fin=len(arr)

    size = fin-ini

    if size==0: #Si esta vacia
        return -1
    elif size ==1: #Si solo hay un elemento
        if arr[0]==target:
            return 0
        else:
            return -1
    else:
        mitad = size//2 + ini
        
        if arr[mitad]==target:
            return mitad
        elif arr[mitad]>target:
            return binary_search(arr, target, ini, mitad)
        else:
            return binary_search(arr, target, mitad, fin)


'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    rows=len(matrix)
    if rows==0: #Si esta vacia
        return False
    
    mid_rows= rows//2
    if rows==1: 
        if len(matrix[0])==0: #Si solo hay una fila y está vacia
            return False
        else: #Si solo hay una fila, y no esta vacia entonces llamanos a la busqueda binaria simple
            if binary_search(matrix[mid_rows], target)==-1: 
                return False
            else:
                return True
    else:
        
        print(mid_rows)
        columns = len(matrix[mid_rows])-1
        if matrix[mid_rows][0]>target: #Si el primer elemento de la fila del medio es mayor
            return binary_search_matrix(matrix[:mid_rows], target) #Vuelve a la funcion solo con las filas hasta la mitad
        
        elif matrix[mid_rows][columns]<target: #Si el ultimo elemento de la fila del medio es menor
            return binary_search_matrix(matrix[mid_rows:], target)#Vuelve a la funcion solo con las filas despues de la mitad
        
        else: #De lo contrario significa que el numero esta en esa fila por lo que llamanos a la busqueda binaria simple
            if binary_search(matrix[mid_rows], target)==-1: 
                return False
            else:
                return True


'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root==None:
        return False
    elif target==root.val:
        return True
    elif root.val<target:
        return binary_search_tree(root.right, target)
    elif root.val>target:
        return binary_search_tree(root.left, target)
