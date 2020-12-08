import unittest
from lettcode.CreateTargetArrayInTheGivenOrder import Solution


class CreateTargetArrayInTheGivenOrderTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual([0, 1, 2, 3, 4], Solution().createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
        self.assertEqual([0, 2, 4, 3], Solution().createTargetArray([0, 2, 3, 4], [0, 1, 2, 2, 1]))