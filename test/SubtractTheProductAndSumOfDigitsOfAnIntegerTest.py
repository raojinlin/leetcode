import unittest
from lettcode.SubtractTheProductAndSumOfDigitsOfAnInteger import Solution


class SubtractTheProductAndSumOfDigitsOfAnIntegerTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(0, s.subtractProductAndSum(123))
        self.assertEqual(15, s.subtractProductAndSum(234))
        self.assertEqual(21, s.subtractProductAndSum(4421))
