from models.tree_node import TreeNode
import numpy as np
'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int, start=0, end=0):
    
    if len(arr)==0 or target not in arr:
        return -1
    if start == 0 and end == 0:
        end = len(arr)-1
    mitad = (start + end)//2
    #print(target,start,end)
    #print(mitad)
    if arr[mitad] == target:
        return mitad
    elif arr[mitad] > target:
        end= mitad-1
        return binary_search(arr,target,start,end)
    elif arr[mitad] < target:
        start= mitad+1
        return binary_search(arr,target,start,end)
    else:
        return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):

    longitud_matriz =len(matrix)
    fila =0
    if longitud_matriz == 0:
        return False
    for i in range(0, longitud_matriz):
        for j in range(0,len(matrix[fila])):
            if matrix[i][j]== target:
                return True
        fila +=1
        
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    if root is None:
        return False
    if target is None:
        return False
    if target == root.val:
        return True 
    if target > root.val:
        return binary_search_tree(root.right, target)
    if target < root.val:
        return binary_search_tree(root.left, target)
    
    return False
