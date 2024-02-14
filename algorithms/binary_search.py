from models.tree_node import TreeNode

def binary_search(arr: list, target: int) -> int:
    bajo, altura = 0, len(arr) - 1
    while bajo <= altura:
        division = (bajo + altura) // 2
        if arr[division] == target:
            return division
        elif arr[division] < target:
            bajo = division + 1
        else:
            altura = division - 1
    return -1

# Búsqueda binaria en una matriz ordenada
def binary_search_matrix(matrix: list[list[int]], target: int) -> bool:
    for fila in matrix:
        if target in fila:
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

