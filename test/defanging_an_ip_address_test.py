import unittest
from lettcode.defangingAnIPAddress import Solution


class DefangingAnIPAddressTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual('1[.]1[.]1[.]1', solution.defangIPaddr('1.1.1.1'))
        self.assertEqual('255[.]100[.]50[.]0', solution.defangIPaddr('255.100.50.0'))
