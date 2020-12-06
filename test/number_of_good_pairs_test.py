import unittest
from lettcode.numberOfGoodPairs import Solution


class NumberOfGoodPairs(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(6, s.numIdenticalPairs([1, 1, 1, 1]))
        self.assertEqual(4, s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
        self.assertEqual(0, s.numIdenticalPairs([1, 2, 3]))

    def test_solution2(self):
        s = Solution()
        self.assertEqual(6, s.numIdenticalPairsWtihMap([1, 1, 1, 1]))
        self.assertEqual(4, s.numIdenticalPairsWtihMap([1, 2, 3, 1, 1, 3]))
        self.assertEqual(0, s.numIdenticalPairsWtihMap([1, 2, 3]))
