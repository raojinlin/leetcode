import unittest
from lettcode.P1436_DestinationCity import Solution


class P1436DestinationCity(unittest.TestCase):
    def test_solution(self):
        self.assertEqual('a', Solution().destCity([['b', 'c'], ['d', 'b'], ['c', 'a']]))
        self.assertEqual('Sao Paulo', Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
        self.assertEqual('z', Solution().destCity([['a', 'z']]))
