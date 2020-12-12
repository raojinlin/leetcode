"""
1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.



Example 1:
    Input: arr = [1,4,2,5,3]
    Output: 58
    Explanation: The odd-length subarrays of arr and their sums are:
    [1] = 1
    [4] = 4
    [2] = 2
    [5] = 5
    [3] = 3
    [1,4,2] = 7
    [4,2,5] = 11
    [2,5,3] = 10
    [1,4,2,5,3] = 15
    If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58


Example 3:

Input: arr = [10,11,12]
Output: 66
"""


class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(arr)):
            j = i
            while j < len(arr):
                sub_list_len = j - i + 1
                if sub_list_len % 2 == 1:
                    result += sum(arr[i:j+1])
                    j += 2
                else:
                    j += 1

        return result


if __name__ == '__main__':
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
    print(Solution().sumOddLengthSubarrays([1, 4]))
    print(Solution().sumOddLengthSubarrays([1, 4, 3]))
    print(Solution().sumOddLengthSubarrays([10, 11, 12]))
