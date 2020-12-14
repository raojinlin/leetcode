from lettcode.P1351_CountNegativeNumbersInASortedMatrix import Solution
import unittest


class P1351CountNegativeNumbersInASortedMatrixTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(8, solution.countNegatives([
            [4, 3, 2, -1],
            [3, 2, 1, -1],
            [1, 1, -1, -2],
            [-1, -1, -2, -3]
        ]))

        self.assertEqual(0, solution.countNegatives([[3, 2], [1, 0]]))
        self.assertEqual(3, solution.countNegatives([[1, -1], [-1, -1]]))