import unittest
from lettcode.P804_UniqueMorseCodeWords import Solution


class P804UniqueMorseCodeWordsTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(2, s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))