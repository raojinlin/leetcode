import unittest
from lettcode.MaximumNestingDepthoftheParentheses import Solution


class MaximumNestingDepthoftheParenthesesTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(3, s.maxDepth("(1)+((2))+(((3)))"))
        self.assertEqual(1, s.maxDepth("1+(2*3)/(2-1)"))
        self.assertEqual(0, s.maxDepth('1'))
        self.assertEqual(3, s.maxDepth("(1+(2*3)+((8)/4))+1"))
