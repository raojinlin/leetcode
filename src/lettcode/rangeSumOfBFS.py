"""
938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example 1:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32


Example 2:
    Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
    Output: 23

Constraints:

    The number of nodes in the tree is in the range [1, 2 * 104].
    1 <= Node.val <= 105
    1 <= low <= high <= 105
    All Node.val are unique.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        """
        :param val:
        :type left TreeNode
        :type right  TreeNode
        """
        self.val = val
        self.left = left
        self.right = right
        self.parent = None

    def __str__(self):
        left = 0
        if self.left is not None:
            left = self.left.val
        right = 0
        if self.right is not None:
            right = self.right.val

        parent = 0
        if self.parent is not None:
            parent = self.parent.val

        return 'TreeNode(val=%d, left=%d, right=%d, parent=%d)' % (self.val, left, right, parent)


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        pass

