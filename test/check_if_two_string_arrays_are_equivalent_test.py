import unittest
from lettcode.CheckIfTwoStringArraysareEquivalent import Solution


class CheckIfTwoStringArraysareEquivalentTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertFalse(s.arrayStringsAreEqual(["a", "b"], []))
        self.assertTrue(s.arrayStringsAreEqual(["a", "b"], ["ab"]))
        self.assertTrue(s.arrayStringsAreEqual(["ab", "b"], ["a", "b", "b"]))
