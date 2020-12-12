import unittest
from lettcode.P709_ToLowerCase import Solution


class P709ToLowerCaseTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual('t', s.toLowerCase('T'))
        self.assertEqual('t.', s.toLowerCase('t.'))
        self.assertEqual('t', s.toLowerCase('t'))
        self.assertEqual('abcd', s.toLowerCase('aBcd'))
        self.assertEqual('abcd', s.toLowerCase('ABCD'))
        self.assertEqual('abc    d', s.toLowerCase('ABC    D'))
