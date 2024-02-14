from models.tree_node import TreeNode

'''
    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    low=0
    high=len(arr)
    if(len(arr)!=0):
        while(low<=high):
            mid=(low+high)//2
            
            if(mid==len(arr)):
                 return -1
            
            if(arr[mid]==target):
                    return mid
            else:
                    if(target<arr[mid]):
                        high=mid-1
                    else:
                        low=mid+1
            
    return -1



 

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_matrix(matrix: list[list[int]], target: int):
    arr=[]
    fila=0
    while(fila<len(matrix)):
        columna=0
        while(columna<len(matrix)):
            arr.append(matrix[fila][columna])
            columna+=1
        fila+=1
    low=0
    high=len(arr)
    if(len(arr)!=0):
        while(low<=high):
            mid=(low+high)//2
            
            if(mid==len(arr)):
                 return False
            
            if(arr[mid]==target):
                    return True
            else:
                    if(target<arr[mid]):
                        high=mid-1
                    else:
                        low=mid+1
            
   
    return False

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False
