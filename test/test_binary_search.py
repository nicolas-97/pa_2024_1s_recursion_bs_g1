import unittest
from algorithms.binary_search import binary_search, binary_search_matrix
"""from models.tree_node import TreeNode"""

class TestBinarySearch(unittest.TestCase):

    def test_binary_search_present(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(binary_search(arr, 5), 2)
        self.assertEqual(binary_search(arr, 9), 4)
        self.assertEqual(binary_search(arr, 13), 6)

    def test_binary_search_not_present(self):
        arr = [1, 3, 5, 7, 9, 11, 13]
        self.assertEqual(binary_search(arr, 0), -1)
        self.assertEqual(binary_search(arr, 6), -1)
        self.assertEqual(binary_search(arr, 15), -1)

    def test_binary_search_empty(self):
        arr = []
        self.assertEqual(binary_search(arr, 5), -1)

    def test_binary_search_matrix_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertTrue(binary_search_matrix(matrix, 5))
        self.assertTrue(binary_search_matrix(matrix, 9))
        self.assertTrue(binary_search_matrix(matrix, 17))

    def test_binary_search_matrix_not_present(self):
        matrix = [
            [1, 3, 5],
            [7, 9, 11],
            [13, 15, 17]
        ]
        self.assertFalse(binary_search_matrix(matrix, 0))
        self.assertFalse(binary_search_matrix(matrix, 6))
        self.assertFalse(binary_search_matrix(matrix, 20))

    def test_binary_search_matrix_empty(self):
        matrix = []
        self.assertFalse(binary_search_matrix(matrix, 5))

    """def test_binary_search_tree_present(self):
        # Construir un árbol de búsqueda binaria para probar
        #        10
        #       /  \
        #      5    15
        #     / \   / \
        #    3   7 12 17
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(17)

        self.assertTrue(binary_search_tree(root, 5))
        self.assertTrue(binary_search_tree(root, 15))
        self.assertTrue(binary_search_tree(root, 3))
        self.assertTrue(binary_search_tree(root, 17))

    def test_binary_search_tree_not_present(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)

        self.assertFalse(binary_search_tree(root, 7))
        self.assertFalse(binary_search_tree(root, 20))
        self.assertFalse(binary_search_tree(None, 5))"""

if __name__ == '__main__':
    unittest.main()