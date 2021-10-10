# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def helper(self, start, end):
        if start >= end or start == 0:
            return [None]

        trees = []
        for i in range(start, end + 1):
            left_trees = self.helper(start, i - 1)
            right_trees = self.helper(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    tree = TreeNode(i, left=left, right=right)
                    trees.append(tree)
        
        return trees


    def generateTrees(self, n: int):
        return self.helper(1, n)


if __name__ == "__main__":
    solution = Solution()
    for tree in solution.generateTrees(3):
        print(tree.val, tree.left)

        