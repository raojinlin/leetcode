import unittest
from lettcode.P1290_ConvertBinaryNumberInALinkedListToInteger import Solution, ListNode


class P1290ConvertBinaryNumberInAlinkedListToIntegerTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(18880, s.getDecimalValue(ListNode.from_list(1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)))
        self.assertEqual(18880, s.getDecimalValueBit(ListNode.from_list(1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0)))
        self.assertEqual(5, s.getDecimalValueBit(ListNode.from_list(1, 0, 1)))