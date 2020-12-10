import unittest
from lettcode.HowManyNumbersAreSmallerThanTheCurrentNumber import Solution


class HowManyNumbersAreSmallerThanTheCurrentNumberTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual([0, 1, 2, 3], s.smallerNumbersThanCurrent([1, 2, 3, 4]))
        self.assertEqual([3, 0, 1, 2], s.smallerNumbersThanCurrent([8, 2, 3, 4]))
        self.assertEqual([3, 1, 2, 0], s.smallerNumbersThanCurrent([8, 2, 3, 0]))
