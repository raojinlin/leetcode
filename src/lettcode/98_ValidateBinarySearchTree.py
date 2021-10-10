"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
  o. The left subtree of a node contains only nodes with keys less than the node's key.
  o. The right subtree of a node contains only nodes with keys greater than the node's key.
  o. Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid(self, root, min_val, max_val):
        if not root:
            return True
        
        if (max_val != None and root.val >= max_val) or (min_val != None and root.val <= min_val):
            return False
        
        return self.is_valid(root.left, min_val, root.val) and self.is_valid(root.right, root.val, max_val)

    def isValidBST(self, root) -> bool:
       return self.is_valid(root, None, None)

        
if __name__ == "__main__":
    solution = Solution() 
    print(solution.isValidBST(TreeNode(2, left=TreeNode(1), right=TreeNode(3))))
    print(solution.isValidBST(TreeNode(5, left=TreeNode(1), right=TreeNode(4))))
    print(solution.isValidBST(TreeNode(0)))
    print(solution.isValidBST(TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))))