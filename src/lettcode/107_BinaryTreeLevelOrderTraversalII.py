"""
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root, level, result):
        if not root:
            return result

        if len(result) - 1 < level:
            result.insert(0, [])
        
        result[0].append(root.val)

        if root.left:
            self.helper(root.left, level + 1, result)
        
        if root.right:
            self.helper(root.right, level + 1, result)
        
        return result

    def levelOrderBottom(self, root):
        return self.helper(root, 0, [])


if __name__ == "__main__":
    solution = Solution() 
    print(solution.levelOrderBottom(TreeNode(3, left=TreeNode(9, left=TreeNode(8), right=TreeNode(11)), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))))
