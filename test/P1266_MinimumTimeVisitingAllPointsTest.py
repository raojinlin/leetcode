import unittest
from lettcode.P1266_MinimumTimeVisitingAllPoints import Solution


class P1266MinimumTimeVisitingAllPoints(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(7, Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
        self.assertEqual(5, Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))