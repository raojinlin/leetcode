import unittest
from lettcode.DecompressRunLengthEncodedList import Solution


class DecompressRunLengthEncodedListTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(solution.decompressRLElist([1, 3, 2, 4, 3, 5]), [3, 4, 4, 5, 5, 5])
        self.assertEqual(solution.decompressRLElist([4, 4]), [4, 4, 4, 4])
        self.assertEqual(solution.decompressRLElist([1, 3, 4, 4]), [3, 4, 4, 4, 4])
