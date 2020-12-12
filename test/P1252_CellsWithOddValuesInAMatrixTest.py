import unittest
from lettcode.P1252_CellsWithOddValuesInAMatrix import Solution


class P1252CellsWithOddValuesInAMatrixTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(6, Solution().oddCells(2, 3, [[0, 1], [1, 1]]))
        self.assertEqual(0, s.oddCells(2, 2, [[1, 1], [0, 0]]))
