import unittest
from lettcode.XOROperationInAnArray import Solution


class XOROperationInAnArray(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(8, s.xorOperation(5, 0))
        self.assertEqual(8, s.xorOperation(4, 3))
        self.assertEqual(7, s.xorOperation(1, 7))
        self.assertEqual(2, s.xorOperation(10, 5))
