import unittest
from lettcode.kidsWiththeGreatestNumberOfCandies import Solution


class kidsWiththeGreatestNumberOfCandiesTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.kidsWithCandies([4, 2, 1, 1, 2], 1), [True, False, False, False, False])
        self.assertEqual(solution.kidsWithCandies([12, 1, 12], 10), [True, False, True])
        self.assertEqual(solution.kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
