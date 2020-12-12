"""
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.


Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that
are not part of the primary diagonal.

Example 1:
    Input: mat = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
    Output: 25
    Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
    Notice that element mat[1][1] = 5 is counted only once.

Example 2:

    Input: mat = [[1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1],
                  [1,1,1,1]]
    Output: 8

Example 3:

    Input: mat = [[5]]
    Output: 5

"""


class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m = len(mat)
        if m == 1:
            return mat[0][0]

        counted = {}
        result = 0

        i = 0
        j = 0
        while i < m and j < m:
            result += mat[i][j]
            counted['%d%d' % (i, j)] = 1
            j += 1
            i += 1

        i = 0
        j = m - 1
        while m > i and m > j >= 0:
            if '%d%d' % (i, j) not in counted:
                result += mat[i][j]

            i += 1
            j -= 1

        return result


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(Solution().diagonalSum(mat))

    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(Solution().diagonalSum(mat))
