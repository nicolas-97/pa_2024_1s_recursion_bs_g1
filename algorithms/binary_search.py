from models.tree_node import TreeNode

def binary_search(arr: list, target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Búsqueda binaria en una matriz ordenada
def binary_search_matrix(matrix: list[list[int]], target: int) -> bool:
    for row in matrix:
        if target in row:
            return True
    return False


# Búsqueda binaria en un árbol binario de búsqueda
def binary_search_tree(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    elif root.val == target:
        return True
    elif root.val < target:
        return binary_search_tree(root.right, target)
    else:
        return binary_search_tree(root.left, target)