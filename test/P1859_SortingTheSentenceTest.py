import unittest
from lettcode.P1859_SortingTheSentence import Solution


class P1859_SortingTheSentenceTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.sortSentence("is2 sentence4 This1 a3"), 'This is a sentence')
        self.assertEqual(s.sortSentence("Myself2 Me1 I4 and3"), "Me Myself and I")
        self.assertEqual(s.sortSentence('a4 d1 x2 c3'), 'd x c a')