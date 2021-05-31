import unittest
from lettcode.P1688_CountOfMatchesInTournament import Solution


class P1688_CountOfMatchesInTournamentTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(13, s.numberOfMatches(14))
        self.assertEqual(6, s.numberOfMatches(7))
