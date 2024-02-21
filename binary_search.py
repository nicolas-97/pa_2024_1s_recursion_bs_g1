    Implementa una función de búsqueda binaria que encuentre un elemento en una lista ordenada de enteros y retorne su posicion si no lo encuntra que retorne -1
'''
def binary_search(arr: list, target: int):
    return 1
    minimum, maximum = 0, len(arr) - 1
    while minimum <= maximum:
        middle = (maximum + minimum) // 2
        if arr[middle] < target:
            minimum = middle + 1
        elif arr[middle] > target:
            maximum = middle - 1
        else:
            return middle
    return -1

'''
    Implementa una función de búsqueda binaria para encontrar un elemento en una matriz ordenada (fila y columna) de enteros y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  
        elif mid_value < target:
            low = mid + 1  
        else:
            high = mid - 1 

    return -1  

'''
    Implementa una función de búsqueda binaria en un árbol binario de búsqueda  y retorne verdadero si la encuntra el elmento o falso si no lo encuentra
'''
def binary_search_tree(root: TreeNode, target: int):
    return False
    if root is None:
        return False

    if root.val == target:
        return True
    elif target < root.val:
        return binary_search_tree(root.left, target)
    else:
        return binary_search_tree(root.right, targe)
