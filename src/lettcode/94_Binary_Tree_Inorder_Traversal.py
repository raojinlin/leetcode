# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        if not root:
            return result

        if root.left:
            result.extend(self.inorderTraversal(root.left))

        result.append(root.val)
        
        if root.right:
            result.extend(self.inorderTraversal(root.right))
        
        return result

        
if __name__ == '__main__':
    solution = Solution() 
    print(solution.inorderTraversal(TreeNode(1, left=None, right=TreeNode(2, left=TreeNode(3))) ))
    print(solution.inorderTraversal(TreeNode(1, left=TreeNode(2)) ))
    print(solution.inorderTraversal(TreeNode(1, right=TreeNode(2)) ))