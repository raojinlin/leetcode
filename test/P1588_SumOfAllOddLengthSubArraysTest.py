import unittest
from lettcode.P1588_SumOfAllOddLengthSubarrays import Solution


class P1588SumOfAllOddLengthSubarraysTest(unittest.TestCase):
    def test_sulotion(self):
        self.assertEqual(58, Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
        self.assertEqual(5, Solution().sumOddLengthSubarrays([1, 4]))
        self.assertEqual(16, Solution().sumOddLengthSubarrays([1, 4, 3]))
        self.assertEqual(66, Solution().sumOddLengthSubarrays([10, 11, 12]))
        self.assertEqual(0, Solution().sumOddLengthSubarrays([]))
        self.assertEqual(1, Solution().sumOddLengthSubarrays([1]))
        self.assertEqual(2, Solution().sumOddLengthSubarrays([1, 1]))
        self.assertEqual(10, Solution().sumOddLengthSubarrays([1, 1, 1, 1]))
