import unittest
from lettcode.P1295_FindNumbersWithEvenNumberOfDigits import Solution


class P1295FindNumbersWithEvenNumberOfDigitsTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(1, s.findNumbers([12, 1]))
        self.assertEqual(4, s.findNumbers([12, 12, 23, 234, 2334]))
