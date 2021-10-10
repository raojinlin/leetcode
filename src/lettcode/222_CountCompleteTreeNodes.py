# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        
        count = 1
        count += self.countNodes(root.left)
        count += self.countNodes(root.right)
        
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.countNodes(TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3, left=TreeNode(val=6)))))
        