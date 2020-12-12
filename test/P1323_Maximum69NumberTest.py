import unittest
from lettcode.P1323_Maximum69Number import Solution


class P1323Maximum69NumberTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(9996, Solution().maximum69Number(9966))
