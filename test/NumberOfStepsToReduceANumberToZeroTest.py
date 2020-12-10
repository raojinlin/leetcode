import unittest
from lettcode.NumberOfStepsToReduceANumberToZero import Solution


class NumberOfStepsToReduceANumberToZeroTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(12, s.numberOfSteps(123))
        self.assertEqual(4, s.numberOfSteps(8))
        self.assertEqual(6, s.numberOfSteps(14))
        self.assertEqual(3, s.numberOfSteps(3))
