"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.
"""


class Solution:
    def helper(self, start, end, memo):
        if start >= end:
            return 1

        if end - start in memo:
            return memo[end - start]
        
        c = 0
        for i in range(start, end + 1):
            left = self.helper(start, i - 1, memo)
            right = self.helper(i + 1, end, memo)

            c += left * right
          
        memo[end - start] = c
        return c

    def numTrees(self, n: int) -> int:
        return self.helper(1, n, {})
    

if __name__ == "__main__":
    print(Solution().numTrees(3))
        