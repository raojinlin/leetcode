"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:
    Input: grid = [
        [4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]
    ]
    Output: 8
    Explanation: There are 8 negatives number in the matrix.

Example 2:
    Input: grid = [[3,2],[1,0]]
    Output: 0

Example 3:
    Input: grid = [[1,-1],[-1,-1]]
    Output: 3

Example 4:
    Input: grid = [[-1]]
    Output: 1


Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

"""


class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        count = 0
        for i in range(m):
            j = 0
            while j < n:
                if grid[i][j] < 0:
                    count += n - j
                    j = n
                else:
                    j += 1

        return count


if __name__ == '__main__':
    s = Solution()
    c = s.countNegatives([
        [4, 3, 2, -1],
        [3, 2, 1, -1],
        [1, 1, -1, -2],
        [-1, -1, -2, -3]
    ])

    print(s.countNegatives([[3, 2], [1, 0]]))
    print(s.countNegatives([[1, -1], [-1, -1]]))

    print(c)