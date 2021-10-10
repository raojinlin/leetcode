"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

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
            result.append([])
        
        if level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)

        children = []
        if root.left:
            children.append(root.left)
        
        if root.right:
            children.append(root.right)

        for child in children:
            self.helper(child, level + 1, result)

        return result


    def zigzagLevelOrder(self, root):
        return self.helper(root, 0, [])


if __name__ == "__main__":
    solution = Solution() 
    print(solution.zigzagLevelOrder(TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))))
    print(solution.zigzagLevelOrder(TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3, left=TreeNode(5)))))
