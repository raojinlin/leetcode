import unittest
from lettcode.rangeSumOfBFS import Solution, TreeNode


class rangeSumOfBFS(unittest.TestCase):
    def test_sum(self):
        s = Solution()
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)

        self.assertEqual(32, s.rangeSumBST(root, 7, 15))
        self.assertEqual(32, s.sum(root, 7, 15))

    def test_sum2(self):
        s = Solution()
        root = TreeNode(10, TreeNode(5), TreeNode(15))
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)

        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        self.assertEqual(23, s.rangeSumBST(root, 6, 10))
        self.assertEqual(23, s.sum(root, 6, 10))
