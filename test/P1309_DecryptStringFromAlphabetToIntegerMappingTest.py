import unittest
from lettcode.P1309_DecryptStringFromAlphabetToIntegerMapping import Solution, encode


class P1309DecryptStringFromAlphabetToIntegerMappingTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual('jkab', Solution().freqAlphabets('10#11#12'))
        self.assertEqual('abcdefghijklmnopqrstuvwxyz', Solution().freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
        self.assertEqual('acz', Solution().freqAlphabets("1326#"))
        self.assertEqual('y', Solution().freqAlphabets("25#"))
        self.assertEqual('azy', Solution().freqAlphabets(encode('azy')))
