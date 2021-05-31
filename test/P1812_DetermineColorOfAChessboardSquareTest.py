import lettcode.P1812_DetermineColorOfAChessboardSquare
import unittest


class DetemineColorOfChessboardSquareTest(unittest.TestCase):
    def test_solution(self):
        solution = lettcode.P1812_DetermineColorOfAChessboardSquare.Solution()
        self.assertTrue(solution.squareIsWhite('a2'))
        self.assertTrue(solution.squareIsWhite('b1'))
        self.assertTrue(solution.squareIsWhite('d1'))
        self.assertFalse(solution.squareIsWhite('a1'))
        self.assertFalse(solution.squareIsWhite('a3'))
        self.assertFalse(solution.squareIsWhite('a5'))
        self.assertFalse(solution.squareIsWhite('a7'))
