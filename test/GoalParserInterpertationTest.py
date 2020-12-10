import unittest
from lettcode.GoalParserInterpertation import Solution


class GoalParserInterpertationTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.interpret('G()()()'), 'Gooo')
        self.assertEqual(s.interpret('G()(al)()'), 'Goalo')
        self.assertEqual(s.interpret('G()()()(al)'), 'Goooal')
        self.assertEqual(s.interpret('G(al)()()'), 'Galoo')
        self.assertEqual(s.interpret('G(al)()()al'), 'Galoo')
