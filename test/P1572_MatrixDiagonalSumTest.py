import unittest
from lettcode.P1572_MatrixDiagonalSum import Solution


class P1572MatrixDiagonalSumTest(unittest.TestCase):
    def test_solution(self):
        mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
        self.assertEqual(25, Solution().diagonalSum(mat))

        mat = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]
        self.assertEqual(8, Solution().diagonalSum(mat))