import unittest
from lettcode.P1732_FindTheHighestAltitude import Solution


class P1732_FindTheHighestAltitudeTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(Solution().largestAltitude([-5, 1, 5, 0. -7]), 1)
        self.assertEqual(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]), 0)