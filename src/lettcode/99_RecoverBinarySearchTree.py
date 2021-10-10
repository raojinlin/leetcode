# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, min_node, max_node):
        if not root:
            return False
        
        if min_node and root.val < min_node.val:
            temp = root.val
            root.val = min_node.val
            min_node.val = temp
            return True
        
        if max_node and root.val > max_node.val:
            temp = root.val
            root.val = max_node.val
            max_node.val = temp
            return True
        
        return self.helper(root.left, min_node, root) or self.helper(root.right, root, max_node)

    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        continueRecovery = True
        while continueRecovery:
            continueRecovery = self.helper(root, None, None) 
        
        