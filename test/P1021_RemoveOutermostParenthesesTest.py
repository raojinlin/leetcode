import unittest
from lettcode.P1021_RemoveOutermostParentheses import Solution


class P1021RemoveOutermostParenthesesTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual('()()()', s.removeOuterParentheses("(()())(())"))
        self.assertEqual('()()()()(())', s.removeOuterParentheses("(()())(())(()(()))"))
        self.assertEqual('', s.removeOuterParentheses("()()"))