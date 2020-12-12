"""
1295. Find Numbers with Even Number of Digits

Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

    Input: nums = [12,345,2,6,7896]
    Output: 2
    Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
    Therefore only 12 and 7896 contain an even number of digits.

Example 2:

    Input: nums = [555,901,482,1771]
    Output: 1
    Explanation:
    Only 1771 contains an even number of digits.


Constraints:

    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
"""


class Solution(object):
    def get_digits(self, num):
        digits = 0
        while num > 0:
            num = num // 10
            digits += 1

        return digits

    def is_even_number_of_digits(self, num):
        return self.get_digits(num) % 2 == 0

    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            if self.is_even_number_of_digits(num):
                result += 1

        return result


if __name__ == '__main__':
    print(Solution().findNumbers([12, 345, 2, 6, 7896]))