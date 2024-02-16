from random import sample
import time
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):

    size = len(arr)

    if size==0:
        return -1

    if(size==1):
        if arr[0]==target:
            return
        else:
            return -1 

    mitad = (size-1)//2 
    reposicion=0

    if arr[mitad] == target:
        return mitad 
    elif arr[mitad]> target:
        nueva_list = arr[:mitad]
    else:
        nueva_list = arr[mitad+1:]
        reposicion=mitad+1

    return binary_search2part(nueva_list,target,reposicion)


def binary_search2part(arr, target,reposicion):

    size = len(arr)

    if(size==1):
        if arr[0]==target:
            return reposicion
        else:
            return -1 

    mitad = (size-1)//2 
    

    if arr[mitad] == target:
        return mitad+ reposicion
    elif arr[mitad]> target:
        nueva_list = arr[:mitad]
    else:
        nueva_list = arr[mitad+1:]
        reposicion=reposicion+mitad+1

    return binary_search2part(nueva_list,target,reposicion)


'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):

    for i in range(len(matrix)):
        numero=binary_search(matrix[i],target)
        if numero != -1:
            return True
    
    return False
    

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''


def binary_search_tree(root: TreeNode, target: int):

    if root == None:
        return False
    elif root.val == target:
        return True
    elif target < root.val:    
        return binary_search_tree(root.left,target)
    else:
        return binary_search_tree(root.right,target)

    
"""
arr = [1, 3, 5, 7, 9, 11, 13]

my_list = list(range(10000))

vector=sample(my_list,10000)
print(sorted(vector))

strat_time=time.time()
binary_search(sorted(vector),6)
end_time=time.time()

print("El tiempo de ejecucion del binary search es: ",end_time -strat_time)


matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]

print(binary_search_matrix(matrix,8))


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(17)

print(binary_search_tree(root,10))
"""