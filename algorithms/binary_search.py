from models.tree_node import TreeNode #no se envia error "no esta definido TreeNode"

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int, start=-100, end=-100):

    if arr == []:
        return -1

    if start == -100 and end == -100:
        start = 0
        end = len(arr)
        
    mitad_arreglo = (start + end) // 2
    
    if mitad_arreglo == len(arr) or end < start:
        return -1
    if start == 0 and end < 0:
         return -1
        
    if arr[mitad_arreglo] == target:
        return mitad_arreglo
    elif arr[mitad_arreglo] > target:
        return binary_search(arr, target, start, mitad_arreglo - 1)
    elif arr[mitad_arreglo] < target:
        return binary_search(arr, target, mitad_arreglo + 1, end)
    
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):

    if matrix == []:
        return False
    
    response = False

    for i in matrix:
        find = binary_search(i, target)
        if find != -1:
            response = True

    #se utiliza la libreria numpy para concatenar
     #vector_uni= np.concatenate(matrix) 
     #binary_search(vector_uni)
    return response


'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
        
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    elif root.val ==target :
        return True
    elif root.val < target :
        return binary_search_tree(root.right,target)
    elif root.val >target :
        return binary_search_tree(root.left,target)