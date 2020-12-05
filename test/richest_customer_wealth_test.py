import unittest
from lettcode.richestCustomerWealth import Solution


class RichestCustomerWealthTest(unittest.TestCase):
    def test_solution(self):
        solution = Solution()
        self.assertEqual(13, solution.maximumWealth([[10, 3], [1, 2, 3], [4, 1, 6]]))
        self.assertEqual(23, solution.maximumWealth([[10, 3], [20, 3], [4, 1, 6]]))
        self.assertEqual(6, solution.maximumWealth([[1, 2, 3], [3, 2, 1]]))
        self.assertEqual(10, solution.maximumWealth([[1, 5], [7, 3], [3, 5]]))
        self.assertEqual(17, solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))


if __name__ == '__main__':
    unittest.main()