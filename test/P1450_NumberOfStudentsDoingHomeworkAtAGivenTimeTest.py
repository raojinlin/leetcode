import unittest
from lettcode.P1450_NumberOfStudentsDoingHomeworkAtAGivenTime import Solution


class P1450NumberOfStudentsDoingHomeworkAtAGivenTimeTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(1, s.busyStudent(startTime=[1, 2, 3], endTime=[3, 2, 7], queryTime=4))
        self.assertEqual(1, s.busyStudent(startTime=[4], endTime=[4], queryTime=4))
        self.assertEqual(5, s.busyStudent(startTime=[9, 8, 7, 6, 5, 4, 3, 2, 1], endTime=[10, 10, 10, 10, 10, 10, 10, 10, 10], queryTime=5))
