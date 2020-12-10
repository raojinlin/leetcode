import unittest
from lettcode.ShuffleString import Solution


class ShuffleStringTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.restoreString('codeleet', [4, 5, 6, 7, 0, 1, 2, 3]), 'leetcode')
        self.assertEqual(s.restoreString('aiohn', [3, 1, 4, 2, 0]), 'nihao')
        self.assertEqual(s.restoreString('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]), 'arigatou')
        self.assertEqual(s.restoreString('art', [1, 0, 2]), 'rat')
