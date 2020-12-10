import unittest
from lettcode.SplitaStringinBalancedStrings import Solution


class SplitaStringinBalancedStringsTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(2, Solution().balancedStringSplit('RLRRRLLRLL'))
        self.assertEqual(1, Solution().balancedStringSplit('RL'))
        self.assertEqual(1, Solution().balancedStringSplit('RRLL'))
        self.assertEqual(4, Solution().balancedStringSplit('RLRRLLRLRL'))
        self.assertEqual(3, Solution().balancedStringSplit('RLLLLRRRLR'))
