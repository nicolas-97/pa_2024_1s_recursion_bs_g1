from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    if not arr:
        return -1
    
    Inicio =0
    Final =len(arr)-1
    while Inicio<=Final:
        Mitad=(Inicio+Final)//2
        if arr[Mitad] ==target:
            return Mitad
        elif arr[Mitad]< target:
            Inicio = Mitad +1
        else :
            Final =Mitad-1
    return -1    

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    Filas =len(matrix)
    if Filas ==0:
        return False
    Columna=len(matrix[0])
    if Columna ==0:
        return False
    for Fila in matrix :
        left,right =0,Columna-1
        while left <=right:
            Mitad =(left+right)//2
            if Fila[Mitad] == target:
                return True
            elif Fila[Mitad] <target:
                left= Mitad+1
            elif Fila[Mitad] > target:
                right =Mitad -1
            else :
                return False
            

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
class TreeNode:
    def __init__(self,valor):
        self.valor =valor
        self.left = None
        self.right = None
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    elif root.val ==target :
        return True
    elif root.val < target :
        return binary_search_tree(root.right,target)
    elif root.val >target :
        return binary_search_tree(root.left,target)
