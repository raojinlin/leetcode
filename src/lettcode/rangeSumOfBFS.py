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


S.NO	BFS	                                    DFS
1.	    BFS stands for Breadth First Search.	DFS stands for Depth First Search.
2.	    BFS(Breadth First Search) uses Queue    DFS(Depth First Search) uses Stack data structure.
        data structure for finding the shortest
        path.
3.	    BFS can be used to find single source   In DFS, we might traverse through more edges to reach a destination vertex from a source.
        shortest path in an unweighted graph,
        because in BFS, we reach a vertex
        with minimum number of edges from
        a source vertex.
3.	    BFS is more suitable for searching      DFS is more suitable when there are solutions away from source.
        vertices which are closer to the given
        source.
4.	    BFS considers all neighbors first        DFS is more suitable for game or puzzle problems. We make a decision, then explore all paths through this decision. And if this decision leads to win situation, we stop.
        and therefore not suitable for decision
        making trees used in games or puzzles.
5.	    The Time complexity of BFS is O(V + E)   The Time complexity of DFS is also O(V + E) when Adjacency List is used and O(V^2) when Adjacency Matrix is used, where V stands for vertices and E stands for edges.
        when Adjacency List is used and O(V^2)
        when Adjacency Matrix is used,
        where V stands for vertices and E
        stands for edges.
"""

import queue


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
        q = queue.Queue()
        q.put(root)

        result = 0
        while not q.empty():
            n = q.get()

            if n.left:
                q.put(n.left)

            if n.right:
                q.put(n.right)

            if high >= n.val >= low:
                result += n.val

        return result

    def sum(self, root, low, high):
        if not root:
            return 0

        result = 0
        if high >= root.val >= low:
            result += root.val

        if high >= root.val:
            result += self.sum(root.right, low, high)

        if low <= root.val:
            result += self.sum(root.left, low, high)

        return result


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10, TreeNode(5), TreeNode(15))
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    print(s.sum(root, 7, 15))
    # print(dfs(root, 181))
