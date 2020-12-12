import unittest
from lettcode.P1534_CountGoodTriplets import Solution


class P1534CountGoodTripletsTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(4, Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
        self.assertEqual(0, Solution().countGoodTriplets(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1))