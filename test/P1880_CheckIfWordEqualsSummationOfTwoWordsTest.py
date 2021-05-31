import unittest

from lettcode.P1880_CheckIfWordEqualsSummationOfTwoWords import Solution


class P1880_CheckIfWordEqualsSummationOfTwoWordsTest(unittest.TestCase):
    def test_solution(self):
        self.assertTrue(Solution().isSumEqual('acb', 'cba', 'cdb'))
        self.assertFalse(Solution().isSumEqual('aaa', 'a', 'aab'))
        self.assertTrue(Solution().isSumEqual('aaa', 'a', 'aaaa'))
