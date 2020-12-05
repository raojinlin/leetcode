import unittest
from lettcode.runningSumof1dArray import Solution


class RunningSumof1dArrayTest(unittest.TestCase):
    def test_running_sum(self):
        solution = Solution()
        self.assertEqual(solution.runningSum([1, 2, 3, 4]), [1, 3, 6, 10])
        self.assertEqual(solution.runningSum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(solution.runningSum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17])
