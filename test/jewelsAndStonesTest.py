import unittest
from lettcode.JewelsAndStones import Solution


class JewelsAndStonesTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(0, s.numJewelsInStones('z', 'Z'))
        self.assertEqual(0, s.numJewelsInStones('z', 'ZZ'))
        self.assertEqual(1, s.numJewelsInStones('z', 'Zz'))
        self.assertEqual(2, s.numJewelsInStones('z', 'Zzz'))
        self.assertEqual(3, s.numJewelsInStones('aA', 'aAAbbbb'))

