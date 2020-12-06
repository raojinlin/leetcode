"""
1512. Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.



Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1

        return result

    def numIdenticalPairsWtihMap(self, nums):
        m = dict()
        for n in nums:
            i = 1
            if n in m:
                i = m[n] + 1

            m[n] = i

        r = 0
        for i in m.values():
            if i > 1:
                r += (i * (i - 1)) / 2

        return r


if __name__ == '__main__':
    s = Solution()
    print(s.numIdenticalPairs([1, 1, 1, 1]))
