import math


'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    high = len(arr)
    low = 0
    x = 0
  
    for x in range(len(arr)-1):
        mid = (high+low)//2
        print(mid)
        if arr[mid] == target:
            x += 1
            return mid
        elif arr[mid] > target:
            high = mid-1
        elif arr[mid] < target:
            low = mid+1
    return -1
        
arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 8))
'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    highlist = len(matrix)
    lowlist = 0
    
    low = 0
    for x in range(len(matrix)):
        midlist = math.floor((highlist+lowlist)/2)
        high = len(matrix[midlist-1])-1
        low = 0
        for j in range(len(matrix)):
            
            mid = math.floor((high+low)/2)
            if matrix[midlist-1][mid] == target: 
                return True
            elif matrix[midlist-1][mid] > target:
                high = mid-1
            elif matrix[midlist-1][mid] < target:
                low = mid+1
            if mid == 0:
                highlist = midlist - 1
                continue
            if mid == len(matrix[midlist-1])-1:
                lowlist = midlist +1
                continue

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
"""def binary_search_tree(root: TreeNode, target: int):
    return False"""

matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
print(binary_search_matrix(matrix, 17))