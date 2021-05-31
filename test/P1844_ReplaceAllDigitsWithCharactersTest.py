import unittest

from lettcode.P1844_ReplaceAllDigitsWithCharacters import Solution


class P1844_ReplaceAllDigitsWithCharactersTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual('abcdef', Solution().replaceDigits("a1c1e1"))
        self.assertEqual('xx', Solution().replaceDigits("x0"))
