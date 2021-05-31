"""
You are given an integer array nums (0-indexed). In one operation,
you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1.
An array of length 1 is trivially strictly increasing.



Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:

4 + 3 + 7
Input: nums = [1,5,2,4,1]
Explanation:

1) Increment nums[3], so numbs becomes [1, 5, 3, 4, 1]
2) Increment nums[3], so numbs becomes [1, 5, 4, 4, 1]
3) Increment nums[3], so numbs becomes [1, 5, 5, 4, 1]
4) Increment nums[3], so numbs becomes [1, 5, 6, 4, 1]
5) Increment nums[4], so numbs becomes [1, 5, 6, 5, 1]
6) Increment nums[4], so numbs becomes [1, 5, 6, 6, 1]
7) Increment nums[4], so numbs becomes [1, 5, 6, 7, 1]
8) Increment nums[5], so numbs becomes [1, 5, 6, 7, 2]
9) Increment nums[5], so numbs becomes [1, 5, 6, 7, 3]
10) Increment nums[5], so numbs becomes [1, 5, 6, 7, 4]
11) Increment nums[5], so numbs becomes [1, 5, 6, 7, 5]
12) Increment nums[5], so numbs becomes [1, 5, 6, 7, 6]
13) Increment nums[5], so numbs becomes [1, 5, 6, 7, 7]
14) Increment nums[5], so numbs becomes [1, 5, 6, 7, 8]

Output: 4 + 3 + 7 = 14

Example 3:

Input: nums = [8]
Output: 0

"""


class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                j += (nums[i-1] - nums[i]) + 1
                nums[i] = nums[i-1] + 1

        return j
