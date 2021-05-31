import unittest

from lettcode.P1684_CountTheNumberOfConsistentStrings import Solution


class P1684_CountTheNumberOfConsistentStringsTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(2, solution.countConsistentStrings('abc', ['a', 'b', 'abcd']))
        self.assertEqual(3, solution.countConsistentStrings('abc', ['a', 'b', 'abc']))
        self.assertEqual(0, solution.countConsistentStrings('a', ['ad', 'ab', 'abc']))
        self.assertEqual(7, solution.countConsistentStrings('abc', ["a", "b", "c", "ab", "ac", "bc", "abc"]))
        self.assertEqual(4, solution.countConsistentStrings('cad', ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
